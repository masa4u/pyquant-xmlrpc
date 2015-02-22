import unittest
from pyquant.instrument.leg.cashflow.cashflow import CashflowSingle, CashflowNoReset


class TestCashflow(unittest.TestCase):
    def test_single_cashflow(self):
        cashflow = CashflowSingle('2015-01-01', '2015-02-02', '2015-03-04', '2013-01-01')

        print cashflow
        # CashflowSingle()
        print cashflow.start_date
        print cashflow.end_date
        print cashflow.pay_date
        print cashflow.reset_date

    def test_cashflow_noreset(self):
        cashflow = CashflowNoReset('2015-01-01', '2015-02-02', '2015-03-04')
        print cashflow


if __name__ == '__main__':
    unittest.main()