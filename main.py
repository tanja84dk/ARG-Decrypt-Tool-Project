#!/usr/bin/env python3

# Imports

# My Include Files
from includes.menu import main as main_menu
from includes import decoder, debug, encoder, ArgTool_binary8bit, ArgTool_base64

main_menu()
option = int(input("Enter your option: ") or '404')

while option != 0:
    if option == 1:
        # Base64 Sub Menu
        print(" [1] Encoding From File")
        print(" [2] Decoding From File")
        print(" [3] Encoding From String")
        print(" [4] Decoding From String")
        print(" [9] Back To Main Menu")
        print("")

        submenu_base64 = int(input("Input Choice: ") or '404')

        if submenu_base64 == 9:
            # Go Back To Main Menu
            submenu_base64 = 0

        if submenu_base64 == 1:
            # Encoding From File
            print("Input Filename: ")
            encoder_plain = input("Type the full file name, has to end with .txt and no spaces: ")
            ArgTool_base64.encode_file_base64(encoder_plain, f"base64_encoded-{ encoder_plain }.txt")
            submenu_base64 = 0
        
        elif submenu_base64 == 2:
            # Decoding From File
            print("Input Filename On Encrypted File: ")
            submenu_base64 = 0
        
        elif submenu_base64 == 3:
            # Encoding From String
            print("Enter String To Encode ( Only One Line ): ")
            submenu_base64 = 0

        elif submenu_base64 == 4:
            # Decoding From String
            print("Enter String To Decode ( Only One Line ): ")
            submenu_base64 = 0
        
        elif submenu_base64 == 0:
            pass

        else:
            # Catch Wrong Input
            print("/n Error Wrong Input. Try Again Please: ")
            submenu_base64 = 0

    elif option == 2:
        # 8Bit Sub Menu
        print(" [1] Encoding From File: ")
        print(" [2] Decoding From File: ")
        print(" [9] Back To Main Menu: \n")

        submenu_8bit = int(input("Input Choice: ") or '404')

        if submenu_8bit == 9:
            # Go Back To Main Menu
            submenu_8bit = 0
            
        
        if submenu_8bit == 1:
            pass
        
        if submenu_8bit == 2:
            # Decoding 8Bit Encoded Text File
            encoded_8bittext_file = input("Type the full file name, has to end with .txt and no spaces: ")
            ArgTool_binary8bit.decoding(encoded_8bittext_file, f'8bit-decoded-{ encoded_8bittext_file }.txt')
            submenu_8bit = 0
        
        if submenu_8bit == 0:
            pass

        else:
            # Catch Wrong Input
            print("/n Error Wrong Input. Try Again Please")
            submenu_base64 = 0


    elif option == 3:
        option_binary = int(input("Choose From List: ") or '404')
        while option_binary != 0:
            if option_binary == 1:
                decoded_8bittext_file = input("Type the full file name, has to end with .txt and no spaces: ")
                option_binary = 0
            elif option_binary == 2:
                print("Enter Encoded Filename: ")
                encoded_8bittext_file = input("Type the full file name, has to end with .txt and no spaces: ")
                ArgTool_binary8bit.decoding(encoded_8bittext_file, f'8bit-decoded-{ encoded_8bittext_file }.txt')
                option_binary = 0
            else:
                print("Wrong Choice Try Again")
                print(option_binary)
                option_binary = int(input("Choose From List: ") or '404')

        
    elif option == 4:
        print("Number 4: Comming Soon")
    else:
        print("Invalid Option")
        main_menu()
        option = int(input("Enter your option: "))
    
    print("\n\n")
    main_menu()
    option = int(input("Enter your option: ") or '404')