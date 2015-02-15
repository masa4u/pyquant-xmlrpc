def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""
    return meta("NewBase", bases, {})


class SingletonMetaclass(type):
    """Singleton Metaclass
    This metaclass is used for creating singletons.
    It changes the class __new__ method to maintain only one instance of the
    class, and tweaks the __init__ method to be executed only once (when the
    first instance of the class is created.
    Usage::
        >>> class MySingleton(object, meta=SingletonMetaclass):
        ...     '''Real singleton class.
        ...
        ...     You have to set the metaclass to SingletonMetaclass,
        ...     and define the __init__ function. Everything else will
        ...     be done by metaclass.
        ...     '''
        ...     def __init__(self, data):
        ...         print 'Initializing'
        ...         self.data = data
        ...
        >>> # Only this actually happen
        >>> first = MySingleton('First initialization')
        Initializing
        >>> second = MySingleton('Second initialization') # This won't happen
        >>> first.data
        'First initialization'
        >>> second.data
        'First initialization'
        >>>
    """
    def __init__(cls, *args, **kwargs):
        super(SingletonMetaclass, cls).__init__(*args, **kwargs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):  # @NoSelf
        if cls._instance is None:
            cls._instance = super(SingletonMetaclass, cls).__call__(*args,
                                                                    **kwargs)
        return cls._instance