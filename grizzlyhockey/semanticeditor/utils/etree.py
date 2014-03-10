"""
etree/ElementTree utils
"""

# ElementTree utilities.  Lots of these are pinched
# from proposed 'ElementLib' module on effbot.

def textjoin(a, b):
    a = a or ''
    b = b or ''
    return a + b

def cleanup(elem, filter):
    """
    Removes start and stop tags for any element for which the filter
    function returns True.  If you want to remove the entire element,
    including all subelements, use the 'clear' method inside the
    filter callable.

    Note that this function modifies the tree in place.
    @param elem An element tree.
    @param filter An filter function.  This should be a callable that
    takes an element as its single argument, and returns True if the
    element should be cleaned.
    """

    out = []
    for e in elem:
        cleanup(e, filter)
        if filter(e):
            if e.text:
                if out:
                    out[-1].tail = textjoin(out[-1].tail, e.text)
                else:
                    elem.text = textjoin(elem.text, e.text)
            out.extend(e)
            if e.tail:
                if out:
                    out[-1].tail = textjoin(out[-1].tail, e.tail)
                else:
                    elem.text = textjoin(elem.text, e.tail)
        else:
            out.append(e)
    elem[:] = out

def flatten(elem):
    text = elem.text or ""
    for e in elem:
        text += flatten(e)
        if e.tail:
            text += e.tail
    return text

def get_parent(topnode, elem):
    """
    Return the parent of 'elem'.

    topnode is the node to start searching from
    """
    for n in topnode.getiterator():
        if elem in n.getchildren():
            return n
    return None

def get_depth(topnode, elem, _start=0):
    """
    Returns the depth of elem in the tree, 0 for root node
    """
    if elem is topnode:
        return _start
    for n in topnode.getchildren():
        d = get_depth(n, elem, _start + 1)
        if d is not None:
            return d
    return None

def get_index(parent, elem):
    """
    Return the index of elem in parent's children
    """
    return list(parent.getchildren()).index(elem)

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for child in elem:
            indent(child, level+1)
        if not child.tail or not child.tail.strip():
            child.tail = i
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def eliminate_tag(parent, index):
    """
    Eliminates the tag from node at index 'index' from the parent.  The contents
    are pulled up into parent.
    """
    elem = parent[index]

    first = index == 0
    last = index == len(parent) - 1

    # 'text'
    if first:
        # 'text' merges with parents.
        parent.text = textjoin(parent.text, elem.text)
    else:
        # 'text' merges with tail of previous sibling
        prev = parent[index-1]
        prev.tail = textjoin(prev.tail, elem.text)
    # 'tail'
    if len(elem.getchildren()) > 0:
        # tail always goes on last child's tail
        elem[-1].tail = textjoin(elem[-1].tail, elem.tail)
    else:
        if first:
            # tail goes on parents text
            parent.text = textjoin(parent.text, elem.tail)
        elif last: # (and not first)
            prev = parent[index-1]
            prev.tail = textjoin(prev.tail, elem.tail)
        else:
            next = parent[index+1]
            next.text = textjoin(elem.tail, next.text)

    # Replace element with its children
    parent.remove(elem)
    for c in reversed(elem.getchildren()):
        parent.insert(index, c)


def empty_text(txt):
    """
    Returns True is the some text is considered empty
    """
    return txt is None or txt.strip() == ""
