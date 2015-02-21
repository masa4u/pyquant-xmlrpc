from pyquant.instrument.instrument import InstrumentAbstract
from pyquant.instrument.leg.range_accrual import SpreadRangeAccrualLeg


class InstrumentSpreadRangeAccrual(InstrumentAbstract):
    def __init__(self, reference1, reference2):
        leg = SpreadRangeAccrualLeg(reference1, reference2)
        self._legs = [leg]

    def instrument_type(self):
        return 'SpreadRangeAccrual'

if __name__ == '__main__':
    instrument = InstrumentSpreadRangeAccrual('KRW CD91', 'KTB 3m')
    print instrument.legs
    print instrument.leg_size
    print instrument.legs[0].reference_size
    print instrument.legs[0].references
    print instrument