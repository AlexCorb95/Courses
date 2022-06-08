class Vehicul:
    def __init__(self, culoare, nr_roti, motorizare, nr_locuri):
        self.color = culoare
        self.roti = nr_roti
        self.motorizare = motorizare
        self.seats = nr_locuri

    def __str__(self):
        return f"{self.color} {self.roti} {self.motorizare} {self.seats}"


class Masini(Vehicul):

    def __init__(self, brand, model, capacitate, putere, culoare, motorizare, nr_locuri):
        super().__init__(culoare, 4, motorizare, nr_locuri)
        self.brand = brand
        self.model = model
        self.capacity = capacitate
        self.power = putere

    def __str__(self):
        return f"{self.brand} {self.model} {self.capacity} {self.power}"

vehicul= Vehicul("albastru",6,"disel",5)
masina = Masini("Audi", "RS6", "4765 cmc", "510 HP", "Negru","Benzina","5")
print(masina,"-",vehicul)
