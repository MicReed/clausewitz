def prepare(readline):
    """
    Prepare for Python's `tokenize`.
    Replace quotes with triple quotes to support multiline strings.
    """

    def _readline():
        '''
        the function of _readline is to read a line from the input file and replace the quotes with triple quotes to support multiline strings, while remaining the escaped quotes as they are.
        e.g example = r'"She said, \"Hello, world!\""' will be converted to example = b'"""She said, \\"Hello, world!\\""""'
        
        learn:the difference between byte and raw byte
        '''
        # in the usage in parse.py, the readline is the readline method of a file object 
        line = readline()
        # don't replace \", only "
        return line.replace(
            rb'\"', b"'''''",  # Pretend that there will never be ''''' in the text
        # This step is likely aimed at preparing the string for a context where triple double quotes are used for string delimiters, such as multiline strings in Python.
        ).replace(
            b'"', b'"""',
        ).replace(
            b"'''''", rb'\"',
        )

    return _readline


def prepare_cmd(args=None):  # pragma: no cover
    import sys
    import argparse
    parser = argparse.ArgumentParser()
    # The nargs parameter specifies the number of command-line arguments that should be consumed by the argument.
    # nargs='?' means that the command-line argument is optional. This configuration allows zero or 1 or more lines to be provided for the defined command-line parameter ('filename' in this case).
    parser.add_argument(
        'filename', nargs='?',
    )
    args = parser.parse_args(args)
    # print(type(args)) # <class 'argparse.Namespace'>
    f = None

    try:
        if args.filename is None:
            # use stdout
            # Python automatically decodes the binary data from stdin into strings using a default or specified encoding. This is suitable for text-based input.
            # the sys.stdin.buffer is used to read binary data from the standard input stream.
            readline = sys.stdin.buffer.readline
        else:
            f = open(args.filename, 'rb')
            readline = f.readline

        readline = prepare(readline) # the _reline function not executed here, but the function itself is returned to be used in the tokenize function

        while True:
            line = readline()
            if not line:
                break
            sys.stdout.buffer.write(line)
            # output the contents in the buffer without reaching the threshold
            sys.stdout.buffer.flush()

    finally:
        if f is not None:
            f.close()
