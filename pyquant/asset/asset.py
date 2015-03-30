from enum import Enum
from abc import ABCMeta, abstractmethod

class AssetType(Enum):
    IR = 0
    EQ = 1
    FX = 2
    COM = 3

# IR, EQ, FX, COM
class Asset():
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, asset_type, currency):
        self._asset_type = asset_type
        self._currency = currency

    @property
    def asset_type(self):
        return self._asset_type

    @property
    def currency(self):
        return self._currency

    def __repr__(self):
        return  '<Asset: type=%s, currency%s>' % ( self.asset_type, self.currency)


if __name__ == '__main__':
    from pyquant.convention.currency import Currency
    asset = Asset(AssetType.IR, Currency.KRW)
    print asset
