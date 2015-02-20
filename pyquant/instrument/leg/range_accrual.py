from abc import ABCMeta, abstractmethod, abstractproperty

from pyquant.instrument.leg.leg import LegAbstract, LegType
from pyquant.instrument.leg.reference import ReferenceSingle, ReferenceSpread


class RangeAccrualLeg(LegAbstract):

    @property
    def leg_type(self):
        return LegType.RangeAccrualLeg

    def __repr__(self):
        return '<RangeAccrualLeg(%s)>' % str(self.references)


class SingleRangeAccrualLeg(RangeAccrualLeg):
    def __init__(self, reference):
        self._references = []
        super(SingleRangeAccrualLeg, self).__init__()
        self.references.append(ReferenceSingle(reference))


class SpreadRangeAccrualLeg(RangeAccrualLeg):
    def __init__(self, reference1, reference2):
        self._references = []
        super(SpreadRangeAccrualLeg, self).__init__()
        self.references.append(ReferenceSpread(reference1, reference2))


if __name__ == '__main__':
    print SingleRangeAccrualLeg('KRW CD91').reference_size
    print SingleRangeAccrualLeg('KRW CD91').references
    print SingleRangeAccrualLeg('KRW CD91').leg_type
    print SingleRangeAccrualLeg('KRW CD91')

    print SpreadRangeAccrualLeg('KRW CD91', 'KTB 3m').reference_size
    print SpreadRangeAccrualLeg('KRW CD91', 'KTB 3m').references
    print SpreadRangeAccrualLeg('KRW CD91', 'KTB 3m').leg_type