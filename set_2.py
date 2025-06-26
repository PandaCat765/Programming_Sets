def shift_letter(letter, shift):
    if letter == " ":
        return " "
    letter_position = ord(letter) - ord("A")
    shifted_position = (letter_position + shift) % 26
    shifted_letter = chr(shifted_position + ord("A")) 
    return shifted_letter


def caesar_cipher(message, shift):
    result = ""
    for letter in message:
        if letter == " ":
            result += " "
        else:
            letter_pos = ord(letter) - ord("A")
            shifted_pos = (letter_pos + shift) % 26
            shifted_letter = chr(shifted_pos + ord("A"))
            result += shifted_letter
    return result

def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " "
    letter_pos = ord(letter) - ord("A")
    letter_shifter = ord(letter_shift) - ord("A")
    shifted_pos = (letter_pos + letter_shifter) % 26
    new_letter = chr(shifted_pos + ord("A")) 
    return new_letter


def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " "
    letter_pos = ord(letter) - ord("A")
    letter_shifter = ord(letter_shift) - ord("A")
    shifted_pos = (letter_pos + letter_shifter) % 26
    new_letter = chr(shifted_pos + ord("A")) 
    return new_letter

#shift_by_letter function will be used in the vigenere function
#it’s important that the shift_by_letter function is defined if your going to complete the 
#vigenere_cipher function

def vigenere_cipher(message, key):
    key_index = 0
    result = ""
    for i in range(len(message)):
        letter = message[i]

        if key_index >= len(key):
            key_letter = key[key_index % len(key)]
        else:
            key_letter = key[key_index]

        key_index += 1
        shifted = shift_by_letter(letter, key_letter)
        result += shifted
    return result


def scytale_cipher(message, shift):
    result = ""
    while len(message) % shift != 0:
        message += "_"
    for i in range(len(message)):
        index = (i // shift) + (len(message) // shift) * (i % shift)
        result += message[index]
    return result

def scytale_decipher(message, shift):
    result = ""
    num_cols = len(message) // shift
    for i in range(len(message)):
        index = (i % num_cols) * shift + (i // num_cols)
        result += message[index]
    return result

