from pyquant.marketdata.marketdata import MarketDataAbstract, MarketDataType


class MarketDataMatrix():
    __metaclass__ = MarketDataAbstract
    class Meta:
        data_type = MarketDataType.Matrix

    def __init__(self):
        self._value = []

    @property
    def value(self):
        return self._value

    def __repr__(self):
        u = '<%s: (%s, %s)>\n' % (self.__class__.__name__, self.type_x.__name__, self.type_y.__name__)
        u += 'size = %d by %d\n' % self.size
        u += 'value = %s\n' % str(self.value)

        return u
print MarketDataMatrix().data_type
print MarketDataMatrix().value
print MarketDataMatrix