#!/usr/bin/env python3

## Imports
import base64
from sys import argv
from os import path
from os import listdir

## My Include Files
from includes.menu import main as main_menu
from includes import decoder
from includes import encoder

## My Variables
#arg1 = argv[1]
#arg2 = argv[2]

## My Functions

# List a directory
def dir_list(dir):
    for f in listdir(dir):
        print(f)


## Example
# folder = input("What folder would you like to print out? ")
# dir_list(folder)

main_menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        print("Encoding")
        encoder.encode_base64()
    elif option == 2:
        print("Decoding")
        decoder.decoder_base64()
    elif option == 3:
        print("Number 3")
    elif option == 4:
        print("Number 4")
    else:
        print("Invalid Option")
        main_menu()
        option = int(input("Enter your option: "))
    
    print("\n\n")
    main_menu()
    option = int(input("Enter your option: "))
