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

DIR_TO_SEARCH = ''
# For storing the directory argument in

REMOVE_FILES_ONCE_PROCESSED = False
# For storing whether the user would like to remove the files once processed

OLD_URLS_JSON_DIR = ''
# For storing the location of the old JSON data

OLD_URLS = {}
NEW_URLS = {}
# Used for storing old (read) and new (to be written) urls [JSON]

PARSER = argparse.ArgumentParser(description='A directory is required to scan for *.url files.')
# Creates a new argparse module, setting the description for the scripts arguments

PARSER.add_argument('-d', '--directory', help='Directory to search', required=True)
# For a directory to run the script on

PARSER.add_argument('-r', '--remove', help='Delete the files as they are processed',
                    required=False, action='store_true')
# If the user would like to remove the file once it is processed

PARSER.add_argument('-j', '--json',
                    help='Instead of creating a new output file, add to an existing JSON data set',
                    required=False)
# Ask for a directory to run the script on

ARGS = PARSER.parse_args()
# Get the argument values

DIR_TO_SEARCH = ARGS.directory
# Set the directory to search

REMOVE_FILES_ONCE_PROCESSED = ARGS.remove
# Set the users preference on file deletion

OLD_URLS_JSON_DIR = ARGS.json
# Set the value of the JSON dir

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

    if not os.path.isfile(current_file):
        continue
    # At this moment, no easy solution for dealing with filenames containing unicode
    # So, run a check to see if the file exists, if not, its probably unicode

    with open(current_file, "r") as infile:
        for line in infile:
            if line.startswith('URL'):
                NEW_URLS[current_file] = line[4:]
                break
    # Get the URL from the current file and add it into the dict

    if REMOVE_FILES_ONCE_PROCESSED:
        #os.remove(current_file)
        print 'remove'
# Iterate through each file that ends in url
# Check the file exists
# If it does, add the filename and url to the dict
# Remove the file if the user has specified to do so

with open('url_data.json', 'w') as file_output:
    json.dump(NEW_URLS, file_output, sort_keys=True, indent=4, ensure_ascii=False)
# Create a new JSON file in the current directory and dump the processed dict
