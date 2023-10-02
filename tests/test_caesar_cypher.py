import io

import pytest

from caesar_cypher.caesar_cypher import convert_to_ascii, convert_to_int, get_user_input


def test_input(monkeypatch):
    monkeypatch.setattr("sys.stdin", io.StringIO("0 1 2"))
    assert get_user_input() == "0 1 2"


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
