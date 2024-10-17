import io
def prepare(readline):
    """
    Prepare for Python's `tokenize`.
    Replace quotes with triple quotes to support multiline strings.
    """

    def _readline():
        '''
        the function of _readline is to read a line from the input file and replace the quotes with triple quotes to support multiline strings, while remaining the escaped quotes as they are.
        e.g example = "She said, \"Hello, world!\"" will be converted to example = """She said, \"Hello, world!\"
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

example = r'"She said, \"Hello, world!\""'
byte_stream = io.BytesIO(example.encode('utf-8'))
a= prepare(byte_stream.readline)()

print(a) # She said, """\"Hello, world!\""""


# Regular String to Byte String (Encoding)
regular_string = "Hello, 🌍!"
byte_string_encoded = regular_string.encode('utf-8')

# Byte String to Regular String (Decoding)
byte_string = b'Hello, \xf0\x9f\x8c\x8d!'
regular_string_decoded = byte_string.decode('utf-8')

print(byte_string_encoded)  # b'Hello, \xf0\x9f\x8c\x8d!'
print(regular_string_decoded)  # Hello, 🌍!


# difference between byte and raw byte is that raw byte does not process escape sequences
'''
Byte Literals (b prefix)
Byte literals are defined with a b prefix before the opening quote of the string literal.
They represent sequences of bytes, which are immutable sequences of integers in the range 0 <= x < 256.
Escape sequences in byte literals are interpreted. For example, \n is interpreted as a newline byte, and \xhh is interpreted as the byte with hexadecimal value hh.

Raw Byte Literals (rb or br prefix)
Raw byte literals combine the r (raw) prefix with the b prefix, and they can be prefixed in either order (rb or br).
They represent byte sequences where escape sequences are not processed. For example, rb'\n' represents the bytes '\\' and 'n', not a newline byte.
This is useful when you need to represent the bytes of a string without treating backslashes as escape characters.
'''