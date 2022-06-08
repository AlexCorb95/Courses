import abc


class FahrenheitInterface(abc.ABC):
    @abc.abstractmethod
    def set_temp(self, fah):
        pass


class CelsiusInterface(abc.ABC):
    @abc.abstractmethod
    def set_temp(self, celsius):
        pass


class Celsius(CelsiusInterface):
    def __init__(self):
        pass

    def set_temp(self, celsius):
        print(f"Setting temperature to {celsius}'C")


class FahrenheitToCelsiusAdapter(FahrenheitInterface):
    def __init__(self, celsius):
        self.celsius = celsius

    # subtract 32 and multiply by . 5556 (or 5/9).
    def set_temp(self, fah):
        celsius = (fah - 32) * (5 / 9)
        self.celsius.set_temp(celsius)


ins_cels = Celsius()
adapter_fah = FahrenheitToCelsiusAdapter(ins_cels)
adapter_fah.set_temp(35)
