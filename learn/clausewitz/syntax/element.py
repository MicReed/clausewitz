import abc as _abc
import os

# from cached_property import cached_property

# double dot indicates the parent directory of the current module's package
'''
The double dot (..) in the import statement from ..util.strings import unescape as _unescape is used for relative importing in Python. It indicates that the module to be imported is in the parent directory of the current module's package.

Here's a breakdown of how it works:

A single dot (.) would refer to the current package.
A double dot (..) moves one level up in the package hierarchy, referring to the parent package.
Similarly, triple dots (...) would move two levels up, and so on.
'''
print("Current working directory:", os.getcwd())

from ..util.strings import (
    unescape as _unescape,
)


class Element(_abc.ABC):
    """
    funciton of Element:
    '''
    Element is an ABC class, so that all its subclasses must implement the value property before an instance of that subclass can be created.
    and the value property should be rewrite by the subclass, or it will raise a NotImplementedError. As the value property is an abstract property.
    
    '''
    
    ABC: Abstract Base Class, cannot be instantiated.
    
    value: abstract property
    The value property is decorated with @property and @_abc.abstractmethod, making it an abstract property. This means any subclass of Element must override and provide an implementation for this property.
    
    abstract method in ABC:
    According to the rules of ABCs in Python, any class that inherits from an ABC must implement all of its abstract methods and properties before an instance of that class can be created. 
    """
    @property
    @_abc.abstractmethod
    def value(self):
        ## The [# pragma: no cover] comment is used in Python code to tell coverage tools to ignore the line or block of code immediately following the comment for the purposes of coverage reporting. Coverage tools are used to measure how much of your code is covered by tests
        #Q what is a coverage tool?
        raise NotImplementedError  # pragma: no cover

    #Q what's the usage of this method?similar to q equal function, but the value is raising a NotImplementedError
    def __eq__(self, other):
        return self.value == other


class Name(Element):
    """
    A class to represent a name element.

    Attributes
    ----------
    raw : str
        The raw string representation of the name.

    Methods
    -------
    value as property:
        Returns the raw string representation of the name.
    """
    
    def __init__(self, raw: str):
        self._raw = raw

    @property
    def value(self):
        return self._raw


class Number(Element):
    """

    Args:
        neg (bool): the sign of the number
        raw (str): the raw string of the number
    
    Attributes:
        raw_string (str): the raw string representation of the number
        value (int or float): the value of the number
    
    """
    def __init__(self, neg: bool, raw: str):
        self._neg = neg
        self._raw = raw

    # determine the potive/negtive, if it's negative, add a '-' before the raw string
    @property
    def raw_string(self) -> str:
        return ('-' if self._neg else '') + self._raw

    # determine the type of value, int of float accorinding to the raw string
    @cached_property
    def value(self):
        s = self.raw_string
        if '.' in s:
            return float(s)
        else:
            return int(s)


class String(Element):
    def __init__(self, raw: str):
        self._raw = raw

    @property
    def raw_string(self) -> str:
        return self._raw

    '''
    The cached_property decorator in Python is used to create a property whose value is cached after the first access. 
    This means that the method under @cached_property will only be executed once, and its return value will be stored. 
    Subsequent accesses to this property will return the stored value instead of recalculating it. This is useful for properties that are expensive to compute and whose value does not change over the lifetime of the object.
    
    the unescape function is an self defined function used to turn "\\" to "\" in a string, 
    '''
    @cached_property
    def value(self):
        # Q why [2:-2]?
        return _unescape(self.raw_string[2:-2])


class Operator(Element):
    '''
    use to reserve the exact type and raw string of the operator
    attrobutes:
    _exact_type: int
    _raw: str
    value: method property, return _raw string 
    '''
    def __init__(self, exact_type: int, raw: str):
        self._exact_type = exact_type
        self._raw = raw

    @property
    def value(self):
        return self._raw


class Modifier(Element):
    # Q what is modifiers?
    # maybe : 'rgb' (Red, Green, Blue) and 'hsv' (Hue, Saturation, Value)
    MODIFIERS = (
        'rgb',
        'hsv',
    )

    def __init__(self, raw: str):
        self._raw = raw

    @property
    def value(self):
        return self._raw
