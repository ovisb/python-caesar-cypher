import io

import pytest

from caesar_cypher.caesar_cypher import (
    convert_to_ascii,
    convert_to_cypher,
    convert_to_int,
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


@pytest.mark.parametrize(
    "test_inp_, expected",
    [
        ("e b i i l", "hello"),
        ("c o f b k a", "friend"),
        ("h b v t l o a", "keyword"),
        ("y r q q b o p z l q z e", "butterscotch"),
    ],
)
def test_convert_to_cypher(test_inp_, expected):
    assert convert_to_cypher(test_inp_) == expected
