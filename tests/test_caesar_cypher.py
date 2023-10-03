import io

import pytest

from caesar_cypher.caesar_cypher import (
    convert_to_ascii,
    convert_to_int,
    decode_text,
    find_shift,
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
def test_decode_shift21(test_inp_, expected):
    test, shift = test_inp_
    assert decode_text(test, shift) == expected
