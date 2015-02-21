from abc import ABCMeta


class CashflowAbstract():
    __metaclass__ = ABCMeta

    def __init__(self, start_date, end_date, pay_date, resets=None):
        self._start_date = start_date
        self._end_date = end_date
        self._pay_date = pay_date
        self._resets = None

    @property
    def start_date(self):
        return self._start_date

    @property
    def end_date(self):
        return self._end_date

    @property
    def pay_date(self):
        return self._pay_date

    @property
    def resets(self):
        return self._resets


class CashflowSingle(CashflowAbstract):
    @property
    def reset_date(self):
        return self.resets[0]