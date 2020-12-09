#!/usr/bin/python3

import base64

def decoder_base64(x):
    with open(x, 'r') as base64_encoded:
        base64_message = base64_encoded.read()
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
        print(message)

def decode_file_base64(x):
    with open(x, 'r') as base64_encoded:
        base64_message = base64_encoded.readline(1)
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
        print(message)

def decode_input_base64():
    base64_message = input("Enter String: ")
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    print(message)