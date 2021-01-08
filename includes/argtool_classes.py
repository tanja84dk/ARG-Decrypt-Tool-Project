#!/usr/bin/env python3

## Includes
from datetime import datetime

class MenusList:
    '''
    Static class there only is used to print the menus
    Main menu is .main, base64 menu is .base, and 8bit binary menu is .bin
    '''

    @staticmethod
    def main():
        '''
        Printing the main menu list
        '''

        print(f" ")
        print(f" ARG Encrypt And Decrypt Tool")
        print(f" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        print(f" [1] Base64")
        print(f" [2] 8Bit Binary")
        print(f" ")
        print(f" [9] Exit")
        print(f" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        print(f" Release Version {Tools.argtoolVersion()}")
        print(f" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    
    @staticmethod
    def base64():
        '''
        Printing the base64 encoding and decoding sub menu list
        '''

        print(" ")
        print(" Base64 Encoding And Decoding")
        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        print(" [1] Encoding From File")
        print(" [2] Decoding From File")
        print(" [3] Encoding From String")
        print(" [4] Decoding From String")
        print(" [9] Back To Main Menu")
        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

    @staticmethod
    def bin():
        '''
        Printing the 8bit binary encoding and decoding sub menu list
        '''

        print(" ")
        print(" Base64 Encoding And Decoding")
        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        print(" [1] Encoding From File:")
        print(" [2] Decoding From File:")
        print(" [9] Back To Main Menu:")
        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

class Tools():
    
    def __init__(self):
        pass

    def remove_ext(self, fileinput):
        '''
        Removing everything from the last . till the end of the string
        will return input filename if no . is located
        '''
        
        filename = '.'.join(fileinput.split(".")[:-1])
        if len(filename) >= 1:
            return filename
        else:
            return fileinput

    @staticmethod
    def timeStamp():
        '''
        Returning a timestamp of the pc's date and time.
        Timestamp is created like this 20201216_184216 and used as prefix for output files
        '''

        return datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def try_read_file(self, filename):
        '''
        Trying to read the file content
        '''
        try:
            with open(filename, 'r') as file_in:
                Lines = file_in.read()
                return Lines
        except FileNotFoundError:
            print("File Not Found")
            input("Press Enter To Go Back To Main Menu")
            return False
    
    @staticmethod
    def argtoolVersion():
        with open(".version", 'r') as ver:
            ver = ver.readline()
        return ver

class Crypt():
    '''
    Working on getting the encrypt and decrypt added in here prober 
    '''

    def __init__(self):
        pass

# Future Proof for only running if this file is run
if __name__ == '__main__':
    pass