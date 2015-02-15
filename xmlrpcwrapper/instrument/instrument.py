from abc import ABCMeta, abstractproperty


class InstrumentAbstract():
    __metaclass__ = ABCMeta

    class Meta:
        legs = []

    @abstractproperty
    def total_leg_size(self):
        return 0

    @abstractproperty
    def leg_size(self):
        return self.Meta.leg_size