"""Main module"""
from caesar_cypher import decode_text, find_shift, get_user_input  # type: ignore


def main() -> None:
    encoded_text = get_user_input()
    text_to_decode = get_user_input()
    shift = find_shift(encoded_text)
    print(shift)
    print(decode_text(text_to_decode, shift))


if __name__ == "__main__":
    main()
