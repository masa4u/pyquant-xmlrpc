from pyquant.instrument.instrument import InstrumentAbstract


class OptionInstrument(InstrumentAbstract):

    class Meta:
        legs = []

    @property
    def leg_size(self):
        return 1