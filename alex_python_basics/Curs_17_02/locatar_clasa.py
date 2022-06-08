class Apartament:
    def __init__(self, numar, suprafata, locatari):
        self.number = numar
        self.surface = suprafata
        self.tenents = locatari


class Locatar:
    def __init__(self, nume, prenume, data_nasterii):
        self.firsname = nume
        self.secondname = prenume
        self.birthday = data_nasterii

    def __repr__(self):
        return f"{self.firsname} {self.secondname} "


locatar_1 = Locatar("Popescu", "Ion", "1973-04-15")
print(locatar_1.firsname, locatar_1.secondname, locatar_1.birthday)
locatar_2 = Locatar("Ionescu", "Vasile", "1973-05-12")
aprt = Apartament("12", "11", [locatar_1, locatar_2])
print(aprt.tenents)
