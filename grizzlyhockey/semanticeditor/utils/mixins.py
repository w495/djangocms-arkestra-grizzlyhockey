# -*- coding: utf-8 -*-

class StandardReprMixin(object):
    u"""
    Used to add an implementation of '__repr__' that is generally 
    useful for debugging.

    >>> class Foo(StandardReprMixin):
    ...     def __init__(self):
    ...         self.name = "blé"
    >>>
    >>> f = Foo()
    >>> f.frobble = 1
    >>> print f
    <Foo frobble=1 name='bl\\xc3\\xa9'>
    """
    def __repr__(self):
        return u"<%s %s>" % (self.__class__.__name__,
                             u' '.join(u"%s=%r" % (k,v) for (k,v) in sorted(self.__dict__.iteritems())
                                       if k != '__doc__'))

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
