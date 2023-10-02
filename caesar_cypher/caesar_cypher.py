"""Hello module"""
import string


def get_user_input() -> str:
    return input()


def convert_to_int(user_input: str) -> list[int]:
    return [int(num) for num in user_input.split()]


def convert_to_ascii(numbers: list[int]) -> str:
    return "".join([string.ascii_lowercase[num] for num in numbers])
