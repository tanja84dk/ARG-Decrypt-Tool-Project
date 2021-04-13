#!/usr/bin/env python3

# Imports
import logging
from datetime import datetime
import base64
import logging

# Global Variables
debug = False
errorLog = "argtool.error.log"

class menus():
    '''
    Static class there only is used to print the menus
    Main menu is .main, base64 menu is .base, and 8bit binary menu is .bin
    '''

    @staticmethod
    def main():
        '''
        Printing the main menu list
        '''

        print(f" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        print(f" ARG Encrypt And Decrypt Tool")
        print(f" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        print(f" [1] Base64")
        print(f" [2] 8Bit Binary")
        print(f" ")
        print(f" [9] Exit")
        print(f" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        print(f" Release Version {argTools.argtoolVersion()}")
        print(f" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    
    @staticmethod
    def base64():
        '''
        Printing the base64 encoding and decoding sub menu list
        '''

        print(f" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        print(f" Base64 Encoding And Decoding")
        print(f" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        print(f" [1] Encoding From File")
        print(f" [2] Decoding From File")
        print(f" [3] Encoding From String")
        print(f" [4] Decoding From String")
        print(f" [9] Back To Main Menu")
        print(f" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

    @staticmethod
    def bin():
        '''
        Printing the 8bit binary encoding and decoding sub menu list
        '''

        print(f" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        print(f" Base64 Encoding And Decoding")
        print(f" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        print(f" [1] Encoding From File:")
        print(f" [2] Decoding From File:")
        print(f" [9] Back To Main Menu:")
        print(f" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

class argTools():
    
    def __init__(self):
        pass

    def remove_ext(fileInput):
        '''
        Removing everything from the last . till the end of the string
        will return input filename if no . is located
        '''
        
        filename = '.'.join(fileInput.split(".")[:-1])
        if len(filename) >= 1:
            return filename
        else:
            return fileInput

    @staticmethod
    def timestamp():
        '''
        Returning a timestamp of the pc's date and time.
        Timestamp is created like this 20201216_184216 and used as prefix for \
        output files
        '''

        return datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def try_read_file(filename):
        '''
        Trying to read the file content
        '''
        try:
            with open(filename, 'r') as file_in:
                Lines = file_in.read()
                return Lines
        except FileNotFoundError:
            print("File Not Found")
            Tools.pause("Press Enter To Go Back To Main Menu")
            return False
    
    @staticmethod
    def pause(message):
        input(f"{ message }")

    @staticmethod
    def argtoolVersion():
        try:
            with open(".version", 'r') as ver:
                ver = ver.readline()
            return ver
        except FileNotFoundError:
            return str(f"v0.3.0-dev")


class encryption():

    # Needed Functions
    def string2bits(s=''):
        return [bin(ord(x))[2:].zfill(8) for x in s]

    def bits2string(b=None):
        return ''.join([chr(int(x, 2)) for x in b])

    def encode_file_base64(inputFile, outputFile):
        '''
        Plain Text is the indput, and outputFile is output filename.
        Output file is prepended with date and time added to avoid overwrite
        '''    
        if argTools.try_read_file(inputFile) != False:
            now = argTools.timestamp() # Timestamp Creation
            pre_encode_message = argTools.try_read_file(inputFile)
            # pre_encode_message = pre_encode.read()
            pre_encode_bytes = pre_encode_message.encode('ascii')
            message_bytes = base64.b64encode(pre_encode_bytes)
            message = message_bytes.decode('ascii')
            with open(now + '-' + outputFile, 'w') as base64_encoded:
                base64_encoded.write(message)
            print(f"The encoded message is saved in a file called { now }-{ outputFile }")
            argTools.pause("Press Enter To Go Back To Main Menu")

    def encode_input_base64(plain_text, outputFile):
        '''
        Plain Text is the indput.
        Output file is prepended with date and time added to avoid overwrite
        '''
        now = argTools.timestamp() # Timestamp Creation
        pre_encode_message = plain_text
        message_bytes = pre_encode_message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        with open(now + '-' + outputFile, 'w') as base64_input_encode:
            base64_input_encode.write(base64_message)
        print(f"The encoded message is saved in a file called { now }-{ outputFile }")
        argTools.pause("Press Enter To Go Back To Main Menu")

    def decode_file_base64(inputFile, outputFile):
        '''
        Base64 encoded text file is input.
        Output file is prepended with date and time added to avoid overwrite
        '''
        #if try_read_file2(inputFile) != False:
        if argTools.try_read_file(inputFile) != False:
            now = argTools.timestamp() # Timestamp Creation
            # base64_encoded = argtools.try_read_file(inputFile)
            with open(inputFile, 'r') as base64_encoded:
                base64_message = base64_encoded.readline().rstrip()
                base64_bytes = base64_message.encode('ascii').rstrip()
                message_bytes = base64.b64decode(base64_bytes)
                message = message_bytes.decode('ascii')
                with open(now + '-' + outputFile, 'w') as base64_decoded:
                    base64_decoded.write(message)
            print(f"The decoded message is saved in a file called { now }-{ outputFile }")
            argTools.pause("Press Enter To Go Back To Main Menu")

    def decode_input_base64(inputString, outputFile):
        '''
        Base64 encoded text is the input from string.
        Output file is prepended with date and time added to avoid overwrite
        '''
        now = argTools.timestamp() # Timestamp Creation
        base64_message = inputString
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
        with open(now + '-' + outputFile, 'w') as base64_input_decoded:
                base64_input_decoded.write(message)
        print(f"The decoded message is saved in a file called { now }-{ outputFile }")
        argTools.pause("Press Enter To Go Back To Main Menu")

    def encode_file_8bit(inputFile, outputFile):
        """Plain Text is the indput, and outputFile is output filename.
        Output file is prepended with date and time added to avoid overwrite"""
        if argTools.try_read_file(inputFile) != False:
            now = argTools.timestamp() # Timestamp Creation
            Lines = argTools.try_read_file(inputFile)
            file_in_temp = encryption.string2bits(Lines)
            with open(now + "-" + outputFile, 'a+') as writefile:
                writefile.write(str(' ').join(file_in_temp))
            print(f"The encoded message is saved in a file called { now }-{ outputFile }")
            argTools.pause("Press Enter To Go Back To Main Menu")

    def decode_file_8bit(inputFile, outputFile):
        """8Bit binary ASCII encoded text file is input.
        Output file is prepended with date and time added to avoid overwrite"""
        if argTools.try_read_file(inputFile) != False:
            now = argTools.timestamp() # Timestamp Creation
            Lines = argTools.try_read_file(inputFile)
            file_in_temp = list(Lines.split("\n\n"))
            for line in file_in_temp:
                file_in_temp = line.replace(" ", "\n")
                file_in_temp = list(file_in_temp.split("\n"))
                text_out = encryption.bits2string(file_in_temp)
                with open(now + "-" + outputFile, 'a+') as writefile:
                    writefile.write(text_out + "\n\n")
                print(f"The decoded message is saved in a file called { now }-{ outputFile }")
                argTools.pause("Press Enter To Go Back To Main Menu")

def logToFile(logfile, logMessage):
            with open(logfile, 'a+') as logWriter:
                logWriter.write(f"{argTools.timestamp()} - {argTools.argtoolVersion()} - {logMessage}\n")


if __name__ == '__main__':
    menus.main()
    main_menu_choise = int(input("Enter your option: ") or '404')

    while main_menu_choise != 0:
        if main_menu_choise == 1:
            menus.base64()

            choice_submenu_base64 = int(input("Input Choice: ") or '404')

            if choice_submenu_base64 == 9:
                # Go Back To Main Menu
                choice_submenu_base64 = 0

            if choice_submenu_base64 == 1:
                # Encoding From File
                print("Input Filename: ")
                encoder_plain = input("Type the full file name, has to end with .txt and no spaces: ")
                argtool_base64.encode_file_base64(encoder_plain, f"base64_encoded-{ (argTools.remove_ext(encoder_plain)) }.txt")
                choice_submenu_base64 = 0
            
            elif choice_submenu_base64 == 2:
                # Decoding From File
                print("Input Filename On Encrypted File: ")
                decode_text_file = input("Type the full file name, has to end with .txt and no spaces: ")
                encryption.decode_file_base64(decode_text_file, f"base64-decoded-{ argTools.remove_ext(decode_text_file) }.txt")
                choice_submenu_base64 = 0
            
            elif choice_submenu_base64 == 3:
                # Encoding From String
                print("Enter String To Encode ( Only One Line ): ")
                encoded_man_input = input("String to encode: ")
                encryption.encode_input_base64(encoded_man_input, 'base64_encoded_output.txt')
                choice_submenu_base64 = 0


            elif choice_submenu_base64 == 4:
                # Decoding From String
                print("Enter String To Decode ( Only One Line ): ")
                decode_man_input = input("Encoded String: ")
                encryption.decode_input_base64(decode_man_input, 'base64-decoded-string.txt')
                choice_submenu_base64 = 0
            
            elif choice_submenu_base64 == 0:
                pass

            else:
                # Catch Wrong Input
                print("/n Error Wrong Input. Try Again Please: ")
                choice_submenu_base64 = 0

        elif main_menu_choise == 2:
            # 8Bit Binary Sub Menu
            menus.bin()
            choice_submenu_bin = int(input("Input Choice: ") or '404')

            if choice_submenu_bin == 9:
                # Go Back To Main Menu
                choice_submenu_bin = 0
                
            
            if choice_submenu_bin == 1:
                # Encode 8Bit From Plain Text File
                non_8bittext_file = input("Type the full file name, has to end with .txt and no spaces: ")
                encryption.encode_file_8bit(non_8bittext_file, f'8bit-encoded-{ (argTools.remove_ext(non_8bittext_file)) }.txt')
                choice_submenu_bin = 0
            
            if choice_submenu_bin == 2:
                # Decoding 8Bit Encoded Text File
                encoded_8bittext_file = input("Type the full file name, has to end with .txt and no spaces: ")
                encryption.decode_file_8bit(encoded_8bittext_file, f'8bit-decoded-{ (argTools.remove_ext(encoded_8bittext_file)) }.txt')
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
        menus.main()
        main_menu_choise = int(input("Enter your option: ") or '404')