from pyquant.instrument.note import NoteInstrument
from pyquant.product.product import ProductAbstract
from pyquant.convention.currency import Currency


class CallableRangeAccrual(ProductAbstract):
    class Meta:
        instrument = NoteInstrument
        # leg = SingleRangeAccrualLeg

    def __init__(self, currency):

        self._payment_currency = currency


if __name__ == '__main__':
    product = CallableRangeAccrual(Currency.KRW)
    print product.Meta.instrument
    # print product.Meta.leg