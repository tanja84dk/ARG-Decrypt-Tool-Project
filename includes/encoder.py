#!/usr/bin/env python3

import base64

def encode_base64():
    with open('decoded.txt', 'r') as base64_decoded:
        message = base64_decoded.read()
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes, altchars=None)
        base64_message = base64_bytes.decode('ascii')
    print(base64_message)