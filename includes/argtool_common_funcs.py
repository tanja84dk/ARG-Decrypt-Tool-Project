#!/usr/bin/env python3

# My Include Files
from includes.argtool_classes import Tools as argtools

def remove_ext(fileinput):
    '''
    Removing everything after the last period in the string
    '''
    filename = '.'.join(fileinput.split(".")[:-1])
    if len(filename) >= 1:
        return filename
    else:
        return fileinput

def try_read_file(filename):
    '''
    Trying to read the file content
    '''
    try:
        with open(filename, 'r') as file_in:
            Lines = file_in.read()
            return Lines
    except FileNotFoundError:
        print("File Not Found")
        argtools.pause("Press Enter To Go Back To Main Menu")
        return False

# Future Proof for only running if this file is run
if __name__ == '__main__':
    pass