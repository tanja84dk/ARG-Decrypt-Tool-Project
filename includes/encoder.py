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

def encode_input_base64(x, y):
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    message = x
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    with open(now + '-' + y, 'w') as base64_input_encode:
        base64_input_encode.write(message)
    print(base64_message)