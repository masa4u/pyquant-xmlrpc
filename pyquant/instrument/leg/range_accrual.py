from abc import ABCMeta, abstractmethod

from pyquant.instrument.leg.leg import LegAbstract
from pyquant.instrument.leg.reference import ReferenceSingle


class RangeAccrualLeg(LegAbstract):
    __metaclass__ = ABCMeta
    class Meta:
        reference_size = None

    @abstractmethod
    def __init__(self):
        pass


class SingleRangeAccrualLeg(RangeAccrualLeg):
    class Meta:
        reference = ReferenceSingle

    @abstractmethod
    def __init__(self, reference):
        self.Meta.reference = self.Meta.reference(reference)


class DualRangeAccrualLeg(RangeAccrualLeg):
    '''
    Dual Range Accrual :
    '''
    class Meta:
        reference_size = 2

class TripleRangeAccrualLeg(RangeAccrualLeg):
    class Meta:
        reference_size = 3

if __name__ == '__main__':
    print SingleRangeAccrualLeg()