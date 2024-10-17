import argparse

# Create the parser
parser = argparse.ArgumentParser(description="An example script.")

# Add the --verbose flag
# This will set args.verbose to True if --verbose is used when the script is run.
parser.add_argument('--verbose', action='store_true', help='Enable verbose output')

# Parse the command line arguments
args = parser.parse_args()

# Use args.verbose in your program
if args.verbose:
    print(args.verbose)
    # print("Verbose mode enabled.")
else:
    print("Verbose mode not enabled.")
    
# -help in argparse
# When you run a Python script that uses the argparse module with the -h or --help flag, argparse automatically generates help output. This output includes the script's description (if provided when creating the ArgumentParser object), the usage syntax, and detailed information about each argument that has been added to the parser, including their help messages.