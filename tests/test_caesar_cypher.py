import io

import pytest

from caesar_cypher.caesar_cypher import (
    convert_to_ascii,
    convert_to_int,
    decode_caesar,
    decode_vigenere,
    find_shift,
    get_indices_difference,
    get_key_length,
    get_user_input,
)


@pytest.mark.parametrize(
    "test_inp_, expected", [("0 1 2", "0 1 2"), ("a b c", "a b c")]
)
def test_input(monkeypatch, test_inp_, expected):
    monkeypatch.setattr("sys.stdin", io.StringIO(test_inp_))
    assert get_user_input() == expected


@pytest.mark.parametrize(
    "test_inp_, expected", [("0 1 2", [0, 1, 2]), ("0", [0]), ("", [])]
)
def test_convert_int(test_inp_, expected):
    assert convert_to_int(test_inp_) == expected


@pytest.mark.parametrize(
    "test_inp_, expected",
    [
        ([0, 1, 2], "abc"),
        ([7, 4, 11, 11, 14], "hello"),
        ([2, 7, 4, 4, 18, 4, 2, 0, 10, 4], "cheesecake"),
    ],
)
def test_convert_to_ascii(test_inp_, expected):
    assert convert_to_ascii(test_inp_) == expected


def test_find_shift():
    text = "r d c r t r c r f i j c x t r j c g z y y j w x h t y h m c u n j"
    assert find_shift(text) == 21


def test_find_not_find_shift():
    text = "r d c r t r c r f t b c x a r x x h a y y j w x a a y h m c u n j"
    assert find_shift(text) == 0


@pytest.mark.parametrize(
    "test_inp_, expected",
    [
        (("r r r", 21), "mmm"),
        (("x r j q q x c y f x y d", 21), "smells tasty"),
        (
            ("u q j f x j c h t r j c y w d c f c x q n h j", 21),
            "please come try a slice",
        ),
        (("r r r", 0), "rrr"),
    ],
)
def test_decode_caesar(test_inp_, expected):
    test, shift = test_inp_
    assert decode_caesar(test, shift) == expected


@pytest.mark.parametrize(
    "test_inp_, expected",
    [
        ("1", 1),
        ("2", 2),
        ("3", 3),
    ],
)
def test_get_key_length(monkeypatch, test_inp_, expected):
    monkeypatch.setattr("sys.stdin", io.StringIO(test_inp_))
    assert get_key_length() == expected


@pytest.mark.parametrize(
    "test_input_, expected",
    [
        (("e a s y", "e a s y"), [0, 0, 0, 0]),
        (("l e s s x e a s y", "m f t t y f b t z"), [1, 1, 1, 1, 1, 1, 1, 1, 1]),
        (("a b c d", "a c c e"), [0, 1, 0, 1]),
        (("t e s t", "d i q d"), [-16, 4, -2, -16]),
        (("", ""), []),
    ],
)
def test_indices_differences(test_input_, expected):
    plain, plain_encoded = test_input_
    assert get_indices_difference(plain, plain_encoded) == expected


@pytest.mark.parametrize(
    "test_input_, expected",
    [
        (("t h e x k e y w o r d x w a s x a", [0, 0, 0, 0], 1), "the keyword was a"),
        (
            ("u i f y l f z x p s e y x b t y c", [1, 1, 1, 1, 1, 1, 1, 1, 1], 1),
            "the keyword was b",
        ),
        (
            ("t i i t x t h p u m d y l p o l x g a n i m i b r", [0, 1, 0, 1], 2),
            "this should look familiar",
        ),
        (("c i a b i r h x c c x", [-16, 4, -2, -16], 3), "secret test"),
        (("", [], 1), ""),
    ],
)
def test_decode_vigenere(test_input_, expected):
    target_message, indices, key_len = test_input_
    assert decode_vigenere(target_message, indices[:key_len]) == expected
