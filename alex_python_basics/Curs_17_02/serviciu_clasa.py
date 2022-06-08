# Sa se scrie clasa Serviciu, cu proprietatile nume, durata, pret
# Sa se scrie o clasa Frizer, cu proprietatile nume, prenume, servicii
# Sa se scrie clasa Programare cu nume, prenume, data, ora, serviciu, frizer
class Serviciu:
    def __init__(self, nume, durata, pret):
        self.name = nume
        self.duration = durata
        self.price = pret

    def __str__(self):
        return f"{self.name} {self.duration} {self.price}"

    def __repr__(self):
        return f"{self.name} {self.duration} {self.price}"


class Spalare(Serviciu):
    def __init__(self, nume, durata, pret, cantitate_sampon, cantitate_apa):
        super().__init__(nume, durata, pret)
        self.sampon = cantitate_sampon
        self.apa = cantitate_apa

    def __str__(self):
        return f"{self.name} {self.duration} {self.price} {self.sampon} {self.apa}"


class Frizer:
    def __init__(self, nume, prenume, servicii):
        self.firstname = nume
        self.secondname = prenume
        self.services = servicii

    def __str__(self):
        return f"{self.firstname} {self.secondname} {self.services}"


class Programare:
    def __init__(self, nume, prenume, data, ora, serviciu, frizer):
        self.nume = nume
        self.prenume = prenume
        self.data = data
        self.ora = ora
        self.serviciu = serviciu
        self.frizer = frizer

    def __str__(self):
        return f"{self.nume} {self.prenume} @ {self.data} @ {self.ora} pentru {self.serviciu} la {self.frizer}"


serviciu = Serviciu("Tuns", "20 de minute", 20.99)
spalare = Spalare("Spalare par scurt", "10 minute", "15 Lei", "40ml", "5L")
frizer = Frizer("Popescu", "Ion", [serviciu, spalare])
programare = Programare("Kun", "Eduard", "1999-10-12", "14:00:00.00", serviciu, frizer)
print(frizer)
print(spalare)
print(programare)
