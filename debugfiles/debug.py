#!/usr/bin/env python3

import datetime

def debugging(filename, debugmessage):
    "Writing Output to a log file to the folder for debugging. extension .log is added automaticly. filename is added to filename to easier locating. Output file is prepended with date and time added to avoid overwrite"
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    message = str(debugmessage)
    with open("debuglogs/" + now + "-debug-" + filename + ".log", 'w+') as debug_log:
            debug_log.write(message)