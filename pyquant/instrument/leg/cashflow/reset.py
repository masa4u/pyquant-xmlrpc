from abc import ABCMeta


class ResetAbstract(object):
    __metaclass__ = ABCMeta

    def __init__(self, reset_date, start_date, end_date=None):
        self._reset_date = reset_date
        self._start_date = start_date
        if end_date == None:
            self._end_date = start_date
        else:
            self._end_date = end_date

    @property
    def reset_date(self):
        return self._reset_date

    @property
    def start_date(self):
        return self._start_date

    @property
    def end_date(self):
        return self._end_date

    def __repr__(self):
        return '%s' % ( self.reset_date)