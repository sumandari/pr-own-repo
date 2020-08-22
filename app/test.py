import pytest

from kalkulator import penjumlahan, pengurangan, perkalian


def test_penjumlahan():
    assert penjumlahan(1, 2) == 3


def test_pengurangan():
    assert pengurangan(2,1) == 1


def test_perkalian():
    assert perkalian(2, 3) == 6
