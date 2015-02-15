from pyquant.instrument.instrument import InstrumentAbstract


class SwapInstrument(InstrumentAbstract):

    class Meta:
        legs = []

    @property
    def leg_size(self):
        return 2