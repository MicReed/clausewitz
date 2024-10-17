import tokenize as _tokenize
import typing as _typing
from tokenize import (
    TokenInfo as _TokenInfo,
)

from .element import (
    # PQ element.py
    Element as _Element,
    Number as _Number,
    Name as _Name,
    Modifier as _Modifier,
)


class Tokens(_typing.List[_TokenInfo]):
    '''
    1. a list to store the TokenInfo object
    2. the val is classified to be _Element object, among _Modifier, _Number, _Name
    3. filter certain cases and raise errors in the append function, if no error, append the token to the list
    
    
    e.g of TokenInfo class instance
    token = TokenInfo(type=STRING, string='"Hello, World!"', start=(1, 0), end=(1, 15), line='"Hello, World!"')
    
    
    '''
    START_SCOPE = (
        _tokenize.LBRACE, # LBRACE the value of this is 25
    )
    END_SCOPE = (
        _tokenize.RBRACE, # RBRACE the value of this is 26
    )

    OPERATORS = (
        _tokenize.EQUAL,
        _tokenize.LESS,
        _tokenize.LESSEQUAL,
        _tokenize.GREATER,
        _tokenize.GREATEREQUAL,
    )

    STRING_TYPES = (
        _tokenize.STRING, # STRING the value of this is complicated
    )

    @property
    # PQ _Modifier
    def modifier(self) -> _typing.Optional['_Modifier']:
        '''
        filer the contents in Tokens, and return the _Modifier object
        1. number of token should be 1
        2. the type of the token should be _tokenize.NAME
        3. the string value of the token should be in the _Modifier.MODIFIERS, rbg, or hsv
        '''
        if not self:
            return None

        if len(self) != 1:
            return None

        token = self[0]
        #N token is of type TokenInfo, the Tokeninfo.type is the str that represent the type of the tokenize module. 
        # here if the token.type is not equal _tokenize.NAME type, then return None
        if token.type != _tokenize.NAME: 
            #N e.g. name_token = TokenInfo(type=NAME, string='variableName', start=(2, 0), end=(2, 12), line='variableName = 42')
            #name_token.type == NAME
            return None

        #N PQ _Modifier.MODIFIERS
        if token.string not in _Modifier.MODIFIERS: #N rgb, hsv
            return None

        return _Modifier(token.string)

    @property
    def number(self) -> _typing.Optional['_Number']:
        '''
        filter the contents in Tokens, and return the _Number object
        1. the length of the token should be 1 or 2
        2. if the length is 1, the type of the token should be _tokenize.NUMBER
        3. if the length is 2, the first token should be _tokenize.MINUS and the second token should be _tokenize.NUMBER
        4. length 1 represents the positive number, length 2 represents the negative number
        '''
        if not self:
            return None

        elif len(self) == 1:
            if self[0].type != _tokenize.NUMBER:
                return None
            # PQ _Number
            return _Number(False, self[0].string)

        elif len(self) == 2:
            if not (self[0].exact_type == _tokenize.MINUS and
                    self[1].type == _tokenize.NUMBER):
                return None
            # PQ _Number
            return _Number(True, self[1].string)

        else:
            return None

    @property
    # PQ _Name
    def name(self) -> '_Name':
        '''
        join the string of the token in self
        '''
        return _Name(''.join(
            token.string
            for token in self
        ))

    class ShouldNotAppend(Exception):
        pass

    class EndStatement(Exception):
        pass

    #N PQ _Statement 
    def __init__(self, parent: '_Statement'):
        super().__init__()
        self._parent = parent

    #Q dont' understand this
    def _modifier_or_end_statement(self):
        #N should not append the value if the tokeninfo in contents is modifier like 
        if self.modifier is not None:
            raise self.ShouldNotAppend
        else:
            raise self.EndStatement

    def append(self, token: _TokenInfo):
        if token.exact_type in self.OPERATORS: # exact_type is the type of the token, to specify the exact type of the token_type, e.g. 14 for + type in OP
            raise self.ShouldNotAppend

        if token.exact_type in self.END_SCOPE:
            raise self.EndStatement

        if token.exact_type in (
                *self.START_SCOPE,
                *self.STRING_TYPES,
        ):
            if self:
                '''
                if token.exactype is [, or STRING, 
                and tokeninfo is not empty,
                raise _modifier_or_end_statement
                '''
                return self._modifier_or_end_statement()
            #Q when will self be useful?

            else:
                #N raise other exceptions
                #Q PQ _Statement.accepts_value
                if self._parent.accepts_value:
                    raise self.ShouldNotAppend
                else:
                    raise self.EndStatement

        if self:
            # self is [TokenInfo]
            # TokenInfo.end is the end position of the store value, e.g. value[-1].end = (1, 2), 1 is the line number, 2 is the column number
            # token.start is the start position of the new token
            # if value is not followed by the token,  then raise _modifier_or_end_statement
            if self[-1].end != token.start:
                return self._modifier_or_end_statement()
            #Q what is the usage of this if block?

        else:
            # for the parent list, if the length the list is 0 nor the last element is an operator or a modifier, raise a EndStatement exception
            if not self._parent.accepts_value:
                raise self.EndStatement
            #Q PQ _Statement.accepts_value

        super().append(token)

    @property
    #N filter the type of the tokeninfo in the list, and return relevant _Element object
    def value(self) -> '_Element':
        return self.modifier or self.number or self.name


from .statement import (  # noqa: E402
    Statement as _Statement,
)
