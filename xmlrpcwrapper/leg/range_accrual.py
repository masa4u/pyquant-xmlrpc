from abc import ABCMeta
from xmlrpcwrapper.leg.leg import LegAbstract


class RangeAccrualLeg(LegAbstract):
    __metaclass__ = ABCMeta


class SingleRangeAccrualLeg(RangeAccrualLeg):
    class Meta:
        leg_size = 1

class DualRangeAccrualLeg(RangeAccrualLeg):
    class Meta:
        leg_size = 2

class TripleRangeAccrualLeg(RangeAccrualLeg):
    class Meta:
        leg_size = 3