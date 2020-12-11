#!/usr/bin/env python3

import datetime

now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])

with open("binaryin.plain", 'r') as file:
    Lines = file.read()
    print(type(Lines))
#    print(Lines)
    new = list(Lines.split("\n\n"))
    print(type(new))
    with open(f"output/{ now }-debuglist.txt", 'a+') as debug:
        debug.write(str(new))
    
#   Debug Printing Each Message With A Line Between
#    print("Line Test")
    for line in new:
#        print(line + "\n")
        line_new = line.replace(" ", "\n")
#        print(line_new)
#        print(type(line_new))
        line_new = list(line_new.split("\n"))
#        print(type(line_new))
        test = bits2string(line_new)
        print(test)
        with open(f"output/{ now }-binarydecoded.txt", 'a+') as writefile:
            writefile.write(test + "\n\n")
