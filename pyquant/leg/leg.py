from abc import ABCMeta, abstractproperty




class LegAbstract():
    __metaclass__ = ABCMeta

    class Meta:
        leg_size = None

    @abstractproperty
    def cashflows(self):
        return ''
