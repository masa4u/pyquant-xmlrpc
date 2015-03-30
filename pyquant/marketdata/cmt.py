from pyquant.marketdata.marketdata import MarketDataType
from pyquant.marketdata.single import MarketDataSingle


class MarketDataCMT(MarketDataSingle):
    def __init__(self):
        super(MarketDataCMT, self).__init__()

print MarketDataCMT().data_type
print MarketDataCMT().value
print MarketDataCMT