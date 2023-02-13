"""
Your module description
"""
import math

def get_double_alphabet(alphabet):
    double_alphabet = alphabet + alphabet
    return double_alphabet


def get_message_from_user():
    string_to_encrypt = input("Please enter a message to encrypt: ")
    return string_to_encrypt


def get_cipher_key():
    shift_amount = input( "Please enter a key (whole number from 1-25): ")
    return shift_amount


def encrypt_message(message, cipher_key, alphabet):
    encrypted_message = ""
    uppercase_message = ""
    uppercase_message = message.upper()

    for current_character in uppercase_message:
        position = alphabet.find(current_character)
        new_position = position + int(cipher_key)
        if current_character in alphabet:
            encrypted_message = encrypted_message + alphabet[new_position]
        else:
            encrypted_message = encrypted_message + current_character

    return encrypted_message


def decrypt_message(message, cipher_key, alphabet):
    decrypt_key = -1 * int(cipher_key)
    return encrypt_message(message, decrypt_key, alphabet)


def run_caesar_cipher_program():
    my_alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {my_alphabet}')
    my_alphabet_2 = get_double_alphabet(my_alphabet)
    print(f'Alphabet2: {my_alphabet_2}')
    my_message = get_message_from_user()
    print(my_message)
    my_cipher_key = get_cipher_key()
    print(my_cipher_key)
    my_encrypted_message = encrypt_message(my_message, my_cipher_key, my_alphabet_2)
    print(f'Encrypted Message: {my_encrypted_message}')
    my_decrypted_message = decrypt_message(my_encrypted_message, my_cipher_key, my_alphabet_2)
    print(f'Decypted Message: {my_decrypted_message}')

run_caesar_cipher_program()