#!/usr/bin/env python3

import datetime

# My Include Files
from includes import argtool_common_funcs as argfunc # Importing My Shared Functions
from includes.argtool_classes import Tools as argtools # Importing My Tools Class

# Needed Functions
def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])


# My Functions

def timestamp():
    """Returning a timestamp of the pc's date and time.
    Timestamp is created like this 20201216_184216 and used as prefix for output files"""
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")


def encode_file_8bit(fileinput, fileoutput):
    """Plain Text is the indput, and output_file is output filename.
    Output file is prepended with date and time added to avoid overwrite"""
    if argfunc.try_read_file(fileinput) != False:
        now = timestamp() # Timestamp Creation
        Lines = argfunc.try_read_file(fileinput)
        file_in_temp = string2bits(Lines)
        with open(now + "-" + fileoutput, 'a+') as writefile:
            writefile.write(str(' ').join(file_in_temp))


def decode_file_8bit(fileinput, fileoutput):
    """8Bit binary ASCII encoded text file is input.
    Output file is prepended with date and time added to avoid overwrite"""
    if argfunc.try_read_file(fileinput) != False:
        now = timestamp() # Timestamp Creation
        Lines = argfunc.try_read_file(fileinput)
        file_in_temp = list(Lines.split("\n\n"))
        for line in file_in_temp:
            file_in_temp = line.replace(" ", "\n")
            file_in_temp = list(file_in_temp.split("\n"))
            text_out = bits2string(file_in_temp)
            with open(now + "-" + fileoutput, 'a+') as writefile:
                writefile.write(text_out + "\n\n")


# Future Proof for only running if this file is run
if __name__ == '__main__':
    pass