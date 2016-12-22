# As this is my first excursion into Python, this script is heavily (OTT) documented

"""Simple script to sort out my internet shortcut archive.
   This will eventually lead to *smrt* sorting of url's into categories/types for easy reference.
   Stores data into a JSON format."""
# Docstring, required for C0111
# Provides help information about the scripts purpose
# Multiple lines as per C0301 (100 char limit per line)

import os
import glob
import argparse
# Import OS for filesystem
# Import glob for dealing with path names
# Import argparse for easy management of script arguments
# Imports spread across multiple lines as per C0410

PARSER = argparse.ArgumentParser(description='A directory is required to scan for *.url files.')
# Creates a new argparse module, setting the description for the scripts arguments

PARSER.add_argument('-d', '--directory', help='Directory to search', required=True)
# Add an argument with the required information

ARGS = PARSER.parse_args()
# Get the argument values

try:
    if not os.path.isdir(ARGS.directory):
        raise ValueError('The path specified is not a directory')

except ValueError, error:
    exit(str(error))
# Check whether the passed argument is a directory, if it isn't throw an error

DIR_TO_SEARCH = os.chdir(ARGS.directory)
# Set the directory to search to the users specified directory

for file_temp in glob.glob("*.url"):
    print file_temp
# Iterate through each file that ends in url and print it (for testing)
