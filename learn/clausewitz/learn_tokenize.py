import io
from tokenize import tokenize

'''
The tokenize.tokenize function specifically takes a byte stream as input and yields tokens in the form of 5-tuples. Each tuple contains the following information:

Type: The type of the token, which corresponds to specific constants defined in the token module (e.g., STRING, NUMBER, NAME, OP(operator)).
String: The exact string of the token in the source code.
Start: The starting position of the token as a (line, column) tuple.
End: The ending position of the token as a (line, column) tuple.
Line: The full line of source code on which the token was found.

'''

# Sample Python code
code = "print('Hello, world!')"
'''
Creating a BytesIO object: byte_stream = io.BytesIO(code.encode('utf-8'))

code.encode('utf-8') converts the code string into bytes using UTF-8 encoding.
io.BytesIO(...) creates a BytesIO object with the byte representation of the Python code. This object can be used as if it were a file.

io.BytesIO(...) creates an in-memory bytes buffer that can be used as a file-like object. This is useful for processing data that behaves like a file without necessarily having to read from or write to an actual file on the disk.
'''
byte_stream = io.BytesIO(code.encode('utf-8'))

# Tokenizing the code
for token in tokenize(byte_stream.readline):
    print(token)