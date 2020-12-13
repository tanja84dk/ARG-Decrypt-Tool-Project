#!/usr/bin/env python3

import datetime

# Needed Functions
def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])


# My Functions
def encode_file_8bit(fileinput, fileoutput):
    "Plain Text is the indput. And output_file is output filename. Output file is prepended with date and time added to avoid overwrite"
    with open(fileinput, 'r') as file_in:
        Lines = file_in.read()
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_in_temp = string2bits(Lines)
        with open(now + fileoutput, 'a+') as writefile:
            writefile.write(str(' ').join(file_in_temp))


def decode_file_8bit(fileinput, fileoutput):
    "8Bit binary ASCII encoded text file is input. Output file is prepended with date and time added to avoid overwrite"
    with open(fileinput, 'r') as file_in:
        Lines = file_in.read()
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_in_temp = list(Lines.split("\n\n"))
        for line in file_in_temp:
            file_in_temp = line.replace(" ", "\n")
            file_in_temp = list(file_in_temp.split("\n"))
            text_out = bits2string(file_in_temp)
            with open(now + fileoutput, 'a+') as writefile:
                writefile.write(text_out + "\n\n")