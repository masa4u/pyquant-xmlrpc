from pyquant.quant.numerical.numerical import NumericalAbstract
from pyquant.patterns.factory import Factory


class MonteCarlo(NumericalAbstract):
    Parameter = {'DailyStep': int,
                 'NumberOfSimulation': int}

    def __init__(self, args):
        for key, value in self.Parameter.items():
            setattr(self, key, args[key])

    def __repr__(self):
        return "<%s : %s>" % (self.__class__.__name__, str(self.DailyStep))

f = Factory()
f.register('MC20000', MonteCarlo, {'DailyStep': 20000, "NumberOfSimulation": 20000})

print f.MC20000().__class__.__name__
print f.MC20000()