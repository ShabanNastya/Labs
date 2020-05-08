class Singleton(type):
    exemplar = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.exemplar:
            cls.exemplar[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.exemplar[cls]


class SimpleSingleton(metaclass=Singleton):
    pass


class SingletonWithValue(metaclass=Singleton):
    def __init__(self, value):
        self.value = value

a=SingletonWithValue(5)
pass
