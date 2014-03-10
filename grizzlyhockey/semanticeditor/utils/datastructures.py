"""
Use the 'struct' function (see below), or use the __metaclass__
attribute with class definition syntax.

>>> class Animal(object):
...    __metaclass__ = struct
...    name = ""
...    weight = 0
...    can_fly = False
>>> Animal(name="Pig")
<Animal can_fly=False name='Pig' weight=0>

Subclass to add more attributes or override
existing ones.  Multiple bases can be used.

>>> class Bird(Animal):
...    __metaclass__ = struct
...    can_fly = True
...    sings = None
>>> Bird(sings=True)
<Bird can_fly=True name='' sings=True weight=0>

You can subclass to add methods like this:

>>> class SelfDescribingBird(Bird):
...     def describe(self):
...         if self.sings:
...             print "I can sing"
>>> SelfDescribingBird(sings=True).describe()
I can sing

"""

from semanticeditor.utils.mixins import StandardReprMixin


def struct(name, bases, attrdict):
    """
    Returns a class that can be used as a simple struct, with default
    attributes defined in 'attrdict'.

    >>> Person = struct("Person", (), dict(age=0, name=""))
    >>> Person
    <class '__main__.Person'>
    >>> Person()
    <Person age=0 name=''>
    >>> Person(name="Joe")
    <Person age=0 name='Joe'>
    >>> Person(name="Fred", age=1)
    <Person age=1 name='Fred'>
    >>> Person(name="Fred", value=0, stupidity=1000)
    Traceback (most recent call last):
        ...
    TypeError: Person does not have attribute(s): stupidity, value

    >>> GenderedObject = struct("GenderedObject", (), dict(sex=None))

    If the default attribute is mutable, use a callable (e.g. a
    lambda, a class or a factory function) to provide it, otherwise it
    will be shared between instances.  Use the bases argument to
    inherit attribute definitions from other structs.

    >>> Parent = struct("Parent", (Person, GenderedObject), dict(children=list))
    >>> Parent(name="Fred", sex="male")
    <Parent age=0 children=[] name='Fred' sex='male'>
    """
    # In case '__metaclass__ = struct' is set directly, need these:
    attrdict.pop('__metaclass__', None)
    attrdict.pop('__module__', None)

    # Find allowed attributes of all bases
    attrs = {}
    for d in filter(lambda x: x is not None,
                    (getattr(b, '_allowed_attrs', None) for b in bases)):
        attrs.update(d)
    attrs.update(attrdict)

    def __init__(self, **kwargs):
        for k, v in attrs.items():
            try:
                val = kwargs.pop(k)
            except KeyError, e:
                val = v
                if callable(val):
                    val = val()
            setattr(self, k, val)
        if kwargs:
            raise TypeError("%s does not have attribute(s): %s" % \
                                (name, ", ".join(sorted(kwargs.keys()))))

    # we have no need for 'real' bases, and they only confuse things:
    bases = (StandardReprMixin,)
    return type(name, bases, {'__init__': __init__,
                              '_allowed_attrs': attrs})

# We could also define a 'Struct' class which has '__metaclass__ = StructBase
# Defining StructBase, however, is more tricky, and can't resuse
# the existing 'struct' function. (You end up needing to do:
#   s = struct(...)
#   s.__class__ = struct
# which does not work.)
# It also makes it harder to define normal subclasses that are just
# using the __init__ functionality provided by the 'struct' type.


def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
