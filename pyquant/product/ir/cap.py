from pyquant.instrument.option import OptionInstrument
from pyquant.product.product import ProductAbstract
from pyquant.convention.currency import Currency


class Cap(ProductAbstract):
    class Meta:
        instrument = OptionInstrument
