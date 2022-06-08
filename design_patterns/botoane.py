import abc


class Buton(abc.ABC):
    @abc.abstractmethod
    def apasare_buton(self, ):
        pass


class ButonPornire(Buton):
    def apasare_buton(self, ):
        print("pornire...")


class ButonInaite(Buton):
    def apasare_buton(self, ):
        print("mutare canal")


if __name__ == '__main__':
    buton_pornire = ButonPornire()
    buton_inaite = ButonInaite()
    buton_pornire.apasare_buton()
    buton_inaite.apasare_buton()