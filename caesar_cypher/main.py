"""Main module"""
from caesar_cypher import (  # type: ignore
    decode_vigenere,
    get_indices_difference,
    get_key_length,
    get_user_input,
)


def main() -> None:
    print("Enter key length: ", end="")
    key_len = get_key_length()
    print("Enter plain text: ", end="")
    regular_text = get_user_input()
    print("Enter encoded text: ", end="")
    encoded_text = get_user_input()
    print("Enter target message to decode: ", end="")
    target_message = get_user_input()

    new_indices = get_indices_difference(regular_text, encoded_text)

    # Slice indices up to max key_len
    new_indices_up_to_key = new_indices[:key_len]

    print(decode_vigenere(target_message, new_indices_up_to_key))


if __name__ == "__main__":
    main()
