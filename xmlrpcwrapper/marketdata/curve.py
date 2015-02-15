from abc import ABCMeta
from xmlrpcwrapper.marketdata.marketdata import MarketDataAbstract, MarketDataType


class MarketDataCurve(MarketDataAbstract):
    __metaclass__ = ABCMeta

    class Meta:
        data_type = MarketDataType.Curve

    def __init__(self, x_type=float, y_type=float):
        self._type_x = x_type
        self._type_y = y_type
        self._x = []
        self._y = []
        self._value = ()

    @property
    def value(self):
        if self._x is []:
            raise Exception('init first')
        return zip(self.x, self.y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def type_x(self):
        return self._type_x

    @property
    def type_y(self):
        return self._type_y

    def append(self, x_value, y_value):
        # print x_value
        # print self.type_x
        if isinstance(x_value, self.type_x) and isinstance(y_value, self.type_y):
            try:
                idx = self._x.index(x_value)
                raise Exception('Already assigned on %d' % idx)
            except ValueError:
                self._x.append(x_value)
                self._y.append(y_value)

    # specific for curve
    @property
    def size(self):
        return len(self.x)

    def __repr__(self):
        u = '<%s: (%s, %s)>\n' % (self.__class__.__name__, self.type_x.__name__, self.type_y.__name__)
        u += 'size = %d\n' % self.size
        u += 'value = %s\n' % str(self.value)

        return u

    def iterator(self):
        for value in self.value:
            yield value

    def remove_value_from_index(self, index):
        self.x.pop(index)
        self.y.pop(index)

    def remove_value_from_x(self, x):
        index = self.x.find(x)
        self.x.pop(index)
        self.y.pop(index)

if __name__ == '__main__':
    curve = MarketDataCurve()
    print curve.data_type
    print curve.type_x

    # print curve.value
    curve.append(1.0, 2.0)
    # curve.append(1.0, 2.0)
    curve.append(2.0, 2.0)
    print curve

    for idx, x in enumerate(curve.iterator()):
        print idx, x