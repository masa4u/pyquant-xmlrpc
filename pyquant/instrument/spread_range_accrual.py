from pyquant.instrument.instrument import InstrumentAbstract
from pyquant.instrument.leg.range_accrual import SpreadRangeAccrualLeg


class SpreadRangeAccrualInstrument(InstrumentAbstract):
    def __init__(self, reference1, reference2):
        super(SpreadRangeAccrualInstrument, self).__init__()
        leg = SpreadRangeAccrualLeg(reference1, reference2)
        self._legs = [leg]

    def instrument_type(self):
        return 'SpreadRangeAccrual'

if __name__ == '__main__':
    instrument = SpreadRangeAccrualInstrument('KRW CD91', 'KTB 3m')
    print instrument.legs
    print instrument.leg_size
    print instrument.legs[0].reference_size
    print instrument.legs[0].references
    print instrument