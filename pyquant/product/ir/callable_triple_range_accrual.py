from pyquant.instrument.note import NoteInstrument
from pyquant.leg.range_accrual import TripleRangeAccrualLeg
from pyquant.product.product import ProductAbstract
from pyquant.convention.currency import Currency


class CallableTripleRangeAccrual(ProductAbstract):
    class Meta:
        instrument = NoteInstrument
        leg = TripleRangeAccrualLeg

    def __init__(self, currency):
        self._payment_currency = currency


if __name__ == '__main__':
    print CallableTripleRangeAccrual(Currency.KRW)