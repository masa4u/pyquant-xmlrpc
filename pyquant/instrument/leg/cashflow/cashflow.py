from abc import ABCMeta


class CashflowAbstract():
    __metaclass__ = ABCMeta

    def __init__(self, start_date, end_date, pay_date, resets=None):
        """

        :type start_date: int
        :type end_date: int
        :type pay_date: int
        :type resets: list
        :return:
        """
        self._start_date = start_date
        self._end_date = end_date
        self._pay_date = pay_date
        self._resets = resets

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

    @property
    def reset_size(self):
        return len(self.resets)

    def __repr__(self):
        return '<%s: %s\t%s\t%s>' % (self.__class__.__name__,
                                     self.start_date, self.end_date, self.pay_date)


class CashflowNoReset(CashflowAbstract):
    def __init__(self, start_date, end_date, pay_date):
        CashflowAbstract.__init__(self, start_date, end_date, pay_date)


class CashflowSingle(CashflowAbstract):
    """
    single reset cashflow
    """
    def __init__(self, start_date, end_date, pay_date, reset_date):
        CashflowAbstract.__init__(self, start_date, end_date, pay_date, [reset_date])

    @property
    def reset_date(self):
        return self.resets[0]

    # def __repr__(self):
    #     return '<CashflowSingle: %s\t%s\t%s>' % (self.start_date, self.end_date, self.pay_date)

