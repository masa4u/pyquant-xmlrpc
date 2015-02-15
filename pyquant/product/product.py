from abc import ABCMeta


class ProductAbstract():
    __metaclass__ = ABCMeta

    class Meta:
        instrument = None
        leg = None

    @property
    def payment_currency(self):
        return self._payment_currency

    def __init__(self, currency):
        self.payment_currency = currency

    def __repr__(self):
        return '<%s(%s)>' % (self.__class__.__name__, self.payment_currency)