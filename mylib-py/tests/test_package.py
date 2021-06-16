import pytest

from mylib import add_one, __version__


def test_version() -> None:
    assert __version__ == "0.1.0"


def test_add_one() -> None:
    assert add_one(10) == 11
    assert add_one(-10) == -9
