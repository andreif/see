"""
see
An alternative to dir(). Easy to type; easy to read. For humans only.

http://github.com/inky/see

    >>> from see import see
    >>> help(see)

Copyright (c) 2009 Liam Cooke

Licensed under the GNU General Public License v3.
See COPYING for the full license text.

"""
__author__ = 'Liam Cooke'
__version__ = '2009-02-16'
__copyright__ = 'Copyright (c) 2009 Liam Cooke'
__license__ = 'GNU General Public License v3'

import textwrap

def see(obj):
    """
    Inspect 'obj'. Like dir(obj), but easier on the eyes.

    Some symbols:

        ?       documentation is available using help(obj)
        .       may have dynamic attributes
        []      allows obj[key]
        for     allows iteration
        in      allows membership tests (e.g. x in obj)
        +@      unary positive operator (e.g. +2)
        -@      unary negative operator (e.g. -3)
    """

    # http://docs.python.org/reference/datamodel.html#specialnames
    symbols = (
        ('__call__', '()'),
        ('__getattr__', '.'),
        #('__setattr__', '.'),
        #('__delattr__', '.'),
        #('__getattribute__', '.'),
        ('__getitem__', '[]'),
        ('__setitem__', '[]'),
        ('__delitem__', '[]'),

        ('__iter__', 'for'),
        ('__contains__', 'in'),

        ('__add__', '+'),
        ('__iadd__', '+='),
        ('__sub__', '-'),
        ('__isub__', '-='),
        ('__mul__', '*'),
        ('__imul__', '*='),
        ('__div__', '/'),
        ('__truediv__', '/'),
        ('__floordiv__', '/'),
        ('__divmod__', '/'),
        ('__idiv__', '/='),
        ('__itruediv__', '/='),
        ('__ifloordiv__', '/='),
        ('__mod__', '%'),
        ('__divmod__', '%'),
        ('__imod__', '%='),
        ('__pow__', '**'),
        ('__ipow__', '**='),
        ('__lshift__', '<<'),
        ('__ilshift__', '<<='),
        ('__rshift__', '>>'),
        ('__irshift__', '>>='),
        ('__and__', '&'),
        ('__iand__', '&='),
        ('__xor__', '^'),
        ('__ixor__', '^='),
        ('__or__', '|'),
        ('__ior__', '|='),

        ('__pos__', '+@'),
        ('__neg__', '-@'),
        ('__invert__', '~'),
        ('__lt__', '<'),
        ('__le__', '<='),
        ('__eq__', '=='),
        ('__ne__', '!='),
        ('__gt__', '>'),
        ('__ge__', '>='),

        ('__abs__', 'abs()'),
        ('__nonzero__', 'bool()'),
        ('__complex__', 'complex()'),
        ('__float__', 'float()'),
        ('__hex__', 'hex()'),
        ('__int__', 'int()'),
        ('__len__', 'len()'),
        ('__long__', 'long()'),
        ('__oct__', 'oct()'),
        ('__unicode__', 'unicode()'),
    )
    attrs = dir(obj)
    actions = []
    name = lambda a: '.%s%s' % (a, callable(getattr(obj, a)) and '()' or '')

    try:
        if obj.__doc__.strip():
            actions.append('?')
    except AttributeError:
        pass
    for attr, symbol in symbols:
        if attr in attrs and symbol not in actions:
            actions.append(symbol)
    attrs = filter(lambda v: not v.startswith('_'), attrs)
    actions.extend(name(a) for a in attrs)
    print textwrap.fill('   '.join(actions), 78,
            initial_indent='  ', subsequent_indent='  ')
