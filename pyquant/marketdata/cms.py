from pyquant.marketdata.marketdata import MarketDataType
from pyquant.marketdata.single import MarketDataSingle


class MarketDataCMS(MarketDataSingle):
    def __init__(self):
        super(MarketDataCMS, self).__init__()

print MarketDataCMS().data_type
print MarketDataCMS().value
print MarketDataCMS