"""Caesar Cypher module"""
# Write your code here
import string


def get_user_input() -> str:
    """
    Get input from user.

    :return: str
    """
    return input()


def decode_text(test_input: str, shift_modifier: int) -> str:
    """
    Decode cypher text based on right shift modifier.

    :param test_input: encoded text
    :param shift_modifier: shift modifier
    :return: decoded text
    """
    new = []
    for char in test_input.split():
        char_idx = string.ascii_lowercase.index(char)
        mod_idx = (char_idx + shift_modifier) % 26
        new.append(string.ascii_lowercase[mod_idx])

    return "".join(new).replace("x", " ")


def convert_to_int(user_input: str) -> list[int]:
    """
    Convert str numbers to integer.

    :param user_input: encoded text
    :return: list of numbers
    """
    return [int(num) for num in user_input.split()]


def convert_to_ascii(numbers: list[int]) -> str:
    """
    Convert list of integers to ASCII characters.

    :param numbers:
    :return: ASCII text
    """
    return "".join([string.ascii_lowercase[num] for num in numbers])


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
