from pyquant.instrument.instrument import InstrumentAbstract
from pyquant.instrument.leg.range_accrual import SingleRangeAccrualLeg


class InstrumentDualRangeAccrual(InstrumentAbstract):
    def __init__(self, reference1, reference2):
        leg1 = SingleRangeAccrualLeg(reference1)
        leg2 = SingleRangeAccrualLeg(reference2)
        self._legs = [leg1, leg2]

    @property
    def instrument_type(self):
        return 'DualRangeAccrual'

if __name__ == '__main__':
    instrument = InstrumentDualRangeAccrual('KRW CD91', 'KTB 3m')
    print instrument.legs
    print instrument.leg_size
    print instrument.legs[0].reference_size
    print instrument.legs[0].references
    print instrument