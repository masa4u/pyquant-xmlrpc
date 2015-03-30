from pyquant.marketdata.marketdata import MarketDataType
from pyquant.marketdata.single import MarketDataSingle


class MarketDataLibor(MarketDataSingle):
    def __init__(self):
        super(MarketDataLibor, self).__init__()

print MarketDataLibor().data_type
print MarketDataLibor().value