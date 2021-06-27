"""
File: caesar.py
Author: Wade Chao
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    decipher_message()


def decipher_message():
    """
    Get secret number and ciphered message, decipher and print the authentic message.
    """
    secret_num = get_secret_num()
    ciphered_message = get_ciphered_message()
    deciphered_message = get_deciphered_message(secret_num, ciphered_message)
    print_result(deciphered_message)


def get_deciphered_message(secret_num, ciphered_message):
    """
    Iterate ciphered message,
     - if character is NOT alphabet then put it in the result directly.
     - If character is alphabet then get the authentic character and put it in the result.
    """
    result = ''
    for char in ciphered_message:
        if not char.isalpha():
            result += char
            continue
        for j in range(len(ALPHABET)):
            if char == ALPHABET[j]:
                index = (j + secret_num) % len(ALPHABET)
                result += ALPHABET[index]
                break
    return result


def get_secret_num():
    """
    get the secret number and return
    """
    return int(input('Secret number:'))


def get_ciphered_message():
    """
    get the ciphered message and return
    """
    return str(input('Ciphered message:')).upper()


def print_result(result):
    """
    Print the deciphered message
    """
    print("=============================")
    print(f"Deciphered_message: {result}")
    print("=============================")


#  DO NOT EDIT THE CODE BELOW THIS LINE  #
if __name__ == '__main__':
    main()
