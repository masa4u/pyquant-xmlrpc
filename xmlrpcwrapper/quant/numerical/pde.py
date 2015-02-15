from xmlrpcwrapper.quant.numerical.numerical import NumericalAbstract


class PDE(NumericalAbstract):
    class Meta:
        Parameter = {'DailyStep': int}


