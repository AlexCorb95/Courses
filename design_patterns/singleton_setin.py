class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
            cls._instances[cls].color="red"
            cls._instances[cls].font_size=12
            cls._instances[cls].language="EN"
        return cls._instances[cls]


class ApplicationSettings(metaclass=SingletonType):
    def __init__(self):
        self.color = None
        self.font_size = None
        self.language = None


        # self.color = "red"
        # self.font_size=12
        # self.language="EN"




    # def __init__(self,font_dimension, language):
    #     self.color = "red"
    #     self.font_dimension = font_dimension
    #     self.language = language
    #




x=ApplicationSettings()
print(x.color)
y=ApplicationSettings()
print(y.language)