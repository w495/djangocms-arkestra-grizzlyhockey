"""
Extract simple HTML and presentation info from combined HTML
"""

from semanticeditor.common import parse, get_structure, get_classes_for_node, html_extract, strip_presentation
from semanticeditor.definitions import PresentationClass, NEWROW, NEWCOL, NEWINNERROW, NEWINNERCOL
from semanticeditor.layout import get_layout_details_strategy
from semanticeditor.utils.etree import get_parent, get_index
from semanticeditor.utils.general import any


def extract_structure(content):
    """
    Extracts H1, H2, etc headings, and other block level elements and
    returns a list of tuples containing (level, name, tag)
    """
    # This function is no longer used externally, but it has tests
    # against it that are useful at checking the behaviour of get_structure
    tree = parse(content, clean=True)
    structure = get_structure(tree, assert_structure=True)
    return structure


def extract_presentation(html):
    """
    Takes HTML with formatting applied and returns presentation elements (a
    dictionary with keys = section names, values = set of classes/commands) and
    the HTML without formatting (ready to be used in an editor)
    """
    # TODO: this function is not brilliantly well defined e.g.  should
    # there be an entry in the dictionary for sections with no
    # formatting?  This does not affect functionality, but it does
    # affect tests.
    layout_strategy = get_layout_details_strategy()
    html = layout_strategy.extract_pre_parse_hacks(html)
    root = parse(html, clean=False) # it's important we don't clean.
    root = layout_strategy.extract_post_parse_hacks(root)
    structure = get_structure(root)
    structure = layout_strategy.extract_structure_hacks(structure)
    pres = {}
    layout_commands = find_all_layout_nodes(root, layout_strategy)
    for si in structure:
        pres[si.sect_id] = set()

        # Section - extract classes
        for c in get_classes_for_node(si.node):
            pres[si.sect_id].add(PresentationClass(c))
            if 'class' in si.node.attrib:
                del si.node.attrib['class']

        # Add custom ids.  These are only for purpose of editing,
        # and will be removed again at end of format_html
        si.node.set('id', si.sect_id)

        # Now, deal with layout divs for this structure item
        cmd_pairs = layout_commands.get(si.node, [])
        for cmd, div_node in cmd_pairs:
            # Need to create another entry in pres
            pres_name = cmd.prefix + si.sect_id
            cmd_classes = set()

            # Find the classes that correspond to PresentationClass objects and
            # add them.
            node_classes = set(get_classes_for_node(div_node))
            if cmd in (NEWROW, NEWINNERROW):
                filterfunc = layout_strategy.is_row_class
            else:
                filterfunc = layout_strategy.is_column_class
                # Need the classes from the inner column div
                children = div_node.getchildren()
                if len(children) > 0 and children[0].tag == 'div':
                    node_classes |= set(get_classes_for_node(children[0]))

            for c in node_classes:
                if not filterfunc(c):
                    cmd_classes.add(PresentationClass(c))

            cmd_classes.add(cmd) # not strictly necessary, but helps testing
            pres[pres_name] = cmd_classes

    strip_presentation(root)
    out_html = html_extract(root)

    return (pres, out_html)


def find_all_layout_nodes(node, layout_strategy, depth=0, current_stack=None,
                          layout_divs=None, layout_commands=None):
    """
    Finds all the layout divs, and the content node they correspond to.
    Returns a dictionary:
       content node: [stack of (command, command node)],
    """
    if layout_commands is None:
        # Rather than messing with lots of return values, we define
        # a containers for collecting the results.
        layout_commands = {}

    if current_stack is None:
        current_stack = []

    children = node.getchildren()

    # Find out the command that corresponds to curent node
    if node.tag == 'div':
        c_classes = get_classes_for_node(node)
        is_col = any(layout_strategy.is_column_class(c) for c in c_classes)
        is_row = any(layout_strategy.is_row_class(c) for c in c_classes)
        if not is_col and len(current_stack) > 0 and \
                current_stack[-1][0] in (NEWROW, NEWINNERROW):
            # A div inside a row is always a column
            is_col = True
        if is_col:
            if depth == 0:
                current_stack.append((NEWCOL, node))
                depth += 1
            else:
                current_stack.append((NEWINNERCOL, node))
        elif is_row:
            current_stack.append((NEWROW if depth == 0 else NEWINNERROW, node))

    else:
        is_row, is_col = False, False


    # Is the current node the one the stack applies to?
    if not (is_col or is_row) and len(current_stack) > 0:
        # If this is the additional inner column div, we want to skip it
        if node.tag != 'div':
            layout_commands[node] = current_stack
            current_stack = []

    # The current stack of commands applies to the first content node that is a
    # descendent of them. We only look in first child, recursively.
    for i, child in enumerate(children):
        if i == 0:
            # Look for content node
            find_all_layout_nodes(child, layout_strategy, depth=depth,
                                  current_stack=current_stack,
                                  layout_commands=layout_commands)
        else:
            # Not the first child, so we reset the current_stack
            find_all_layout_nodes(child, layout_strategy, depth=depth,
                                  current_stack=[],
                                  layout_commands=layout_commands)

    return layout_commands
