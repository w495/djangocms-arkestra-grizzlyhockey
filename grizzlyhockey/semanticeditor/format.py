"""
Combine simple HTML and presentation info into rendered HTML
"""
from lxml import etree as ET

from semanticeditor.common import strip_presentation, get_classes_from_presinfo, html_extract, parse, get_structure
from semanticeditor.definitions import PREVIEW_BLOCKDEF, BLOCKDEF
from semanticeditor.layout import create_layout, check_layout, get_layout_details_strategy
from semanticeditor.utils.etree import indent

## Main functions and sub functions
def format_html(html, styleinfo, return_tree=False, pretty_print=False):
    """
    Formats the XHTML given using a dictionary of style information.
    The dictionary has keys which are the ids of sections,
    and values which are lists of CSS classes or special commands.
    """
    layout_strategy = get_layout_details_strategy()
    html = layout_strategy.format_pre_parse_hacks(html, styleinfo)
    root = parse(html, clean=True)
    root = layout_strategy.format_post_parse_hacks(root, styleinfo)
    structure = get_structure(root, assert_structure=True)
    structure = layout_strategy.format_structure_hacks(structure, styleinfo)
    sect_ids = [s.sect_id for s in structure]
    styleinfo = _sanitise_styleinfo(styleinfo, sect_ids)

    # Strip existing divs, otherwise we cannot format properly.  If
    # there are other block level elements that mess things up, we
    # raise BadStructure later, but divs have no semantics so can just
    # be removed.
    strip_presentation(root)

    # Apply normal CSS classes.
    for si in structure:
        # Apply css styles
        classes = get_classes_from_presinfo(styleinfo[si.sect_id])
        classes.sort()
        if classes:
            si.node.set("class", " ".join(classes))

    # Create layout from row/column commands
    layout = create_layout(root, styleinfo, structure)
    for c in layout.content:
        check_layout(c, structure, layout_strategy)
    # Create new ET tree from layout.  The individual nodes that belong to
    # 'root' are not altered, but just added to a new tree.  This means that the
    # information in 'structure' does not need updating.
    nodes = []

    for content in layout.content:
        nodes.extend(content.as_nodes(layout_strategy))
    rendered = ET.fromstring("<html><body></body></html>")
    rendered.getchildren()[0].extend(nodes)

    # Apply hacks
    rendered = layout_strategy.format_post_layout_hacks(rendered, structure, styleinfo)

    # Pretty print
    if pretty_print:
        indent(rendered)

    # Remove the temporary IDs we may have added when splitting the HTML
    # into content and presentation.  We don't do this before this point,
    # as the IDs need to be there to identify sections
    for si in structure:
        if 'id' in si.node.attrib:
            del si.node.attrib['id']

    if return_tree:
        return (rendered, structure)
    else:
        return html_extract(rendered)


def preview_html(html, pres):
    root, structure = format_html(html, pres, return_tree=True)
    structure2 = [si for si in structure if si.tag in PREVIEW_BLOCKDEF]
    known_nodes = dict((si.node, si) for si in structure2)
    _create_preview(root, structure2, known_nodes)
    return html_extract(root)

def _create_preview(node, structure, known_nodes):
    children = node.getchildren()
    if children and children[0].tag == 'body':
        children = children[0].getchildren()
    for n in children:
        if n.tag == 'div' and n not in known_nodes:
            _create_preview(n, structure, known_nodes)
        else:
            sect = known_nodes.get(n)
            if sect is not None and (n.tag in BLOCKDEF or n.tag == 'div'):
                n.set('class', 'structural ' + "tag" + n.tag.lower())
                n.tag = "div"
                n[:] = []
                n.text = sect.name
            else:
                node.remove(n)


def _sanitise_styleinfo(styleinfo, sect_ids):
    # Replace lists with sets
    out = {}
    for k, v in styleinfo.items():
        out[k] = set(v)

    # Ensure that all sections have an entry in styleinfo
    for sect_id in sect_ids:
        if not sect_id in out:
            out[sect_id] = set()

    return out
