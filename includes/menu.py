#!/usr/bin/env python3

class Menus:
    '''
    Static class there only is used to print the menus
    Main menu is .main, base64 menu is .base, and binary menu is .bin
    '''

    @staticmethod
    def main():
        "Printing the main menu list"
        # Main Menu List
        print(" ")
        print(" ARG Encrypt And Decrypt Tool")
        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        print(" [1] Base64")
        print(" [2] 8Bit Binary")
        print(" ")
        print(" [9] Exit")
        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        print(" Release Version v0.2.0-beta")
        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    
    @staticmethod
    def base():
        "Printing the base64 encoding and decoding sub menu list"
        # Base64 Sub Menu List
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
        "Printing the 8bit binary encoding and decoding sub menu list"
        # 8Bit Binary Sub Menu
        print(" ")
        print(" Base64 Encoding And Decoding")
        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        print(" [1] Encoding From File:")
        print(" [2] Decoding From File:")
        print(" [9] Back To Main Menu:")
        print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

# Future Proof for only running if this file is run
if __name__ == '__main__':
    pass