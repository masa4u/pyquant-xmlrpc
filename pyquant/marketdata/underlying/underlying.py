from pyquant.marketdata.marketdata import MarketDataType


class UnderlyingMap(dict):
    def __init__(self):
        pass

    def __repr__(self):
        return '<UnderlyingMap: %s>' % self.keys()

    def append(self, underlying):
        if isinstance(underlying, Underlying) is False:
            raise Exception('Error')

        self[underlying.ins] = underlying


class Underlying(object):
    def __init__(self, asset_type, market_data_class, ins):
        self.asset_type = asset_type
        self.market_data_class = market_data_class
        self.ins = ins

    def __repr__(self):
        return '<Underlying: %s(%s, %s)>' % (self.ins, self.asset_type, self.market_data_class.__name__)

    def __str__(self):
        return '<%s>' % self.ins

if __name__ == '__main__':
    from pyquant.asset.asset import AssetType
    from pyquant.marketdata.libor import MarketDataLibor
    und_map = UnderlyingMap()

    krw_cd91 = Underlying(AssetType.IR, MarketDataLibor, 'KRW CD91')

    und_map.append(krw_cd91)

    print und_map
    print und_map['KRW CD91']
