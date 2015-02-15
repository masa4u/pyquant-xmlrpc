from xmlrpcwrapper.instrument.instrument import InstrumentAbstract


class SwapInstrument():
    __metaclass__ = InstrumentAbstract

    class Meta:
        legs = []