from enum import Enum, unique


@unique
class Currency(Enum):
    KRW = 0
    USD = 1
    JPY = 2
    EUR = 3

    def __add__(self, other):
        return CurrencyPair(self, other)

    def __repr__(self):
        return '<Currency: %s>' % self.name

    def __str__(self):
        return self.name


class CurrencyPair(object):
    '''
    Currency Pair such as USDKRW, KRWUSD
    XXXYYY : foreign + domestic
    '''
    def __init__(self, domestic, foreign):
        self._domestic = domestic
        self._foreign = foreign

    @property
    def domestic(self):
        return self._domestic

    @property
    def foreign(self):
        return self._foreign

    @property
    def code(self):
        return self.domestic.name + self.foreign.name

    def __repr__(self):
        return '<CurrencyPair: %s>' % self.code

    # def __str__(self):
    #     return self.code
