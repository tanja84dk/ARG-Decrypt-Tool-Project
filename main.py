#!/usr/bin/env python3

# Imports

# My Include Files
from includes.menu import main as main_menu
from includes import decoder, debug, encoder, binary8bit

main_menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        # Encoding

        # Sub Menu
        print(" [1] From input (Only one line): ")
        print(" [2] From File: ")
        option_encode = int(input("Choose Encoding: "))
        while option_encode != 0:
            if option_encode == 1:
                # From String
                encoded_man_input = input("String to encode: ")
                encoder.encode_input_base64(encoded_man_input, 'base64_encoded_out.txt') 
                option_encode = 0

            elif option_encode == 2:
                # From File
                encoder_plain = input("Type the full file name, has to end with .txt and no spaces: ")
                encoder.encode_file_base64(encoder_plain, "base64_encoded_out.txt")
                option_encode = 0
            else:
                print("Wrong Choice of encoding")

    elif option == 2:
        # Decoding
        
        # Sub Menu
        print(" [1] From input: ")
        print(" [2] From File: ")
        option_decode = int(input("Choose Decoding: "))
        while option_decode != 0:
            if option_decode == 1:
                decode_man_input = input("Encoded String: ")
                decoder.decode_input_base64(decode_man_input, 'manout.txt')
                option_decode = 0
            elif option_decode == 2:
                decode_text_file = input("Type the full file name, has to end with .txt and no spaces: ")
                decoder.decode_file_base64(decode_text_file, "output.txt")
                option_decode = 0
            else:
                print("Issue")

    elif option == 3:
        print("Number 3: Binary From File Comming Soon")
    elif option == 4:
        print("Number 4: Comming Soon")
    else:
        print("Invalid Option")
        main_menu()
        option = int(input("Enter your option: "))
    
    print("\n\n")
    main_menu()
    option = int(input("Enter your option: "))