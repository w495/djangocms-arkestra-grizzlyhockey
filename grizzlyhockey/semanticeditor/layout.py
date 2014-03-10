import re

from lxml import etree as ET

from semanticeditor.definitions import COMMANDS, SORTED_COMMANDS, NEWROW, NEWCOL, NEWINNERROW, NEWINNERCOL, TooManyColumns, BadStructure
from semanticeditor.common import get_classes_for_node, get_classes_from_presinfo
from semanticeditor.utils.etree import get_parent


### Layout details ###

# This is designed to be user supply-able if necessary

class LayoutDetailsBase(object):
    """
    Base class for strategy object used to define the details of
    CSS/HTML to be used when rendering a layout
    """
    # Inherit from this class if creating your own custom class.  LayoutDetails
    # provides a concrete implementation.

    def _raise_not_implemented(self):
        raise NotImplementedError()

    max_columns = property(_raise_not_implemented, doc="""Maximum number of columns to allow""")

    use_inner_column_div = property(_raise_not_implemented, doc="""True to wrap all column content in a inner div""")

    def row_classes(self, logical_column_count, actual_column_count):
        """
        Returns a list of CSS classes to be used for a row containing
        logical_column_count 'logical' columns, actual_column_count 'actual'
        columns.  'actual' columns are present in the HTML structure, but some
        might be, for example, double width, so are counted as two logical
        columns.
        """
        raise NotImplementedError()

    def column_classes(self, logical_column_num, actual_column_num, logical_column_count, actual_column_count):
        """
        Returns a list of CSS classes to be used for a column which is number
        column_num out of column_count.  (see above regarding logical/actual)
        """
        raise NotImplementedError()

    def is_row_class(self, class_):
        """
        Returns true if the class (a string) corresponds to a CSS class used for
        a row.
        """
        raise NotImplementedError

    def is_column_class(self, class_):
        """
        Returns true if the class (a string) corresponds to a CSS class used for
        a column.
        """
        raise NotImplementedError()

    def outer_column_classes(self, presinfo):
        """
        Given a list a PresentationInfo objects, return the ones that should be
        applied to the outer column div.
        """
        if not self.use_inner_column_div:
            return presinfo
        else:
            raise NotImplementedError()

    def inner_column_classes(self, presinfo):
        """
        Given a list a PresentationInfo objects, return the ones that should be
        applied to the inner column div.  (Never called if use_inner_column_div
        = False)
        """
        raise NotImplementedError()

    # Hacks, optional
    def format_pre_parse_hacks(self, html, styleinfo):
        """
        For formatting, applies hacks to unformatted HTML before parsing,
        returns HTML to be used.
        """
        return html

    def format_post_parse_hacks(self, tree, styleinfo):
        """
        For formatting, applies hacks to tree after parsing, returns new tree to
        be used.
        """
        return tree

    def format_structure_hacks(self, structure, styleinfo):
        """
        For formatting, given a list of StructureItems and a list of
        PresentationInfos, applies hacks and returns new structure to be used.
        """
        return structure

    def format_post_layout_hacks(self, tree, structure, styleinfo):
        """
        For formatting, given the tree after layout, the structure and style
        info, apply hacks and return a new tree.
        """
        return tree

    def extract_pre_parse_hacks(self, html):
        """
        For extracting presentation info, applies hacks to formatted HTML before
        parsing, and returns HTML to be used.
        """
        return html

    def extract_post_parse_hacks(self, tree):
        """
        For extracting presentation info, applies hacks to parse tree before
        after parsing, and returns tree.
        """
        return tree

    def extract_structure_hacks(self, structure):
        """
        For extracting presentation info, given a list of StructureItems,
        applies hacks and returns new structure to be used.
        """
        return structure

