from pyquant.product.product import ProductAbstract

from pyquant.convention.currency import Currency
from pyquant.instrument.optional import OptionalCallable, OptionalNote, OptionalRisky
from pyquant.instrument.single_range_accrual import SingleRangeAccrualInstrument


class CallableRangeAccrual(ProductAbstract, SingleRangeAccrualInstrument, OptionalCallable, OptionalNote):

    def __init__(self, currency, reference):

        self._payment_currency = currency
        SingleRangeAccrualInstrument.__init__(self, reference)

if __name__ == '__main__':
    product = CallableRangeAccrual(Currency.KRW, 'KRW CD91')
    print product.legs[0].references
    print product
    # print product.Meta.leg