import tokenize
from io import StringIO

code = "a + b"
tokens = tokenize.generate_tokens(StringIO(code).readline)

'''
print algorithm:

Use f-strings with specified width for each field. You can use {:<width} for left alignment, {:^width} for center alignment, and {:>width} for right alignment, where width is the number of characters you want the field to occupy.
'''
    
for token in tokens:
    print(f'token.string: {token.string:<10}\t token.type: {token.type:<3}\t tokenize.tok_name[token.type]: {tokenize.tok_name[token.type]:<15}\t token.exact_type: {token.exact_type:<3}')