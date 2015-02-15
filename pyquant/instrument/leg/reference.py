from abc import ABCMeta, abstractmethod, abstractproperty
from enum import Enum


class ReferenceType(Enum):
    Single = 0
    Spread = 1


class ReferenceAbstract():
    __metaclass__ = ABCMeta

    class Meta:
        reference = []

    @abstractproperty
    def reference(self):
        return ''


class ReferenceSingle(ReferenceAbstract):

    def __init__(self, reference):
        self._reference

    @property
    def reference(self):
        return self._reference


class ReferenceSpread(ReferenceAbstract):
    def __init__(self, reference1, reference2):
        self._reference = [reference1, reference2]

    @property
    def reference(self):
        return self._reference
