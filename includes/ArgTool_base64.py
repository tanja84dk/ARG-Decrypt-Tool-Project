#!/usr/bin/python3

import base64
import datetime

def encode_file_base64(input_file, output_file):
    "Plain Text is the indput. And output_file is output filename. Output file is prepended with date and time added to avoid overwrite"
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(input_file, 'r') as pre_encode:
        pre_encode_message = pre_encode.read()
        pre_encode_bytes = pre_encode_message.encode('ascii')
        message_bytes = base64.b64encode(pre_encode_bytes)
        message = message_bytes.decode('ascii')
        with open(now + '-' + output_file, 'w') as base64_encoded:
            base64_encoded.write(message)
        print(message)

def encode_input_base64(plain_text, output_file):
    "Plain Text is the indput. Output file is prepended with date and time added to avoid overwrite"
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    pre_encode_message = plain_text
    message_bytes = pre_encode_message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    with open(now + '-' + output_file, 'w') as base64_input_encode:
        base64_input_encode.write(base64_message)
    print(base64_message)

def decode_file_base64(input_file, output_file):
    "Base64 encoded text file is input. Output file is prepended with date and time added to avoid overwrite"
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(input_file, 'r') as base64_encoded:
        base64_message = base64_encoded.readline().rstrip()
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
        with open(now + '-' + output_file, 'w') as base64_decoded:
            base64_decoded.write(message)
        print(message)

def decode_input_base64(string_input, output_file):
    "Base64 encoded text is the input from string. Output file is prepended with date and time added to avoid overwrite"
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    base64_message = string_input
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    with open(now + '-' + output_file, 'w') as base64_input_decoded:
            base64_input_decoded.write(message)
    print(message)

# Future Proof for only running if this file is run
if __name__ == '__main__':
    pass