#!/usr/bin/python3

import base64
import datetime

# My Include Files
from includes import argtool_common_funcs as argfunc # Importing My Shared Functions
from includes.argtool_classes import Tools as argtools # Importing My Tool Class

def try_read_file2(filename):
    '''
    Trying to read the file content
    '''
    try:
        with open(filename, 'r') as file_in:
            Lines = file_in.read()
            return Lines
    except FileNotFoundError:
        print("File Not Found")
        argtools.pause("Press Enter To Go Back To Main Menu")
        return False

def encode_file_base64(input_file, output_file):
    '''
    Plain Text is the indput, and output_file is output filename.
    Output file is prepended with date and time added to avoid overwrite
    '''    
    if try_read_file2(input_file) != False:
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") # Timestamp Creation
        pre_encode_message = try_read_file2(input_file)
        # pre_encode_message = pre_encode.read()
        pre_encode_bytes = pre_encode_message.encode('ascii')
        message_bytes = base64.b64encode(pre_encode_bytes)
        message = message_bytes.decode('ascii')
        with open(now + '-' + output_file, 'w') as base64_encoded:
            base64_encoded.write(message)
        print(f"The encoded message is saved in a file called { now }-{ output_file }")
        argtools.pause("Press Enter To Go Back To Main Menu")

def encode_input_base64(plain_text, output_file):
    '''
    Plain Text is the indput.
    Output file is prepended with date and time added to avoid overwrite
    '''
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") # Timestamp Creation
    pre_encode_message = plain_text
    message_bytes = pre_encode_message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    with open(now + '-' + output_file, 'w') as base64_input_encode:
        base64_input_encode.write(base64_message)
    print(f"The encoded message is saved in a file called { now }-{ output_file }")
    argtools.pause("Press Enter To Go Back To Main Menu")

def decode_file_base64(input_file, output_file):
    '''
    Base64 encoded text file is input.
    Output file is prepended with date and time added to avoid overwrite
    '''
    #if try_read_file2(input_file) != False:
    if try_read_file2(input_file) != False:
        now = argtools.timeStamp() # Timestamp Creation
        # base64_encoded = argtools.try_read_file(input_file)
        with open(input_file, 'r') as base64_encoded:
            base64_message = base64_encoded.readline().rstrip()
            base64_bytes = base64_message.encode('ascii').rstrip()
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode('ascii')
            with open(now + '-' + output_file, 'w') as base64_decoded:
                base64_decoded.write(message)
        print(f"The decoded message is saved in a file called { now }-{ output_file }")
        argtools.pause("Press Enter To Go Back To Main Menu")

def decode_input_base64(string_input, output_file):
    '''
    Base64 encoded text is the input from string.
    Output file is prepended with date and time added to avoid overwrite
    '''
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") # Timestamp Creation
    base64_message = string_input
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    with open(now + '-' + output_file, 'w') as base64_input_decoded:
            base64_input_decoded.write(message)
    print(f"The decoded message is saved in a file called { now }-{ output_file }")
    argtools.pause("Press Enter To Go Back To Main Menu")

# Future Proof for only running if this file is run
if __name__ == '__main__':
    pass
