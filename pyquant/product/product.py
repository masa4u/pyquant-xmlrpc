from abc import ABCMeta

from pyquant.instrument.instrument import InstrumentAbstract
from pyquant.instrument.leg.leg import LegAbstract
from pyquant.instrument.optional import OptionalCallableAbstract, OptionalNoteSwapAbstract, OptionalRiskyAbstract


class ProductAbstract(InstrumentAbstract, OptionalCallableAbstract, OptionalNoteSwapAbstract, OptionalRiskyAbstract):
    __metaclass__ = ABCMeta

    class Meta:
        model = None
        numerical = None

    @property
    def payment_currency(self):
        return self._payment_currency

    def __init__(self, currency):
        self.payment_currency = currency

    def __repr__(self):
        return '<%s(%s)>' % (self.__class__.__name__, self.payment_currency)

    def get_full_name(self):
        instrument_type = []
        rlt = ''
        if self.is_risky:
            rlt += 'CreditLinked'
        rlt += 'Callable' if self.is_callable else ''
        if self.is_note:
            instrument_type.append('Note')
        if self.is_swap:
            instrument_type.append('Swap')
        if self.is_option:
            instrument_type.append('Option')

        rlt += self.instrument_type
        if len(instrument_type) > 0:
            rlt += ','.join(instrument_type)

        return rlt