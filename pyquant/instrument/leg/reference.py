from abc import ABCMeta, abstractmethod, abstractproperty
from enum import Enum


class ReferenceType(Enum):
    Single = 0
    Spread = 1


class ReferenceAbstract():
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        self._reference = []

    @property
    def reference(self):
        return self._reference

    @abstractproperty
    def reference_type(self):
        return ''

    def reference_size(self):
        return len(self.reference)

    def __repr__(self):
        return 'Reference(%s)' % str(self._reference)


class ReferenceSingle(ReferenceAbstract):

    def __init__(self, reference):
        super(ReferenceSingle, self).__init__()
        self._reference = [reference]

    @property
    def reference_type(self):
        return ReferenceType.Single


class ReferenceSpread(ReferenceAbstract):
    def __init__(self, reference1, reference2):
        super(ReferenceSingle, self).__init__()
        self._reference = [reference1, reference2]

    @property
    def reference(self):
        return self._reference

    @property
    def reference_type(self):
        return ReferenceType.Spread