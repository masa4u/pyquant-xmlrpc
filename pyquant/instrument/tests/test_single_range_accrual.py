import unittest
from pyquant.instrument.single_range_accrual import SingleRangeAccrualInstrument
from pyquant.instrument.leg.reference import ReferenceSingle


class TestSingleRangeAccrual(unittest.TestCase):

    def test_init(self):
        instrument = SingleRangeAccrualInstrument('KRW CD91')
        self.assertEqual(instrument.leg_size, 1)
        self.assertEqual(instrument.legs[0].reference_size, 1)
        self.assertEqual(instrument.legs[0].references[0].reference, ReferenceSingle('KRW CD91').reference)

if __name__ == '__main__':
    unittest.main()