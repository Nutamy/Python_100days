# alphabet = [',', "'", '?', ' ', 'a', '0', 'b', '1', 'c', '2', 'd', '9', 'e', '3', 'f', '"', 'g', 'h', '.', 'i',
#             '4', 'j', '5', 'k', 'l', '6', 'm', 'n', '7', '!', 'o', '8', 'p', 'q', 'r', 's', 't', 'u', 'v', '%', 'w',
#             'x', 'y', 'z']
import string

box = " "
box += string.ascii_letters
box += string.digits
box += string.punctuation
alphabet = []
for symbol in box:
    alphabet.append(symbol)


def encode(text, shift):
    new_text = ""
    for letter in text:
        idx = alphabet.index(letter)
        if idx + shift >= len(alphabet):
            new_idx = idx + shift - len(alphabet)
        else:
            new_idx = idx + shift
        new_letter = alphabet[new_idx]
        new_text += new_letter
    return new_text


def decode(text, shift):
    new_text = ""
    for letter in text:
        idx = alphabet.index(letter)
        if idx - shift < 0:
            new_idx = len(alphabet) - (shift - idx)
        else:
            new_idx = idx - shift
        new_letter = alphabet[new_idx]
        new_text += new_letter
    return new_text


def cipher_mashine(direction, text, shift):
    if shift > len(alphabet):
        shift = shift % len(alphabet)
    if direction == "encode":
        encode(text, shift)
    else:
        decode(text, shift)