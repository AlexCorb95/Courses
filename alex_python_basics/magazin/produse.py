class Produs:

    def __init__(self, nume, pret, categorie, cantitate, descriere):
        self.name = nume
        self.price = round(pret,2)
        self.category = categorie
        self.quantity = cantitate
        self.description = descriere

    def __str__(self):
        return f"{self.name} - {self.quantity}buc  {self.price}lei"
    def __repr__(self):
        return str(self)


    def update (self, nume=None,pret=None,categorie=None,cantitate=None,descriere=None):
        if nume is not None:
            self.name=nume
        if pret is not None:
            self.price=round(pret,2)
        if categorie is not None:
            self.category=categorie
        if cantitate is not None:
            self.quantity=cantitate
        if descriere is not None:
            self.description=descriere

if __name__ == "__main__":
    sapca = Produs("Sapca", 12.5, "accesoriu", 22, "neagra")
    sapca.update("Ceapa",2.5,"alimente",123,"galbena")
    print(sapca)
