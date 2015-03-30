from pyquant.instrument.instrument import InstrumentAbstract
from pyquant.instrument.leg.range_accrual import SingleRangeAccrualLeg, SpreadRangeAccrualLeg


class TripleRangeAccrualInstrument(InstrumentAbstract):
    def __init__(self, reference1, reference2, reference3):
        super(TripleRangeAccrualInstrument, self).__init__()

        single_leg1 = SingleRangeAccrualLeg(reference1)
        single_leg2 = SingleRangeAccrualLeg(reference2)
        single_leg3 = SingleRangeAccrualLeg(reference3)
        self._legs = [single_leg1, single_leg2, single_leg3]

    @property
    def instrument_type(self):
        return 'TripleRangeAccrual'

if __name__ == '__main__':
    instrument = TripleRangeAccrualInstrument('KRW CD91', 'KRW CD91', 'KTB 3m')
    print instrument.legs
    print instrument.leg_size
    print instrument.legs[0].reference_size
    print instrument.legs[0].references
    print instrument