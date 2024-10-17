import sys
from parse import parse_cmd

# Assuming parse_cmd can take a file path as an argument
if len(sys.argv) > 1:
    file_path = sys.argv[1]
    parse_cmd(file_path)
else:
    print("Please provide a file path as an argument.")