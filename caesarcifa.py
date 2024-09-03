# main.py

import argparse
from cipher_service import encrypt, decrypt  # Import the functions from cipher_service.py

def display_intro():
    print("  ***********************************************")
    print(" *                                               *")
    print("*    ███████╗███╗   ██╗██████╗ ███████╗ █████╗    *")
    print("*    ██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗   *")
    print("*    █████╗  ██╔██╗ ██║██║  ██║█████╗  ███████║   *")
    print("*    ██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██║   *")
    print("*    ███████╗██║ ╚████║██████╔╝███████╗██║  ██║   *")
    print("*    ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝   *")
    print(" *                                               *")
    print(" *    ENcryption & DEcryption CIfher for All     *")
    print(" *                                               *")
    print(" *              Created by Divine E. Ezelibe     *")
    print(" *                                               *")
    print(" *************************************************")
    print()
    print(" Welcome to ENDECIFA – Your Caesar Cipher Toolkit! 🔐")
    print()

def display_result(result, mode):
    print("==================================================")
    print("                * ENDECIFA RESULT *               ")
    print("==================================================")
    if mode == 'encrypt':
        print(f" Encrypted message: {result}")
    elif mode == 'decrypt':
        print(f" Decrypted message: {result}")
    print("==================================================")
    print()

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Encrypt or Decrypt messages using the Caesar Cipher.')
    
    # Define arguments
    parser.add_argument('-e', '--encrypt', help='Encrypt the provided text.', action='store_true')
    parser.add_argument('-d', '--decrypt', help='Decrypt the provided text.', action='store_true')
    parser.add_argument('text', help='The text to be encrypted or decrypted.')
    parser.add_argument('shift', type=int, help='The shift value (integer).')
    
    # Parse the arguments
    args = parser.parse_args()

    # Display the introduction
    display_intro()

    # Determine the operation and call the appropriate function
    if args.encrypt:
        result = encrypt(args.text, args.shift)
        display_result(result, 'encrypt')
    elif args.decrypt:
        result = decrypt(args.text, args.shift)
        display_result(result, 'decrypt')
    else:
        print("❗ Please specify whether to encrypt (-e) or decrypt (-d) the text.")

if __name__ == "__main__":
    main()  # Call the main function to start the program
