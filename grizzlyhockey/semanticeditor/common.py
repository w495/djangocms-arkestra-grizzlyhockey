"""
Functionality common to different parts of the HTML manipulation
(but not generic enough for utils)
"""

from lxml import etree as ET
from lxml.html import HTMLParser

from semanticeditor.definitions import IncorrectHeadings, BLOCKDEF, BLOCK_LEVEL_TRIM_LENGTH, HEADINGDEF
from semanticeditor.utils.datastructures import struct
from semanticeditor.utils.etree import flatten, get_depth, cleanup

### Structure related ###

class StructureItem(object):
    __metaclass__ = struct
    level = 0     #    level is the 'outline level' in the document i.e. an integer
    sect_id = ''  #    sect_id is a unique ID used for storing presentation information against
    name = ''     #    name is a user presentable name for the section
    tag = ''      #    tag is the HTML element e.g. h1
    node = None   #    node is the ElementTree node


def get_structure(root, assert_structure=False):
    """
    Return the structure nodes, as a list of StructureItems.  Structure nodes
    are nodes that can have commands or classes applied to them.
    """
    retval = []
    sect_ids = set()
    headings_used = False
    cur_level = 1
    last_heading_num = 0
    first_heading_level = 1

    # Pre-pass to get existing ids.
    for n in root.getiterator():
        if n.tag in BLOCKDEF:
            sect_id = n.get('id')
            if sect_id is not None:
                if sect_id in sect_ids:
                    # don't use duplicate ids.
                    del n.attrib['id']
                else:
                    # reserve
                    sect_ids.add(sect_id)

    for n in root.getiterator():
        if n.tag in BLOCKDEF:
            text = flatten(n)
            sect_id = n.get('id')
            if sect_id is None:
                sect_id = _make_sect_id(n.tag, sect_ids)
            sect_ids.add(sect_id)
            if n.tag in HEADINGDEF:
                name = text
                level = int(n.tag[1])
                cur_level = level
                if assert_structure:
                    if not headings_used:
                        first_heading_level = level
                    else:
                        if level < first_heading_level:
                            raise IncorrectHeadings("No heading can be higher than the first "
                                                    "heading, which was H%d." %
                                                    first_heading_level)

                    # Heading level should decrease or increase by no more than one.
                    if headings_used and level > last_heading_num + 1:
                        raise IncorrectHeadings('Heading "%(name)s" is level H%(foundnum)d, '
                                                'but it should be level H%(rightnum)d or less' %
                                                dict(name=name, foundnum=level,
                                                     rightnum=last_heading_num + 1))

                if name == "":
                    name = "?"

                last_heading_num = level
                headings_used = True
            else:
                name = text[0:BLOCK_LEVEL_TRIM_LENGTH]
                if name == '':
                    name = '?'
                else:
                    name = name + "..."

                # Paragraphs etc within a section should be indented
                # one further than the heading above them.
                if not headings_used:
                    level = 1
                else:
                    level = cur_level + 1

            # Level is adjusted so that e.g. H3 is level 1, if it is
            # the first to appear in the document.
            # It is also adjusted so that nested items (e.g. p in blockquote)
            # appear to be nested.
            nesting_level = get_depth(root, n) - 2
            retval.append(StructureItem(level=nesting_level + level - first_heading_level + 1,
                                        sect_id=sect_id,
                                        name=name,
                                        tag=n.tag.lower(),
                                        node=n))

    return retval


def _make_sect_id(tag, used_ids):
    i = 1
    while True:
        attempt = tag + "_" + str(i)
        if attempt not in used_ids:
            return attempt
        else:
            i += 1


def parse(content, clean=False):
    """
    Parses the HTML provided into an ElementTree.
    If 'clean' is True, lax parsing is done, the tree is cleaned
    of dirty user provided HTML
    """
    # We also use HTMLParser for 'strict', because the XML parser seems to eliminate
    # '\r' for some reason.
    tree = ET.fromstring(u'<html><body>' + content + u'</body></html>', parser=HTMLParser())
    if clean:
        from semanticeditor.clean import clean_tree
        clean_tree(tree)
    return tree


def html_extract(root):
    return ET.tostring(root).replace('<html>', '').replace('</html>', '').replace('<body>', '').replace('</body>', '').replace('<body/>','').replace("<head/>", "").replace("&#13;", "\r")


def get_classes_for_node(node):
    return filter(len, node.get('class', '').split(' '))


def get_classes_from_presinfo(presinfos):
    # Extract a list of classes from a list of PresentationInfo objects
    return [pi.name for pi in presinfos if pi.prestype == "class"]


def strip_presentation(tree):
    cleanup(tree, lambda t: t.tag == 'div')
