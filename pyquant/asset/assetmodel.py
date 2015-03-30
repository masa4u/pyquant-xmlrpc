from pyquant.asset.asset import Asset


class AssetModel(Asset):

    def __init__(self, asset_type, currency, model):
        # Asset.__init__(self, asset_type, currency)
        super(AssetModel, self).__init__(asset_type, currency)

    def __repr__(self):
        return '<%s: type=%s, Currency:%s>' % (self.__class__.__name__, self.asset_type, self.currency)

if __name__ == '__main__':
    from pyquant.convention.currency import Currency
    from pyquant.asset.asset import AssetType
    asset_model = AssetModel(AssetType.IR, Currency.KRW, 'dummy')
    print asset_model

