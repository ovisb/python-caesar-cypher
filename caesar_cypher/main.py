"""Main module"""
from .caesar_cypher import (  # type: ignore
    convert_to_ascii,
    convert_to_int,
    get_user_input,
)


def main() -> None:
    user_input = get_user_input()
    numbers = convert_to_int(user_input)

    print(convert_to_ascii(numbers))


if __name__ == "__main__":
    main()
