"""Unit tests kalkulator lib."""
from kalkulator import penjumlahan, pengurangan, perkalian


class TestKalkulator:

    def test_penjumlahan(self):
        assert penjumlahan(1, 2) == 3

    def test_pengurangan(self):
        assert pengurangan(2, 1) == 1

    def test_perkalian(self):
        assert perkalian(2, 3) == 6
