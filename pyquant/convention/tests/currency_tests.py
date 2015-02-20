import unittest
from pyquant.convention.currency import Currency


class TestCurrency(unittest.TestCase):
    def test_currency(self):
        self.assertTrue(Currency.KRW is Currency.KRW)

    def test_fail(self):
        self.assertTrue(False)