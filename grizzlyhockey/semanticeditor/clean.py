"""
Utilities for cleaning user HTML
"""

from lxml import etree as ET
from pyquery import PyQuery as pq

from semanticeditor.common import html_extract, parse, get_classes_for_node
from semanticeditor.definitions import BLOCKDEF_SELECTOR, COMMANDS
from semanticeditor.utils.etree import get_parent, get_index, eliminate_tag, empty_text
from django.conf import settings

disallowed_elements = getattr(settings, "SEMANTICEDITOR_DISALLOWED_ELEMENTS", ['span', 'li p:only-child', 'table', 'tbody', 'thead', 'tr', 'td'])

def clean_tree(root):
    """
    Cleans dirty HTML from an ElementTree
    """
    initial_html = ET.tostring(root)
    body = root[0] # <html><body>
    # If there is text directly in body, it needs wrapping in a block element.
    _promote_child_text(body, 'p')

    # replace 'command' divs
    _remove_command_divs(body)

    # First replace divs
    _replace_block_elements(body)

    # Deal with nested 'p's and other elements.
    _clean_nested(body)

    doc = pq(root)
    doc('*').each(_clean_elem)
    doc('style').remove()
    doc('col').remove()

    def pull_up(n):
        p = get_parent(body, n)
        i = get_index(p, n)
        eliminate_tag(p, i)

    for x in disallowed_elements: 
        for n in doc(x):
            pull_up(n)
    # "li p:only-child" appears to be buggy.  It works like
    # "li p:only-descendent" or something.

    for x in ['strong', 'em', 'b', 'i']:
        for n in doc(x):
            if pq(n).is_(BLOCKDEF_SELECTOR):
                pull_up(n)

    # remove duplicate 'id' attributes.
    ids = [n.get('id', None) for n in doc('*[id]')]
    ids = [i for i in ids if i != "" and i != None]
    for i in set(ids):
        for j, node in enumerate(doc('#' + i)):
            if (j > 0): # skip the first one
                del node.attrib['id']

    doc('p + br').remove()
    for par in doc('p:empty'):
        if par.text is None  or par.text.strip() == "":
            par.getparent().remove(par)

    # Removed elements can give problems which need to be fixed again.  We keep
    # iterating through this until we get the same answer!
    output_html = ET.tostring(root)
    if initial_html == output_html:
        return
    else:
        clean_tree(root)


def clean_html(html):
    tree = parse(html, clean=True)
    return html_extract(tree)


def _clean_text(t):
    return t.replace(u'\xa0', u' ')


def _clean_elem(i, d):
    for x in ['style', 'class']:
        try:
            del d.attrib[x]
        except KeyError:
            pass
    for elem in d:
        if elem.text is not None:
            elem.text = _clean_text(elem.text)
        if elem.tail is not None:
            elem.tail = _clean_text(elem.tail)


def _promote_child_text(elem, tag):
    """
    Ensure any leading or trailing text directly as a child of elem is wrapped
    in a tag.
    """
    if not empty_text(elem.text):
        newtag = ET.Element(tag)
        newtag.text = elem.text
        elem.insert(0, newtag)
        elem.text = None

    if len(elem) > 0 and not empty_text(elem[-1].tail):
        newtag = ET.Element(tag)
        newtag.text = elem[-1].tail
        elem[-1].tail = None
        elem.append(newtag)


def _clean_nested(elem):
    for idx, child in reversed(list(enumerate(elem.getchildren()))):
        # (do it reversed so that indexes never change as we mutate children)
        _clean_nested(child)
        if child.tag == 'p' and elem.tag == 'p':
            eliminate_tag(elem, idx)


def _replace_block_elements(elem):
    for child in elem.getchildren():
        if child.tag == 'div':
            child.tag = 'p'
        _replace_block_elements(child)


def _remove_command_divs(elem):
    for child in reversed(elem.getchildren()):
        _remove_command_divs(child)
        if child.tag == 'div' or child.tag == 'p':
            classes = set(get_classes_for_node(child))
            if any(c.name in classes for c in COMMANDS):
                elem.remove(child)
