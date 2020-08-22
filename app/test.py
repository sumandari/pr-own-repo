import pytest

from kalkulator import penjumlahan, pengurangan


def test_penjumlahan():
    assert penjumlahan(1, 2) == 3


def test_pengurangan():
    assert pengurangan(2,1) == 1
