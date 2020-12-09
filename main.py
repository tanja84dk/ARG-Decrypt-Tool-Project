#!/usr/bin/env python3

## Imports

## My Include Files
from includes.menu import main as main_menu
from includes import decoder, encoder
# from includes import encoder

main_menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        print("Encoding")
        encoder.encode_base64("decoded.txt")
    elif option == 2:
        print("Decoding")
        
        # Sub Menu
        print(" [1] From input: ")
        print(" [2] From File: ")
        option_decode = int(input("Choose Decoding: "))
        while option_decode != 0:
            if option_decode == 1:
                decode_man_input = input("Encoded String: ")
                # print("Encoded String: ")
                decoder.decode_input_base64(decode_man_input, 'manout.txt')
                option_decode = 0
            elif option_decode == 2:
                print("2. From File")
                decoder.decode_file_base64("encoded.txt", "output.txt")
                option_decode = 0
            else:
                print("Issue")

    elif option == 3:
        print("Number 3: Comming Soon")
    elif option == 4:
        print("Number 4: Comming Soon")
    else:
        print("Invalid Option")
        main_menu()
        option = int(input("Enter your option: "))
    
    print("\n\n")
    main_menu()
    option = int(input("Enter your option: "))
