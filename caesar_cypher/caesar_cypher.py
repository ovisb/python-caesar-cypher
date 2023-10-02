"""Hello module"""
import string


def get_user_input() -> str:
    return input()


def convert_to_cypher(test_input: str, shift_modifier: int = 3) -> str:
    new = []
    for char in test_input.split():
        char_idx = string.ascii_lowercase.index(char)
        mod_idx = (char_idx + shift_modifier) % 26
        new.append(string.ascii_lowercase[mod_idx])

    return "".join(new)


def convert_to_int(user_input: str) -> list[int]:
    return [int(num) for num in user_input.split()]


def convert_to_ascii(numbers: list[int]) -> str:
    return "".join([string.ascii_lowercase[num] for num in numbers])
