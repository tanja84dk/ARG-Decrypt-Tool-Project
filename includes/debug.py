#!/usr/bin/env python3

def debugging(x, y):
    message = y
    with open("debug-" + x, 'w') as debug_log:
            debug_log.write(message)