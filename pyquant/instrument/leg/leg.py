from abc import ABCMeta, abstractproperty


class LegAbstract():
    __metaclass__ = ABCMeta

    class Meta:
        reference_size = None

    # @abstractproperty
    # def cashflows(self):
    #     return ''
