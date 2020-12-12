#!/usr/bin/env python3

import datetime

# Needed Functions
def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])

def decoding(fileinput, fileoutput):
    with open(fileinput, 'r') as file_in:
        Lines = file_in.read()
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_in_temp = list(Lines.split("\n\n"))
        for line in file_in_temp:
            file_in_temp = line.replace(" ", "\n")
            file_in_temp = list(file_in_temp.split("\n"))
            text_out = bits2string(file_in_temp)
            with open(now + "-binarydecoded.txt", 'a+') as writefile:
                writefile.write(text_out + "\n\n")