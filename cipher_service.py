# cipher_service.py

def encrypt(text, shift):
    shift_amount = shift % 26  # Normalize the shift to within the alphabet range
    result = ""

    for char in text:
        if char.isupper():
            start = ord('A')
            encrypted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            result += encrypted_char
        elif char.islower():
            start = ord('a')
            encrypted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            result += encrypted_char
        else:
            result += char  # Non-alphabetic characters are added as-is
    
    return result


def decrypt(text, shift):
    # Decrypt by shifting in the opposite direction
    shift_amount = 26 - (shift % 26)
    return encrypt(text, shift_amount)  # Reuse the encrypt function for decryption
