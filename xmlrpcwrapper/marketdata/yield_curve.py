from xmlrpcwrapper.marketdata.curve import MarketDataCurve


class Tenor:
    pass


class YieldCurve(MarketDataCurve):

    def __init__(self, currency):
        """

        :param currency: Currency
        """
        super(YieldCurve, self).__init__(Tenor, float)
        self._currency = currency

    @property
    def currency(self):
        return self._currency

    def __repr__(self):
        u = super(YieldCurve, self).__repr__()
        u += str(self.currency)
        return u

if __name__ == '__main__':
    from xmlrpcwrapper.convention.currency import Currency
    print YieldCurve(Currency.KRW)