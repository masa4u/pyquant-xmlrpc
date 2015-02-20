from pyquant.product.product import ProductAbstract

from pyquant.convention.currency import Currency

from pyquant.instrument.optional import OptionalCallable, OptionalNote, OptionalRisky
from pyquant.instrument.dual_range_accrual import InstrumentDualRangeAccrual


class CallableDualRangeAccrual(ProductAbstract, InstrumentDualRangeAccrual,
                               OptionalCallable, OptionalNote, OptionalRisky):

    def __init__(self, currency, reference1, reference2):
        self._payment_currency = currency
        InstrumentDualRangeAccrual.__init__(self, reference1, reference2)

if __name__ == '__main__':
    import unittest

    from pyquant.convention.tests.currency_tests import TestCurrency
    from pyquant.instrument.tests.single_range_accrual_tests import TestSingleRangeAccrual

    unittest.main()
    product = CallableDualRangeAccrual(Currency.KRW, 'KRW CD91', 'KRW KTB3m')
    print product.is_callable
    print product.is_note
    print product.is_swap
    print product.is_option
    print product.legs
    print product
    print product.get_full_name()