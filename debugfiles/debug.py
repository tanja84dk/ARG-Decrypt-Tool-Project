#!/usr/bin/env python3

import datetime
import logging

def debugging(filename, debugmessage):
    "Writing Output to a log file to the folder for debugging. extension .log is added automaticly. filename is added to filename to easier locating. Output file is prepended with date and time added to avoid overwrite"
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    message = str(debugmessage)
    with open("debuglogs/" + now + "-debug-" + filename + ".log", 'w+') as debug_log:
            debug_log.write(message)


# Future Proof for only running if this file is run
if __name__ == '__main__':
    logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    logging.info('Example of logging with ISO-8601 timestamp')