from pyquant.product.product import ProductAbstract
from pyquant.convention.currency import Currency
from pyquant.instrument.optional import OptionalCallable, OptionalNote, OptionalRisky
from pyquant.instrument.triple_range_accrual import InstrumentTripleRangeAccrual


class CallableTripleRangeAccrual(ProductAbstract, InstrumentTripleRangeAccrual, OptionalCallable, OptionalNote):

    def __init__(self, currency, reference1, reference2, reference3):
        self._payment_currency = currency
        InstrumentTripleRangeAccrual.__init__(self, reference1, reference2, reference3)

if __name__ == '__main__':
    product = CallableTripleRangeAccrual(Currency.KRW, 'USD Libor 3m', 'KRW CD91', 'KTB 3m')
    print product.legs
    print product.legs[0].references
    print product.get_full_name()