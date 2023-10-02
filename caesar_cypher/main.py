"""Main module"""
from caesar_cypher import convert_to_cypher, get_user_input  # type: ignore


def main() -> None:
    left_shift = 3
    user_input = get_user_input()
    print(convert_to_cypher(user_input, left_shift))


if __name__ == "__main__":
    main()
