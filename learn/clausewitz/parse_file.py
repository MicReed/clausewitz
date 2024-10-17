import sys

from clausewitz.util.tokenize import prepare
from tokenize import tokenize
from parse import parse
def parse_file(file_path):
    '''
    Parse the file using the parse_cmd function
    '''
    with open(file_path, 'rb') as f:
        # Prepare the readline function for tokenization
        readline = prepare(f.readline)
        # Tokenize the input file
        tokens = tokenize(readline)
        # Parse the tokens to get the structured data
        value = parse(tokens)

if __name__ == '__main__':
    parse_file(sys.argv[1])