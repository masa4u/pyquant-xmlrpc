from xmlrpcwrapper.marketdata.marketdata import MarketDataType
from xmlrpcwrapper.marketdata.single import MarketDataSingle


class MarketDataSpot(MarketDataSingle):
    def __init__(self):
        super(MarketDataSpot, self).__init__()

print MarketDataSpot().data_type
print MarketDataSpot().value