class LayoutDetails(LayoutDetailsBase):
    """
    Strategy object used for defining the details of CSS/HTML to be used when
    rendering a Layout.  This is a concrete implementation.
    """
    ROW_CLASS = "row"
    COLUMN_CLASS = "column"

    max_columns = 6

    use_inner_column_div = True

    def row_classes(self, logical_column_count, actual_column_count):
        retval = [self.ROW_CLASS]
        if actual_column_count > 1:
            retval.append("columns%d" % logical_column_count)
        return retval

    def column_classes(self, logical_column_num, actual_column_num, logical_column_count, actual_column_count):
        if actual_column_count == 1:
            # No classes
            return []
        retval = [self.COLUMN_CLASS]
        if actual_column_num == 1:
            retval.append("firstcolumn")
        if actual_column_num == actual_column_count:
            retval.append("lastcolumn")
        return retval

    def is_row_class(self, class_):
        return class_ == self.ROW_CLASS or re.match(r'^columns\d+$', class_)

    def is_column_class(self, class_):
        return class_ == self.COLUMN_CLASS or re.match(r'^(first|last)column$', class_)

    def outer_column_classes(self, presinfo):
        return [pi for pi in presinfo if pi.column_equiv is not None]

    def inner_column_classes(self, presinfo):
        return [pi for pi in presinfo if pi.column_equiv is None]

    # Hacks
    def format_post_layout_hacks(self, tree, structure, styleinfo):
        # WYMEditor cannot insert divs. This is a workaround
        for n in tree.getiterator():
            if n.tag == 'p' and ('div' in get_classes_for_node(n)):
                n.tag = 'div'
            if n.tag == 'p':
                # If only child element is a plugin object, convert to
                # a div.
                # NB: current implementation of plugin objects is that they
                # are represented by an image in the editor.  Our code has to
                # run before these are converted, so we have to work with this
                # implementation detail.
                children = n.getchildren()
                if ((n.text is None or n.text.strip() == "")
                    and len(children) == 1
                    and children[0].tag == "img"
                    and (children[0].tail is None or children[0].tail.strip() == "")
                    and children[0].attrib.get('id', '').startswith("plugin_obj")):
                        n.tag = 'div'
                        # Add 'div' to list of classes
                        # This handles the reverse transform for us:
                        n.attrib['class'] = ' '.join(n.attrib.get('class', '').split(' ') + ['div']).strip()
        return tree

    def extract_post_parse_hacks(self, tree):
        # inverse part of above workaround
        for n in tree.getiterator():
            if n.tag == 'div' and ('div' in get_classes_for_node(n)):
                n.tag = 'p'
        return tree


def get_layout_details_strategy():
    # TODO - make configurable
    return LayoutDetails()



### Creating layouts ###

# Simple wrapper for nodes to provide as_nodes() method.
class NodeContent(object):
    def __init__(self, node):
        self.node = node

    def as_nodes(self, layout_strategy):
        return [self.node]

# Simple container for whole layout.
class Layout(object):
    # True if the structure corresponding to this command allows content to be
    # embedded directly.
    accepts_content = True

    def __init__(self):
        self.content = []

# LayoutRow contains a list of columns, and a list of PresentationInfo objects
class LayoutRow(object):

    accepts_content = False

    def __init__(self, presinfo=None):
        if presinfo is None:
            presinfo = []
        self.content = []
        self.presinfo = presinfo

    def column_count(self):
        """
        Get the number of logical columns.
        """
        return sum(_layout_column_width(c) for c in self.content)

    def as_nodes(self, layout_strategy):
        """
        Returns layout as a list of ElementTree nodes
        """
        # Row
        logical_column_count = self.column_count()
        actual_column_count = len(self.content)
        rowdiv = ET.Element('div')
        classes = layout_strategy.row_classes(logical_column_count, actual_column_count) + get_classes_from_presinfo(self.presinfo)
        if classes:
            rowdiv.set('class', ' '.join(classes))

        # Columns
        logical_column_num = 1
        for i, col in  enumerate(self.content):
            coldiv = ET.Element('div')
            classes = layout_strategy.column_classes(logical_column_num,
                                                     i + 1,
                                                     logical_column_count,
                                                     actual_column_count) + \
                    get_classes_from_presinfo(layout_strategy.outer_column_classes(col.presinfo))
            if classes:
                coldiv.set('class', ' '.join(classes))
            if layout_strategy.use_inner_column_div:
                contentdiv = ET.Element('div')
                coldiv.append(contentdiv)
                inner_classes = get_classes_from_presinfo(layout_strategy.inner_column_classes(col.presinfo))
                if inner_classes:
                    contentdiv.set('class', ' '.join(inner_classes))
            else:
                contentdiv = coldiv
            for n in col.content:
                contentdiv.extend(n.as_nodes(layout_strategy))
            rowdiv.append(coldiv)

            logical_column_num += _layout_column_width(col)
        return [rowdiv]

# LayoutColumn contains a list of content, and a list of PresentationInfo objects.
class LayoutColumn(object):

    accepts_content = True

    def __init__(self, presinfo=None):
        if presinfo is None:
            presinfo = []
        self.content = []
        self.presinfo = presinfo


### Structures for commands ###

LAYOUT_STRUCTURES = {
    NEWROW: LayoutRow,
    NEWCOL: LayoutColumn,
    NEWINNERROW: LayoutRow,
    NEWINNERCOL: LayoutColumn,
}


def _layout_column_width(col):
    """
    Returns the logical column width of a column
    """
    column_equivs = [pi.column_equiv for pi in col.presinfo if pi.column_equiv is not None]
    if len(column_equivs) > 0:
        # assume user has not done something silly like put
        # *2* column_equiv classes on a column
        return column_equivs[0]
    else:
        return 1

