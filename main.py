#!/usr/bin/env python3

# Imports

# My Include Files
from includes.menu import main as main_menu
from includes import ArgTool_binary8bit, ArgTool_base64
from debugfiles import debug

Debuging = False

main_menu()
main_menu_choise = int(input("Enter your option: ") or '404')

while main_menu_choise != 0:
    if main_menu_choise == 1:
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
            if Debuging == True: debug.debugging("base64encffile.txt", encoder_plain)
            ArgTool_base64.encode_file_base64(encoder_plain, f"base64_encoded-{ encoder_plain }.txt")
            submenu_base64 = 0
        
        elif submenu_base64 == 2:
            # Decoding From File
            print("Input Filename On Encrypted File: ")
            decode_text_file = input("Type the full file name, has to end with .txt and no spaces: ")
            if Debuging == True: debug.debugging("base64decffile.txt", decode_text_file)
            ArgTool_base64.decode_file_base64(decode_text_file, f"base64-decoded-{ decode_text_file }.txt")
            submenu_base64 = 0
        
        elif submenu_base64 == 3:
            # Encoding From String
            print("Enter String To Encode ( Only One Line ): ")
            encoded_man_input = input("String to encode: ")
            if Debuging == True: debug.debugging("base64encfstring.txt", encoded_man_input)
            ArgTool_base64.encode_input_base64(encoded_man_input, 'base64_encoded_output.txt')
            submenu_base64 = 0
            input("\n\n Press Enter To Contiue: ")


        elif submenu_base64 == 4:
            # Decoding From String
            print("Enter String To Decode ( Only One Line ): ")
            decode_man_input = input("Encoded String: ")
            if Debuging == True: debug.debugging("base64decfstring.txt", decode_man_input)
            ArgTool_base64.decode_input_base64(decode_man_input, 'base64-decoded-string.txt')
            submenu_base64 = 0
        
        elif submenu_base64 == 0:
            pass

        else:
            # Catch Wrong Input
            print("/n Error Wrong Input. Try Again Please: ")
            submenu_base64 = 0

    elif main_menu_choise == 2:
        # 8Bit Sub Menu
        print(" [1] Encoding From File ( Placeholder Comming Soon ): ")
        print(" [2] Decoding From File: ")
        print(" [9] Back To Main Menu: \n")

        submenu_8bit = int(input("Input Choice: ") or '404')

        if submenu_8bit == 9:
            # Go Back To Main Menu
            submenu_8bit = 0
            
        
        if submenu_8bit == 1:
            # Encode 8Bit From Plain Text File
            non_8bittext_file = input("Type the full file name, has to end with .txt and no spaces: ")
            if Debuging == True: debug.debugging("8bitencffile.txt", non_8bittext_file)
            ArgTool_binary8bit.encode_file_8bit(non_8bittext_file, f'8bit-encoded-{ non_8bittext_file }.txt')
            submenu_8bit = 0
        
        if submenu_8bit == 2:
            # Decoding 8Bit Encoded Text File
            encoded_8bittext_file = input("Type the full file name, has to end with .txt and no spaces: ")
            if Debuging == True: debug.debugging("8bitdecffile.txt", encoded_8bittext_file)
            ArgTool_binary8bit.decode_file_8bit(encoded_8bittext_file, f'8bit-decoded-{ encoded_8bittext_file }.txt')
            submenu_8bit = 0
        
        if submenu_8bit == 0:
            pass

        else:
            # Catch Wrong Input
            print("/n Error Wrong Input. Try Again Please")
            submenu_base64 = 0

    else:
        print("Invalid Option")
    
    print("\n\n")
    main_menu()
    main_menu_choise = int(input("Enter your option: ") or '404')