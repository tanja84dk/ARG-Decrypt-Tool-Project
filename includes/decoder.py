#!/usr/bin/python3

import base64
import datetime

def decoder_base64(x):
    with open(x, 'r') as base64_encoded:
        base64_message = base64_encoded.read()
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
        print(message)

def decode_file_base64(x, y):
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(x, 'r') as base64_encoded:
        base64_message = base64_encoded.readline().rstrip()
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
        with open(now + '-' + y, 'w') as base64_decoded:
            base64_decoded.write(message)
        print(message)

def decode_input_base64(x, y):
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    base64_message = x
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    with open(now + '-' + y, 'w') as base64_input_decoded:
            base64_input_decoded.write(message)
    print(message)