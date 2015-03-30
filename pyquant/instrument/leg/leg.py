from abc import ABCMeta, abstractproperty, abstractmethod
from enum import Enum

class LegType(Enum):
    FixedLeg = 1
    FloatLeg = 2
    OptionLeg = 3
    RangeAccrualLeg = 4
    FloaterLeg = 5
    Steepener = 6


class LegAbstract():
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        self._references = []

    @abstractproperty
    def leg_type(self):
        return None

    @property
    def references(self):
        return self._references

    @property
    def reference_size(self):
        return len(self._references)

    def __repr__(self):
        return '<Leg(%s)>' % str(self._references)