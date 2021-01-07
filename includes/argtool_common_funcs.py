#!/usr/bin/env python3

def remove_ext(fileinput):
    """Removing everything from the last . till the end of the string"""
    filename = '.'.join(fileinput.split(".")[:-1])
    return filename

def try_read_file(filename):
    """Trying to read the file content"""
    try:
        with open(filename, 'r') as file_in:
            Lines = file_in.read()
            return Lines
    except FileNotFoundError:
        print("File Not Found")
        input("Press Enter To Go Back To Main Menu")
        return False

# Future Proof for only running if this file is run
if __name__ == '__main__':
    pass