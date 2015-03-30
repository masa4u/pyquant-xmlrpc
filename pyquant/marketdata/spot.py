from pyquant.marketdata.marketdata import MarketDataType
from pyquant.marketdata.single import MarketDataSingle


class MarketDataSpot(MarketDataSingle):
    def __init__(self):
        super(MarketDataSpot, self).__init__()

print MarketDataSpot().data_type
print MarketDataSpot().value

if __name__ == '__main__':
    from pyquant.marketdata.libor import MarketDataLibor
    from pyquant.marketdata.cmt import MarketDataCMT
    from pyquant.marketdata.cms import MarketDataCMS
    from pyquant.marketdata.curve import MarketDataCurve

    if issubclass(MarketDataSpot, MarketDataSingle):
        print 'yes'

    single_data_list = [MarketDataSpot, MarketDataLibor, MarketDataCMT, MarketDataCurve]

    for c in single_data_list:
        print c.__name__, issubclass(c, MarketDataSingle)
