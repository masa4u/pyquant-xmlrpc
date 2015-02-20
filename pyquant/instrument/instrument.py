from abc import ABCMeta, abstractproperty, abstractmethod


class InstrumentAbstract():
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        self._legs = []

    @property
    def leg_size(self):
        return len(self.legs)

    @property
    def legs(self):
        return self._legs

    @abstractmethod
    def instrument_type(self):
        return ''

    def __repr__(self):
        return '<Instrument(%s)>' % ', '.join(map(lambda x: str(x), self.legs))