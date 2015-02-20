from abc import ABCMeta, abstractmethod, abstractproperty


class OptionalCallableAbstract(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def is_callable(self):
        return False


class OptionalCallable(OptionalCallableAbstract):

    @property
    def is_callable(self):
        return True


class OptionalNonCallable(OptionalCallableAbstract):

    @property
    def is_callable(self):
        return False


class OptionalNoteSwapAbstract():
    __metaclass__ = ABCMeta

    @abstractproperty
    def is_note(self):
        pass

    @abstractproperty
    def is_swap(self):
        pass

    @property
    def is_option(self):
        return self.is_note == self.is_swap and self.is_swap is False


class OptionalNote(OptionalNoteSwapAbstract):

    @property
    def is_note(self):
        return True

    @property
    def is_swap(self):
        return False


class OptionalSwap(OptionalNoteSwapAbstract):

    @property
    def is_note(self):
        return False

    @property
    def is_swap(self):
        return True


class OptionalOption(OptionalNoteSwapAbstract):
    @property
    def is_note(self):
        return False

    @property
    def is_swap(self):
        return False


class OptionalRiskyAbstract():
    __metaclass__ = ABCMeta

    @property
    def is_risky(self):
        return False


class OptionalRisky(OptionalRiskyAbstract):

    @property
    def is_risky(self):
        return True