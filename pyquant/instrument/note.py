from pyquant.instrument.instrument import InstrumentAbstract


class NoteInstrument(InstrumentAbstract):

    class Meta:
        legs = []

    @property
    def leg_size(self):
        return 1