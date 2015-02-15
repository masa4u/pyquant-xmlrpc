from abc import ABCMeta, abstractmethod
from xmlrpcwrapper.marketdata.marketdata import MarketDataAbstract, MarketDataType


class MarketDataSingle(MarketDataAbstract):
    __metaclass__ = ABCMeta

    class Meta:
        data_type = MarketDataType.Single

    def __init__(self):
        self._value = 0.0
    @property
    def value(self):
        return self._value

    def __repr__(self):
        return '<%s>' % (self.__class__.__name__)

    @property
    def iterator(self):
        yield self.value