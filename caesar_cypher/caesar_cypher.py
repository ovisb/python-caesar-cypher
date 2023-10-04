"""Caesar Cypher project
Can decode using both Caesar and adapted Vigenere
"""
# Write your code here
import string


def get_indices_difference(regular_text: str, encoded_text: str) -> list[int]:
    """
    Get indices difference from subtracting
    each character position from encoded_text
    to each character position from regular_text

    :param regular_text: plain text
    :param encoded_text: same text but encoded
    :return: list of indices
    """
    regular_chars = regular_text.split()
    encoded_chars = encoded_text.split()
    diff_indices = []
    for idx, item in enumerate(regular_chars):
        regular_char_idx = string.ascii_lowercase.index(item)
        encoded_char_idx = string.ascii_lowercase.index(encoded_chars[idx])
        diff_indices.append(encoded_char_idx - regular_char_idx)

    return diff_indices

def get_user_input() -> str:
    """
    Get input from user.

    :return: str
    """
    return input()

def get_key_length() -> int:
    """
    Get key length

    :return: type cast to int
    """
    return int(input())

def decode_caesar(test_input: str, shift_modifier: int) -> str:
    """
    Decode cypher text based on Caesar Cypher using right shift modifier.

    :param test_input: encoded text
    :param shift_modifier: shift modifier
    :return: decoded text
    """
    max_letters = 26
    new = []
    for char in test_input.split():
        char_idx = string.ascii_lowercase.index(char)
        mod_idx = (char_idx + shift_modifier) % max_letters
        new.append(string.ascii_lowercase[mod_idx])

    return "".join(new).replace("x", " ")

def decode_vigenere(target_message: str, indices: list[int]) -> str:
    """
    Decode Vigenere cipher text

    :param target_message: target encoded message
    :param indices: List of indices sliced up to key len
    :return:
    """
    max_letters = 26
    target_chars = target_message.split()
    for idx, letter in enumerate(target_chars):
        pos_idx = idx % len(indices) # alternate indices
        new_pos = (max_letters + string.ascii_lowercase.index(letter) - indices[pos_idx]) % max_letters
        target_chars[idx] = string.ascii_lowercase[new_pos]

    return "".join(target_chars).replace("x", " ")



def convert_to_int(user_input: str) -> list[int]:
    """
    Convert str numbers to integer.

    :param user_input: encoded text
    :return: list of numbers
    """
    return [
        int(num)
        for num in user_input.split()
    ]

def convert_to_ascii(numbers: list[int]) -> str:
    """
    Convert list of integers to ASCII characters.

    :param numbers:
    :return: ASCII text
    """
    return "".join([
        string.ascii_lowercase[num]
        for num in numbers
    ])

def find_shift(user_input: str) -> int:
    """
    Find shift modifier from encoded text through 'secret word'.

    :param user_input: encoded text
    :return: shift number if secret word is found or 0
    """
    max_letters = 26
    letters = user_input.split()
    for shift in range(1, max_letters):
        for idx, letter in enumerate(letters):
            char_idx = string.ascii_lowercase.index(letter)
            mod_idx = (char_idx + shift) % max_letters
            letters[idx] = string.ascii_lowercase[mod_idx]
        if "butterscotch" in "".join(letters):
            return shift
        letters = user_input.split()

    return 0