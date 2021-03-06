from pyquant.instrument.instrument import InstrumentAbstract
from pyquant.instrument.leg.range_accrual import SingleRangeAccrualLeg


class SingleRangeAccrualInstrument(InstrumentAbstract):
    def __init__(self, reference):
        super(SingleRangeAccrualInstrument, self).__init__()
        leg = SingleRangeAccrualLeg(reference)
        self._legs = [leg]

    def instrument_type(self):
        return 'SingleRangeAccrual'

if __name__ == '__main__':
    import unittest
    from pyquant.tests.utils import test_all_file_from_inspection
    test_all_file_from_inspection('pyquant.instrument.single_range_accrual')
    unittest.main()
    # instrument = InstrumentSingleRangeAccrual('KRW CD91')
    # print instrument.legs
    # print instrument.leg_size
    # print instrument.legs[0].reference_size
    # print instrument.legs[0].references
    # print instrument