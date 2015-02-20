from pyquant.instrument.instrument import InstrumentAbstract
from pyquant.instrument.leg.range_accrual import SingleRangeAccrualLeg


class InstrumentSingleRangeAccrual(InstrumentAbstract):
    def __init__(self, reference):
        leg = SingleRangeAccrualLeg(reference)
        self._legs = [leg]
    def instrument_type(self):
        return 'SingleRangeAccrual'

if __name__ == '__main__':
    instrument = InstrumentSingleRangeAccrual('KRW CD91')
    print instrument.legs
    print instrument.leg_size
    print instrument.legs[0].reference_size
    print instrument.legs[0].references
    print instrument