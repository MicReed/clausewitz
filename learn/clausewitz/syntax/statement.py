import typing as _typing
from tokenize import (
    TokenInfo as _TokenInfo,
)
from typing import Optional
'''
Optional is a type hint from the typing module in Python. It is used to indicate that a variable or return value of a function can be of a specified type or None. 
Essentially, Optional[X] is a shorthand for Union[X, None], meaning that the use of Optional explicitly allows the possibility of a None value.



'''

from .element import (
    Element as _Element,
    String as _String,
    Operator as _Operator,
    Modifier as _Modifier,
)


class Statement(_typing.List[_Element]):
    """
    Attributes:
        1. _queue: _Tokens, instance of self as _Tokens
        2. End: Exception
        3. Invalid: Exception
        4. accepts_value: method property, accept the value if the length of the list is 0 or the last element is an operator or a modifier
        5. values: return the value of the element in the list
        
    Methods:
        1. _raise: raise exception according to the token value
        2. finish_queue: get the value from the self._queue and append it to the list of self. and then clear the self._queue
        3. _end: call the finish_queue and raise the End exception
        4. push: 
            4.1 try append _TokenInfo to the self._queue 
            4.2 if exception: ShouldNotAppend
                4.2.1 append the value and clear the queue
                4.2.2 accoring to the exact_type of the token, append the token to the list, or raise the Invalide exception
            4.3 if exception: EndStatement
                4.3.1 call the _end function, and raise the End exception,
                4.3.2 if the exact type of the token is in the END_SCOPE, End.reject_last is False, otherwise True
    """
    class End(Exception):
        def __init__(self, reject_last: bool):
            self.reject_last = reject_last
        '''
        #Q what is usage of reject_last?
        #A End is intended to be used as an exception that can be raised during the execution of a program to indicate a specific error condition.
        #e.g 
        
        try:
            raise TestStatement.End(reject_last=True)
        except TestStatement.End as e:
            print(f"Caught an End exception with reject_last={e.reject_last}")
        '''

    class Invalid(Exception):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #N the _Tokens is a subclass of list, and store the TokenInfo
        self._queue: _Tokens = _Tokens(self)
        '''
        the super class is list, so the self is a list
        
        
        '''
        #Q what is the function of Token
        
    def _raise(self, token: Optional[_TokenInfo] = None):
        '''
        raise exception according to the token value
        '''
        if token is not None:
            raise self.Invalid(self, self._queue, token)
        else:
            raise self.Invalid(self, self._queue)
        # Q what is the function of _raise?

    def finish_queue(self):
        '''
        get the value from the self._queue and append it to the list of self. and then clear the self._queue
        '''
        if self._queue:
            self.append(self._queue.value)
            self._queue.clear()

        #Q what is the function of finish_queue?, what is self._queue.value?
        #A self_queue.value is the value of the Element Object in the Tokens class, and the function of finish_queue is to append the value to the list of self and clear the self._queue
            
    def _end(self, *, reject_last: bool):
        '''
        call the finish_queue and raise the End exception
        '''
        self.finish_queue()
        raise self.End(reject_last)
        # Q what is the function of _end?

    @property
    def accepts_value(self) -> bool:
        '''
        accept the value if the the list is empty or the last element is an operator or a modifier
        
        as the self is a list, so the self[-1] is the last element of the list
        and len(self) is the length of the list
        '''
        return len(self) == 0 or \
               isinstance(self[-1], _Operator) or \
               isinstance(self[-1], _Modifier)
        #Q what is the function of accepts_value?

    def push(self, token: _TokenInfo) -> None:
        try:
            self._queue.append(token)

        except self._queue.ShouldNotAppend:
            '''
            if exception: ShouldNotAppend:
            1. append the value and clear the queue
            2. accoring to the exact_type of the token, append the token to the list, or raise the Invalide exception
            '''
            self.finish_queue()

            if token.exact_type in _Tokens.OPERATORS:
                self.append(_Operator(token.exact_type, token.string))
            # PQ Scope
            elif token.exact_type in _Tokens.START_SCOPE:
                self.append(_Scope())
            elif token.exact_type in _Tokens.STRING_TYPES:
                self.append(_String(token.string))
            else:
                self._raise(token)

        except self._queue.EndStatement:
            '''
            call the _end function, and raise the End exception,
            if the exact type of the token is in the END_SCOPE, End.reject_last is False, otherwise True
            '''
            if token.exact_type in _Tokens.END_SCOPE:
                return self._end(reject_last=False)
            else:
                return self._end(reject_last=True)
            # Q what is the meaning of the reject_last?

    @property
    def values(self) -> _typing.List:
        '''
        as the self is a list of type Token, so the value of the element is the value of the element
        '''

        return [
            element.value
            for element in self
        ]
        # what is the value of a token
    

from .token import (  # noqa: E402
    Tokens as _Tokens,
)
from .scope import (  # noqa: E402
    Scope as _Scope,
)
