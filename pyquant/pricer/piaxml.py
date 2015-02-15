from xmlrpcwrapper.pricer.pricer import PricerAbstract, PricerType

class PIAXML(PricerAbstract):
    class Meta:
        pricer_type = PricerType.PIAXML
