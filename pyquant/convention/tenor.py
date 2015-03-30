
class Tenor():
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tenor_to_string(self):
        rlt = ''
        if self.year > 0:
            rlt += '%dY' % (self.year)
        if self.month > 0:
            rlt += '%dM' % (self.month)
        if self.day > 0:
            rlt += '%dD' % (self.day)
        return rlt

    def __repr__(self):
        return '<Tenor(%s)>' % (self.tenor_to_string())

if __name__ == '__main__':
    tenor = Tenor(0, 3, 0)
    print tenor

    print tenor.tenor_to_string()