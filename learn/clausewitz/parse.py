import tokenize as _tokenize  # Import the tokenize module with an alias to avoid naming conflicts.
import typing as _typing  # Import the typing module with an alias for type hinting purposes.
from tokenize import (
    TokenInfo as _TokenInfo,  # Import TokenInfo class for type hinting token objects.
)
import json

from clausewitz.syntax.scope import (
    Scope as _Scope,  # Import Scope class from a custom module, likely used elsewhere in the project.
)

class ErrorToken(Exception):
    pass  # Custom exception to indicate an error with a token.

class Unfinished(Exception):
    pass  # Custom exception to indicate unfinished parsing or processing.


def filter_tokens(tokens: _typing.Iterable[_TokenInfo]) -> _typing.Iterator[_TokenInfo]:
    """
    Filters out unipmortant tokens from the given iterable of tokens. Raise an error if an error token is encountered.

    Args:
        tokens: An iterable of TokenInfo objects to be filtered.

    Returns:
        An iterator over TokenInfo objects, excluding the filtered types.
    """
    for token in tokens:
        if token.type in (
                _tokenize.ENCODING,  # Exclude tokens representing file encoding.
                _tokenize.NEWLINE,  # Exclude tokens representing new lines.
                _tokenize.NL,  # Exclude tokens representing non-significant new lines (e.g., within a string).
                _tokenize.COMMENT,  # Exclude tokens representing comments.
                _tokenize.INDENT,  # Exclude tokens representing indentation increases.
                _tokenize.DEDENT,  # Exclude tokens representing indentation decreases.
                _tokenize.ENDMARKER,
        ):
                continue
            
        if token.type == _tokenize.ERRORTOKEN:
            raise ErrorToken  # Raise an error if an error token is encountered.

        yield token  # Yield the token if it is not excluded. the yjk

def parse(tokens: _typing.Iterable[_TokenInfo]):
    '''
    Filter the tokens using a function `filter_tokens`. 
    
    '''
    tokens = filter_tokens(tokens)
    
    # Create an instance of `_Scope`. This object might be used to manage
    # the current parsing scope, holding context or results as parsing progresses.
    scope = _Scope()
    
    # Push the filtered tokens into the scope. This could mean that the scope
    # is being prepared to process or hold these tokens in some way.
    scope.push(tokens) # only one token is pushed into the scope, as the tokens is the result of a generator

    try:
        # Attempt to get the next token from the iterable. This serves as a check
        # to ensure there are tokens to process. If there are no tokens (i.e., the
        # tokens iterable is empty), a `StopIteration` exception will be raised.
        next(tokens)
    except StopIteration:
        # If a `StopIteration` exception is caught, it means there were no tokens
        # to process. The function simply passes in this case, likely indicating
        # that an empty input is considered valid and does not interrupt the parsing
        # process.
        pass
    else:
        # If the `try` block does not raise an exception, it means there was at least
        # one token to process, but since no further processing happens after this
        # `next(tokens)` call, it implies that there are unprocessed tokens left.
        # Therefore, an `Unfinished` exception is raised to indicate that the parsing
        # is incomplete or the input was not fully consumed.
        raise Unfinished

    # Return the value of the current scope. This value is the result of the parsing
    # process, which could be an abstract syntax tree, a configuration object, or any
    # other structured representation of the input tokens.
    return scope.value


def parse_cmd(args=None):  # pragma: no cover
    # Import necessary modules
    import sys
    import argparse  # For parsing command line arguments
    import json  # For outputting the parsed data in JSON format
    from tokenize import tokenize  # For tokenizing the input file
    from clausewitz.util.tokenize import prepare  # Custom preparation function for tokenization

    # Create a parser for command line arguments
    parser = argparse.ArgumentParser()
    # Add an argument for the input file. This is a positional argument.
    parser.add_argument('input')
    # Add an optional argument to pretty-print the JSON output
    # action='store_true': This tells argparse to store the boolean value True if the associated command-line argument is present, and False otherwise (which is the default if the argument is not included). This eliminates the need for the user to explicitly specify a value (True or False) for the argument; the presence of the argument itself acts as a True value.
    parser.add_argument('--pretty', action='store_true')
    # Parse the command line arguments
    args = parser.parse_args(args)

    # Open the input file in binary mode for reading
    # 'rb' is a mode specifier that stands for "read binary". When a file is opened using 'rb', it is opened in binary mode. This means that the file is read as a sequence of bytes and no encoding or decoding is performed. This mode is commonly used when working with non-text files or when the file content is not expected to be human-readable text.
    with open(args.input, 'rb') as f:
        # 
        # Prepare the readline function for tokenization
        readline = prepare(f.readline)
        # Tokenize the input file
        tokens = tokenize(readline)
        # Parse the tokens to get the structured data
        value = parse(tokens)

    # Check if the pretty-print option was used
    if args.pretty:
        # If so, set JSON dump options for pretty printing
        kwargs = {
            'indent': 4,
        }
    else:
        # Otherwise, set JSON dump options for compact printing
        kwargs = {
            'separators': (',', ':'),
        }

    # Dump the parsed data as JSON to stdout, using the specified options
    # sys.stdout in Python refers to the standard output stream. When you use sys.stdout as an argument in functions like json.dump(), it directs the output of the function to the standard output, which is typically the console or terminal from which the Python script is run. This allows the script to print the output directly to the console instead of writing it to a file or another output stream.
    # so using a sys.stdout in json.dump() will print the output to the console rather than writing it to a json file.
    json.dump(value, sys.stdout, **kwargs)
