from abc import ABCMeta


class ModelAbstract(object):
    __metaclass__ = ABCMeta

    @property
    def model_name(self):
        return None
