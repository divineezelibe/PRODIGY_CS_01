# main.py

from cipher_service import encrypt, decrypt  # Import the functions from cipher_service.py

def main():
    # Ask the user whether they want to encrypt or decrypt
    operation = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()

    # Get the message and shift value from the user
    message = input("Enter your message: ").strip()
    shift = int(input("Enter the shift value (integer): "))

    if operation == 'E':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif operation == 'D':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid operation! Please choose 'E' for encrypt or 'D' for decrypt.")

if __name__ == "__main__":
    main()  # Call the main function to start the program
