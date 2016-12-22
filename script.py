# As this is my first excursion into Python, this script is heavily (OTT) documented

"""Simple script to sort out my internet shortcut archive.
   This will eventually lead to *smrt* sorting of url's into categories/types for easy reference.
   Stores data into a JSON format."""
# Docstring, required for C0111
# Provides help information about the scripts purpose
# Multiple lines as per C0301 (100 char limit per line)

import os
import argparse
import glob
import json
#import pprint
# OS for filesystem
# Argparse for easy management of script arguments
# Glob for dealing with path names
# JSON for data manipulation/storage
# pprint for similar behavior of PHP's var_dump, pprint.pprint(VAR), helps with debugging
# Spread across multiple lines as per C0410

PARSER = argparse.ArgumentParser(description='A directory is required to scan for *.url files.')
# Creates a new argparse module, setting the description for the scripts arguments

PARSER.add_argument('-d', '--directory', help='Directory to search', required=True)
# Add an argument with the required information

ARGS = PARSER.parse_args()
# Get the argument values

DIR_TO_SEARCH = ARGS.directory
# Set the directory to search

#pprint.pprint(DIR_TO_SEARCH)

try:
    if not os.path.isdir(DIR_TO_SEARCH):
        raise ValueError('Error: The path specified is not a directory')

except ValueError, error:
    exit(str(error))
# Check whether the passed argument is a directory, if it isn't throw an error

os.chdir(DIR_TO_SEARCH)
# Set the directory to search to the users specified directory

for current_file in glob.glob("*.url"):

    #current_file = unicode(current_file, 'utf-8', errors='ignore')

    if not os.path.isfile(current_file):
        print 'ALERT: contains unicode, just fucking skip it for now'
        continue
    # At this moment, no easy solution for dealing with filenames containing unicode
    # So, run a check to see if the file exists, if not, its probably unicode

    with open(current_file, "r") as infile:
        for line in infile:
            if line.startswith('URL'):
                print line[4:]
                break
# Iterate through each file that ends in url
# Check the file exists
# If it does, grab the url
