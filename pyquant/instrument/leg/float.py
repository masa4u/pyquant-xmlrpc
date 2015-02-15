from pyquant.instrument.leg.leg import LegAbstract


class FloatLeg(LegAbstract):
    class Meta:
        leg_size = 1
