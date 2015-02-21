from pyquant.instrument.instrument import InstrumentAbstract
from pyquant.instrument.leg.range_accrual import SingleRangeAccrualLeg, SpreadRangeAccrualLeg


class InstrumentSingleSpreadRangeAccrual(InstrumentAbstract):
    def __init__(self, reference1, (reference21, reference22)):
        single_leg = SingleRangeAccrualLeg(reference1)
        spread_leg = SpreadRangeAccrualLeg(reference21, reference22)
        self._legs = [single_leg, spread_leg]

    def instrument_type(self):
        return 'SingleSpreadRangeAccrual'

if __name__ == '__main__':
    instrument = InstrumentSingleSpreadRangeAccrual('KRW CD91', ('KRW CD91', 'KTB 3m'))
    print instrument.legs
    print instrument.leg_size
    print instrument.legs[0].reference_size
    print instrument.legs[0].references
    print instrument