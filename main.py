#!/usr/bin/env python3

# Imports
import logging
import datetime

# My Include Files
from includes.argtool_classes import MenusList as Menus # Importing the Print Menu classes
from includes.argtool_classes import Tools as argTools # Importing the Tool classes
from includes import argtool_binary8bit, argtool_base64, argtool_common_funcs

# Global Variables
errorLog = "argtool.error.log"

def logToFile(logfile, logMessage):
            with open(logfile, 'a+') as logWriter:
                logWriter.write(f"{argTools.timeStamp()} - {argTools.argtoolVersion()} - {logMessage}\n")


if __name__ == '__main__':
    Menus.main()
    main_menu_choise = int(input("Enter your option: ") or '404')

    while main_menu_choise != 0:
        if main_menu_choise == 1:
            Menus.base64()

            choice_submenu_base64 = int(input("Input Choice: ") or '404')

            if choice_submenu_base64 == 9:
                # Go Back To Main Menu
                choice_submenu_base64 = 0

            if choice_submenu_base64 == 1:
                # Encoding From File
                print("Input Filename: ")
                encoder_plain = input("Type the full file name, has to end with .txt and no spaces: ")
                argtool_base64.encode_file_base64(encoder_plain, f"base64_encoded-{ (argtool_common_funcs.remove_ext(encoder_plain)) }.txt")
                choice_submenu_base64 = 0
            
            elif choice_submenu_base64 == 2:
                # Decoding From File
                print("Input Filename On Encrypted File: ")
                decode_text_file = input("Type the full file name, has to end with .txt and no spaces: ")
                argtool_base64.decode_file_base64(decode_text_file, f"base64-decoded-{ (argtool_common_funcs.remove_ext(decode_text_file)) }.txt")
                choice_submenu_base64 = 0
            
            elif choice_submenu_base64 == 3:
                # Encoding From String
                print("Enter String To Encode ( Only One Line ): ")
                encoded_man_input = input("String to encode: ")
                argtool_base64.encode_input_base64(encoded_man_input, 'base64_encoded_output.txt')
                choice_submenu_base64 = 0
                input("\n\n Press Enter To Contiue: ")


            elif choice_submenu_base64 == 4:
                # Decoding From String
                print("Enter String To Decode ( Only One Line ): ")
                decode_man_input = input("Encoded String: ")
                argtool_base64.decode_input_base64(decode_man_input, 'base64-decoded-string.txt')
                choice_submenu_base64 = 0
            
            elif choice_submenu_base64 == 0:
                pass

            else:
                # Catch Wrong Input
                print("/n Error Wrong Input. Try Again Please: ")
                choice_submenu_base64 = 0

        elif main_menu_choise == 2:
            # 8Bit Binary Sub Menu
            Menus.bin()
            choice_submenu_bin = int(input("Input Choice: ") or '404')

            if choice_submenu_bin == 9:
                # Go Back To Main Menu
                choice_submenu_bin = 0
                
            
            if choice_submenu_bin == 1:
                # Encode 8Bit From Plain Text File
                non_8bittext_file = input("Type the full file name, has to end with .txt and no spaces: ")
                argtool_binary8bit.encode_file_8bit(non_8bittext_file, f'8bit-encoded-{ (argtool_common_funcs.remove_ext(non_8bittext_file)) }.txt')
                choice_submenu_bin = 0
            
            if choice_submenu_bin == 2:
                # Decoding 8Bit Encoded Text File
                encoded_8bittext_file = input("Type the full file name, has to end with .txt and no spaces: ")
                argtool_binary8bit.decode_file_8bit(encoded_8bittext_file, f'8bit-decoded-{ (argtool_common_funcs.remove_ext(encoded_8bittext_file)) }.txt')
                choice_submenu_bin = 0
            
            if choice_submenu_bin == 0:
                pass

            else:
                # Catch Wrong Input
                print("/n Error Wrong Input. Try Again Please")
                choice_submenu_bin = 0

        elif main_menu_choise == 9:
            break

        else:
            print("Invalid Option")
        
        print("\n\n")
        Menus.main()
        main_menu_choise = int(input("Enter your option: ") or '404')