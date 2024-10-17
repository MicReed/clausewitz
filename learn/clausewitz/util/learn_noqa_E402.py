import tokenize as _tokenize
import typing as _typing
from tokenize import (
    TokenInfo as _TokenInfo,
)
##  noqa is a comment directive commonly used in Python code to tell linters and other code analysis tools to ignore a specific line for quality checks or warnings. The acronym "noqa" stands for "No Quality Assurance"

# noqa: E402 is used to tell the linter to ignore the E402 error on this line. E402 error typically means "module level import not at top of file", which is a violation of PEP 8 style guide.



class Tokens(_typing.List[_TokenInfo]):
    def __init__(self, parent: '_Statement'):
        super().__init__()
        self._parent = parent
        
        
from learn.clausewitz.syntax.statement import (  # noqa: E402
    Statement as _Statement,
)