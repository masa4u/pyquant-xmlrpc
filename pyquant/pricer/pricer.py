from abc import ABCMeta, abstractmethod
from enum import Enum


class PricerType(Enum):
    PIAXML = 0
    ATLComDLL = 1
    StaticDLL = 2


class PricerAbstract():
    __metaclass__ = ABCMeta

    class Meta:
        pricer_type = None

    @abstractmethod
    def to_xml(self):
        return ''

    @abstractmethod
    def from_xml(self):
        return ''
