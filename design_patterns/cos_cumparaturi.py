# Fiind data o clasa CosCumparaturi care contine un dictionar de perechi produs-cantitate, sa se scrie suportul pentru
# iterarea produselor cu ajutorul lui iter()

class CosCumparaturi:
    def __init__(self, dict_produse):
        self.dict_produse: dict = dict_produse

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        if self.index < len(self.dict_produse)-1:
            self.index += 1
            key = list(self.dict_produse.keys())[self.index]

            return key, self.dict_produse[key]
        else:
            raise StopIteration

cos={"ala":2,"bala":3,"alaa":3,"balla":4}
cos_clas=CosCumparaturi(cos)
# print(cos_clas.__iter__())
# print(cos_clas.__next__())
# print(cos_clas.__next__())
cos_iter=iter(cos_clas)
print(next(cos_iter))
for produs,cantitate in cos_clas:
    print(produs,cantitate)
