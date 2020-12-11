#!/usr/bin/env python3

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
#    print(new)
#    count = 0
#    for line in Lines:
#        print(line.strip())
#        print(list(line.strip()))
#    for line in Lines:
#        print("Line{}: {}".format(count, line.strip()))