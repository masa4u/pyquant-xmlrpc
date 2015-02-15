from abc import ABCMeta, abstractmethod, abstractproperty
from enum import Enum


class MarketDataType(Enum):
    Single = 0
    Curve = 1
    Matrix = 2


class MarketDataAbstract():
    __metaclass__ = ABCMeta

    class Meta:
        data_type = None

    @property
    def data_type(self):
        return self.Meta.data_type

    @abstractproperty
    def value(self):
        return 'Should never get here'

    @abstractmethod
    def __repr__(self):
        return '<%s>' % (self.__class__.__name__)

    @abstractmethod
    def iterator(self):
        yield None