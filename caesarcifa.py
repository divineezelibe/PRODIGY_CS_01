# main.py

import argparse
from cipher_service import encrypt, decrypt  # Import the functions from cipher_service.py

def display_intro():
    print("**************************************************")
    print("*                                                *")
    print("*  ███████╗███╗   ██╗██████╗ ███████╗ █████╗      *")
    print("*  ██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗     *")
    print("*  █████╗  ██╔██╗ ██║██║  ██║█████╗  ███████║     *")
    print("*  ██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██║     *")
    print("*  ███████╗██║ ╚████║██████╔╝███████╗██║  ██║     *")
    print("*  ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝     *")
    print("*                                                *")
    print("*    ENcryption & DEcryption CIfher for All      *")
    print("*                                                *")
    print("*              Created by Divine E. Ezelibe      *")
    print("*                                                *")
    print("**************************************************")
    print()
    print("🔐 Welcome to ENDECIFA – Your Caesar Cipher Toolkit! 🔐")
    print()
    print("🔄 With ENDECIFA, you can easily encrypt your messages or")
    print("   decrypt hidden texts with the power of Caesar Cipher.")
    print()
    print("✨ How to use ENDECIFA:")
    print("   - Use '-e' followed by your text and a shift value to encrypt.")
    print("   - Use '-d' followed by your text and a shift value to decrypt.")
    print()
    print("💡 Example:")
    print("   To encrypt: python main.py -e 'Hello, World!' 3")
    print("   To decrypt: python main.py -d 'Khoor, Zruog!' 3")
    print()
    print("🔍 Explore the secrets of encryption and decryption with ENDECIFA! 🚀")
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
        encrypted_message = encrypt(args.text, args.shift)
        print(f"🔒 Encrypted message: {encrypted_message}")
    elif args.decrypt:
        decrypted_message = decrypt(args.text, args.shift)
        print(f"🔓 Decrypted message: {decrypted_message}")
    else:
        print("❗ Please specify whether to encrypt (-e) or decrypt (-d) the text.")

if __name__ == "__main__":
    main()  # Call the main function to start the program