def _find_layout_commands(root, structure, styleinfo):
    # Layout commands are not stored against normal sections,
    # but have their own entry in the section list, using an id
    # of 'newrow_' or 'newcol_' + id of block they precede.

    sect_dict = dict((s.sect_id, s) for s in structure)
    command_info = {}
    for c in COMMANDS:
        # for each command, store a dictionary that is
        # key = sect_id, val = [PresentationInfo]
        command_info[c.name] = {}

    for sect_id, presinfo in styleinfo.items():
        for c in COMMANDS:
            if sect_id.startswith(c.prefix):
                real_sect_id = sect_id[len(c.prefix):]
                sect = sect_dict.get(real_sect_id)
                if sect is not None:
                    parent = get_parent(root, sect.node)
                    if not _is_root(parent):
                        raise BadStructure("Section \"%(name)s\" is not at the top level of the"
                                           " document, and therefore cannot have a column"
                                           " structure applied to it.  Please move the"
                                           " '%(commandname)s' command to a top level element." %
                                           dict(name=sect.name,
                                                commandname=c.name))

                command_info[c.name][real_sect_id] = presinfo

    return command_info

def create_layout(root, styleinfo, structure):
    # Find the layout commands
    command_info = _find_layout_commands(root, structure, styleinfo)

    # Build a Layout structure.
    layout = Layout()

    # Get nodes
    nodes = root.getchildren()
    if nodes and nodes[0].tag == 'body':
        nodes = nodes[0].getchildren()

    sect_dict = dict((si.node, si) for si in structure)

    # Now build a layout. At each point, we need to:
    # - append nodes to current container
    # - keep track of all containers, so we can respond to new row/column commands.

    containers = [layout]
    current_level = -1

    for node in nodes:
        si = sect_dict.get(node)
        if si:
            for command in SORTED_COMMANDS:
                presinfo = command_info[command.name].get(si.sect_id)
                if presinfo is not None:
                    # We have the command.

                    # First, need to work out what level it is on:
                    command_level = command.layout_order

                    if command_level > current_level + 1:
                        lowercommand = SORTED_COMMANDS[command_level-1]
                        raise BadStructure('Section "%(sect)s" has command "%(command)s" '
                                           'but there needs to be a "%(lowercommand)s" '
                                           'command first.' %
                                           dict(sect=si.name,
                                                command=command.verbose_name,
                                                lowercommand=lowercommand.verbose_name)
                                           )

                    if command_level <= current_level:
                        # Need to pop of list of containers so that the next
                        # container goes on the right parent.

                        # Pop as many containers as necessary
                        for i in xrange(current_level - command_level + 1):
                            containers.pop()

                    # Make new container
                    layout_container = LAYOUT_STRUCTURES[command](presinfo=presinfo)
                    containers[-1].content.append(layout_container)
                    containers.append(layout_container)

                    current_level = command_level

        # Deal with the nodes

        # Check whether we can add them here.
        if not containers[-1].accepts_content:
            # can't append content to this. We infer the presence of the next
            # structure down.
            current_level += 1
            next_command = SORTED_COMMANDS[current_level]
            layout_container = LAYOUT_STRUCTURES[next_command]()
            # Currently this will always produce a command that accepts content
            assert layout_container.accepts_content
            containers[-1].content.append(layout_container)
            containers.append(layout_container)

        # Add the content nodes.
        containers[-1].content.append(NodeContent(node))

    # Need to remove empty layout structures.
    _trim_empty_layout(layout)

    return layout

def _trim_empty_layout(layout):
    for i, l in reversed(list(enumerate(layout.content))):
        if hasattr(l, 'content'):
            if not l.content:
                # l has nothing, so remove from parent.
                layout.content[i:i+1] = []
            else:
                _trim_empty_layout(l)

def check_layout(row, structure, layout_strategy, sect_dict=None):
    if sect_dict is None:
        sect_dict = dict((si.node, si) for si in structure)
    max_cols = layout_strategy.max_columns

    # Cope with NodeContent:
    if not hasattr(row, 'content'):
        return

    if row.column_count() > max_cols:
        # Because columns can be multiple width, we can't easily work out
        # which column needs to be moved, so just refer user to whole
        # section.

        nodes = row.content[0].content[0].as_nodes(layout_strategy)
        while True:
            # nodes[0] might be a div created for layout.  If so, it won't
            # be in sect_dict. But one of its children will be.
            sect = sect_dict.get(nodes[0], None)
            if sect is not None:
                break
            else:
                nodes = nodes[0]

        raise TooManyColumns("The maximum number of columns is %(max)d. "
                             "Please adjust columns in section '%(name)s'." %
                             dict(max=max_cols, name=sect.name))

    for col in row.content:
        # Check nested layouts.
        for content in col.content:
            check_layout(content, structure, layout_strategy, sect_dict=sect_dict)


def _is_root(node):
    return node.tag == 'html' or node.tag == 'body'



