#!/usr/bin/env python3

import base64
import datetime

def encode_base64(x):
    with open(x, 'r') as base64_decoded:
        message = base64_decoded.read()
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
    print(base64_message)

def encode_file_base64(x, y):
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(x, 'r') as pre_encode:
        pre_encode_message = pre_encode.read()
        pre_encode_bytes = pre_encode_message.encode('ascii')
        message_bytes = base64.b64encode(pre_encode_bytes)
        message = message_bytes.decode('ascii')
        with open(now + '-' + y, 'w') as base64_encoded:
            base64_encoded.write(message)
        print(message)

def encode_input_base64(x, y):
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    message = x
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    with open(now + '-' + y, 'w') as base64_input_encode:
        base64_input_encode.write(base64_message)
    print(base64_message)