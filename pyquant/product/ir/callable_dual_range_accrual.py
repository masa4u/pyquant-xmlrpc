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
    from pyquant.tests.utils import test_all_file_from_inspection
    test_all_file_from_inspection('pyquant.convention.currency')
    test_all_file_from_inspection('pyquant.instrument.single_range_accrual')

    unittest.main()
    product = CallableDualRangeAccrual(Currency.KRW, 'KRW CD91', 'KRW KTB3m')
    print product.is_callable
    print product.is_note
    print product.is_swap
    print product.is_option
    print product.legs
    print product
    print product.get_full_name()