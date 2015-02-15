from xmlrpcwrapper.quant.numerical.numerical import NumericalAbstract
from xmlrpcwrapper.design_pattern.factory import Factory


class MonteCarlo(NumericalAbstract):
    class Meta:
        Parameter = {'DailyStep': int,
                     'NumberOfSimulation': int}

    def __init__(self, args):
        for key, value in self.Meta.Parameter.items():
            setattr(self, key, args[key])

    def __repr__(self):
        return "<%s : %s>" % (self.__class__.__name__, str(self.DailyStep))

f = Factory()
f.register('MC20000', MonteCarlo, {'DailyStep': 20000, "NumberOfSimulation": 20000})

print f.MC20000().__class__.__name__
print f.MC20000()