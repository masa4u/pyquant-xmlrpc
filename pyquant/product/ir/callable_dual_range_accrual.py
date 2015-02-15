from pyquant.instrument.note import NoteInstrument
from pyquant.leg.range_accrual import DualRangeAccrualLeg
from pyquant.product.product import ProductAbstract
from pyquant.convention.currency import Currency


class CallableDualRangeAccrual(ProductAbstract):
    class Meta:
        instrument = NoteInstrument
        leg = DualRangeAccrualLeg

    def __init__(self, currency):
        self._payment_currency = currency


if __name__ == '__main__':
    print CallableDualRangeAccrual(Currency.KRW)