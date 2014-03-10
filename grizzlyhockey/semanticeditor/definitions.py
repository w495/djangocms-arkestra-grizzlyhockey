"""
Definitions used for HTML manipulation
"""

### Errors ###

class IncorrectHeadings(ValueError):
    pass

class BadStructure(ValueError):
    pass

class TooManyColumns(BadStructure):
    pass

AllUserErrors = (IncorrectHeadings, BadStructure, TooManyColumns)


### Definitions ###

_TECHNICAL_BLOCKDEF = set(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ol', 'ul', 'blockquote']) # according to HTML4
_ADDITIONAL_BLOCKDEF = set(['li']) # li really act like block elements
BLOCKDEF = _TECHNICAL_BLOCKDEF | _ADDITIONAL_BLOCKDEF
BLOCKDEF_SELECTOR = ",".join(BLOCKDEF) # need to sync with wymeditor.semantic.js
HEADINGDEF = set(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
PREVIEW_BLOCKDEF = _TECHNICAL_BLOCKDEF

# The number of chars we trim block level elements to.
BLOCK_LEVEL_TRIM_LENGTH = 200

### Presentation information ###

class PresentationInfo(object):
    """
    Encapsulates a piece of presentation information.
    """
    def __init__(self, prestype=None, name=None, verbose_name="", description="", allowed_elements=None, column_equiv=None):
        self.prestype = prestype
        self.name = name
        # verbose_name, description and allowed_elements are additional pieces
        # of information that are only needed when the client is requesting a
        # list of styles.  In other situations these objects may not have these
        # attributes filled in.
        self.verbose_name = verbose_name
        self.description = description
        if allowed_elements is None:
            allowed_elements = []
        self.allowed_elements = allowed_elements
        self.column_equiv = column_equiv

    def __eq__(self, other):
        return self.prestype == other.prestype and self.name == other.name

    def __hash__(self):
        return hash(self.prestype) ^ hash(self.name)

    def __repr__(self):
        return "PresentationInfo(prestype=\"%s\", name=\"%s\")" % (self.prestype, self.name)


class PresentationClass(PresentationInfo):
    """
    A PresentationInfo representing a CSS class applied to a section.
    """
    def __init__(self, name, verbose_name="", description="",
                 allowed_elements=None, column_equiv=None,
                 category=None):
        super(PresentationClass, self).__init__(prestype="class",
                                                name=name,
                                                verbose_name=verbose_name,
                                                description=description,
                                                allowed_elements=allowed_elements,
                                                column_equiv=column_equiv)
        self.category = category


class PresentationCommand(PresentationInfo):
    """
    A PresentationInfo representing a command applied to a section
    """
    def __init__(self, name, layout_order, verbose_name="", description=""):
        super(PresentationCommand, self).__init__(prestype="command",
                                                  name=name,
                                                  verbose_name=verbose_name,
                                                  description=description,
                                                  allowed_elements=sorted(list(_TECHNICAL_BLOCKDEF)))
        # The order that the command must appear in the document e.g. NEWROW
        # appears before NEWCOL.  (If there isn't a simple ordering on these
        # commands, the logic in _create_layout may need to be re-thought)
        self.layout_order = layout_order


    @property
    def prefix(self):
        """
        This is a prefix used to generate a name used for registering this
        command against a section and storing other presentation info.
        """
        # If there is, for example, a section 'h1_1' in the document, this
        # prefix is used to generate e.g. newrow_h1_1. The presence of the
        # name 'newrow_h1_1' says that a 'newrow' command was used against
        # h1_1, and it also allows PresentationClass objects to be stored
        # against newrow_h1_1 itself, which represents the entire row.

        return self.name + "_"


### DEFINITONS OF COMMANDS ###

NEWROW = PresentationCommand('newrow',
                             0,
                             verbose_name="new row",
                             description="""
<p>Use this command to start a new row.</p>

<p>This must be used in conjunction with 'New column'
to create a column layout.</p>

<p>If you wish to stop an existing column layout for a section, then you will
need to apply a 'New row' command to that section, creating a row with
just one column in it.</p>

""")

NEWCOL = PresentationCommand('newcol',
                             1,
                             verbose_name="new column",
                             description="""
<p>Use this command to start a new column, after a 'New row'
command has been used to start a set of columns.</p>

""")

NEWINNERROW = PresentationCommand('innerrow',
                                  2,
                                  verbose_name="inner row",
                                  description="""
<p>Use this command to start a nested, inner row within an existing column
structure.</p>

<p>This must be used in conjunction with 'Inner column'
to create a column layout.</p>

""")


NEWINNERCOL = PresentationCommand('innercol',
                                  3,
                                  verbose_name="inner column",
                                  description="""
<p>Use this command to start a new inner column, after an 'Inner row' command
has been used to start a set of nested columns.</p>

""")

COMMANDS = [NEWROW, NEWCOL, NEWINNERROW, NEWINNERCOL]

SORTED_COMMANDS = sorted(COMMANDS, key=lambda c: c.layout_order)

for i, c in enumerate(SORTED_COMMANDS):
    # Several places that index SORTED_COMMANDS make this assumption:
    assert c.layout_order == i
