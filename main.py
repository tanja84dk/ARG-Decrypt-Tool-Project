#!/usr/bin/env python3

## Imports
# from os import listdir

## My Include Files
from includes.menu import main as main_menu
from includes import decoder
from includes import encoder

main_menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        print("Encoding")
        encoder.encode_base64("decoded.txt")
    elif option == 2:
        print("Decoding")
        decoder.decoder_base64("encoded.txt")
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
