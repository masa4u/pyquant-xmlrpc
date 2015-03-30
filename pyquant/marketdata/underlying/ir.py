from pyquant.marketdata.underlying.underlying import Underlying, UnderlyingMap
from pyquant.asset.asset import AssetType
from pyquant.marketdata.libor import MarketDataLibor
from pyquant.marketdata.cms import MarketDataCMS
from pyquant.marketdata.cmt import MarketDataCMT

ir_underlyings = UnderlyingMap()

#KRW
ir_underlyings['KRW CD91'] = Underlying(AssetType.IR, MarketDataLibor, 'KRW CD91')
ir_underlyings['KRW IRS 1y'] = Underlying(AssetType.IR, MarketDataCMS, 'KRW IRS 1y')
ir_underlyings['KRW IRS 2y'] = Underlying(AssetType.IR, MarketDataCMS, 'KRW IRS 2y')
ir_underlyings['KRW IRS 3y'] = Underlying(AssetType.IR, MarketDataCMS, 'KRW IRS 3y')
ir_underlyings['KRW IRS 4y'] = Underlying(AssetType.IR, MarketDataCMS, 'KRW IRS 4y')
ir_underlyings['KRW IRS 5y'] = Underlying(AssetType.IR, MarketDataCMS, 'KRW IRS 5y')
ir_underlyings['KRW IRS 7y'] = Underlying(AssetType.IR, MarketDataCMS, 'KRW IRS 7y')
ir_underlyings['KRW IRS 10y'] = Underlying(AssetType.IR, MarketDataCMS, 'KRW IRS 10y')

#KTB
ir_underlyings['KRW KTB3m'] = Underlying(AssetType.IR, MarketDataCMT, 'KRW KTB3m')
ir_underlyings['KRW KTB 1y'] = Underlying(AssetType.IR, MarketDataCMT, 'KRW KTB 1y')
ir_underlyings['KRW KTB 2y'] = Underlying(AssetType.IR, MarketDataCMT, 'KRW KTB 2y')
ir_underlyings['KRW KTB 3y'] = Underlying(AssetType.IR, MarketDataCMT, 'KRW KTB 3y')
ir_underlyings['KRW KTB 4y'] = Underlying(AssetType.IR, MarketDataCMT, 'KRW KTB 4y')
ir_underlyings['KRW KTB 5y'] = Underlying(AssetType.IR, MarketDataCMT, 'KRW KTB 5y')
ir_underlyings['KRW KTB 7y'] = Underlying(AssetType.IR, MarketDataCMT, 'KRW KTB 7y')
ir_underlyings['KRW KTB 10y'] = Underlying(AssetType.IR, MarketDataCMT, 'KRW KTB 10y')

print ir_underlyings['KRW CD91']


