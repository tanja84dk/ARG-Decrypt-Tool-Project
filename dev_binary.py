#!/usr/bin/env python3

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
    with open("debuglist.txt", 'a+') as debug:
        debug.write(str(new))
    
#   Debug Printing Each Message With A Line Between
    print("Line Test")
    for line in new:
        print(line + "\n")
        line_new = line.replace(" ", "\n")
        print(line_new)
        line_new = line_new(Lines.split("\n"))
        print(type(line_new))
#        test = bits2string(line_new)
#        print(test)
#    print(new)
#    count = 0
#    for line in Lines:
#        print(line.strip())
#        print(list(line.strip()))
#    for line in Lines:
#        print("Line{}: {}".format(count, line.strip()))