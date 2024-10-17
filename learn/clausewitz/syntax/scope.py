import typing as _typing
from tokenize import (
    TokenInfo as _TokenInfo,
)

from cached_property import cached_property
# from returns import (
#     returns as _returns, # this causes an error
# )
from typeguard import typechecked as _typechecked

from .element import (
    Element as _Element,
    Operator as _Operator,
    Modifier as _Modifier,
)
from ..datastructure import (
    Dict as _Dict,
)


class Scope(_Element):
    '''
    Attributes:
        SerializationError (Exception): the exception class for serialization errors
        
        _statements (list): list of _Statement objects
        
        _current_statement (_Statement): method property,  the current statement, either None or a _Statement object
        
    Methods:
        __init__: initialize the _statements and _current_statement as an empty list and None
        
        finish_statement: finish the current statement and set the current statement to None
        
        _as_list: return the value of the self.statement
        
        _as_dict: assert that the statement has at least 3 elements, the second element is an instance of _Operator, and the rest of the elements are instances of _Modifier
        
        _raw: yield the raw value of the statement
        
        value: a cached_property , return self._as_dict() or self._as_list() or raise a SerializationError using self._raw()
        
        push: perhaps the main parse, not understand
        
    
    '''
    class SerializationError(Exception):
        def __init__(self, data=None):
            '''
            pformat the data
            '''
            from pprint import pformat
            super().__init__(pformat(data))
            self.data = data

    def __init__(self):
        self._statements: _typing.List['_Statement'] = [] # _Statement is imported at the end of the file
        self._current_statement: _typing.Optional['_Statement'] = None

    '''
    if current_statement is None, create a new empty _Statement object and append it to the _statements list
    '''
    @property
    def current_statement(self) -> '_Statement':
        if self._current_statement is None:
            # Q what is the usage of an empty Statement object?
            self._current_statement = _Statement()
            self._statements.append(self._current_statement)
        return self._current_statement

    def finish_statement(self) -> None:
        '''
        finish the current statement and set the current statement to None
        '''
        if self._current_statement is not None:
            self._current_statement.finish_queue()
            self._current_statement = None
    
    # the return method did not exist
    # @_returns(list)
    # @_typechecked
    def _as_list(self):
        '''
        return the value of the self.statement
        '''
        for statement in self._statements:
            if len(statement) != 1:
                raise self.SerializationError
            yield statement[0].value
    #Q why use the yield as it has already been asserted to have only one element?

    # @_returns(_Dict)
    def _as_dict(self):
        '''
        assert that the statement has at least 3 elements, the second element is an instance of _Operator, and the rest of the elements are instances of _Modifier
        return key-value pairs of the statement
        '''
        for statement in self._statements:
            if len(statement) < 3:
                raise self.SerializationError
            op = statement[1]
            if not isinstance(op, _Operator):
                raise self.SerializationError
            if not all(
                    isinstance(element, _Modifier)
                    for element in statement[2:-1]
            ):
                raise self.SerializationError

            values = statement.values
            yield values[0], values[1:]
            
    
    # @_returns(tuple)
    def _raw(self):
        '''
        yield the raw value of the statement
        '''
        for statement in self._statements:
            yield statement.values

    '''
    a cached_property , return self._as_dict() or self._as_list() or raise a SerializationError using self._raw()
    '''
    @cached_property
    def value(self):
        try:
            return self._as_dict()
        except self.SerializationError:
            pass

        try:
            return self._as_list()
        except self.SerializationError:
            pass

        raise self.SerializationError(self._raw())

    def push(self, tokens: _typing.Iterable[_TokenInfo]):
        tokens = iter(tokens)

        try:
            for token in tokens:
                '''
                if the token is an instance of _Tokens.END_SCOPE and the length of self._statements is 0, return
                
                
                '''
                if token.exact_type in _Tokens.END_SCOPE and len(self._statements) == 0:
                    return

                try:
                    '''
                    statement.push:
                    4. push: 
                        4.1 try append _TokenInfo to the self._queue 
                        4.2 if exception: ShouldNotAppend
                            4.2.1 append the value and clear the queue
                            4.2.2 accoring to the exact_type of the token, append the token to the list, or raise the Invalide exception
                        4.3 if exception: EndStatement
                            4.3.1 call the _end function, and raise the End exception,
                            4.3.2 if the exact type of the token is in the END_SCOPE, End.reject_last is False, otherwise True

                    '''
                    self.current_statement.push(token)
                except _Statement.End as end:
                    self.finish_statement()
                    if end.reject_last:
                        self.current_statement.push(token)
                # Q what is the function of the except block?

                if token.exact_type in _Tokens.START_SCOPE:
                    scope: Scope = self.current_statement[-1]
                    scope.push(tokens)

                elif token.exact_type in _Tokens.END_SCOPE:
                    return

        finally:
            self.finish_statement()

'''
The `# noqa: E402` comment is used to tell linters like `flake8` to ignore the rule that requires imports to be at the top of the file. 

This is useful in situations where imports need to be delayed, for example, to avoid circular dependencies or to conditionally import modules.


'''

from .token import (  # noqa: E402
    Tokens as _Tokens,
)
from .statement import (  # noqa: E402
    Statement as _Statement,
)
