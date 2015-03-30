from pyquant.instrument.leg.leg import LegAbstract


class FloatLeg(LegAbstract):

    def __init__(self, reference):
        super(FloatLeg, self).__init__()
        self.references = [reference]
