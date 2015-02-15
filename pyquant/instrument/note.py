from xmlrpcwrapper.instrument.instrument import InstrumentAbstract


class NoteInstrument():
    __metaclass__ = InstrumentAbstract

    class Meta:
        legs = []