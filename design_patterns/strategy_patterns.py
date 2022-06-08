# Sa se scrie o clasa Product, care poate fi serializat/deserializat cu JSON, Pickle.
import abc
import json
import pickle


class Encoder(abc.ABC):
    @abc.abstractmethod
    def encode(self, object_):
        pass

    def decode(self, string):
        pass


class JsonEncoder(Encoder):
    def encode(self, object_):
        # print(object_.__dict__.__doc__)
        return json.dumps(object_,default=lambda o:o.__dict__)

    def decode(self, string):
        return json.loads(string)


class PickleEncoder(Encoder):
    def encode(self, object_):
        return pickle.dumps(object_)

    def decode(self, string):
        return pickle.loads(string)


class Product:
    def __init__(self, title, price, encoder):
        self.title = title
        self.price = price
        self.encoder = encoder

    def encode(self):
        return self.encoder.encode(self)

    def decode(self, string):
        return self.encoder.decode(string)


produs=Product("Varza",12,JsonEncoder())
product_encoded=produs.encode()
print(product_encoded)
product_decoded=produs.decode(product_encoded)
print(product_decoded)
print(produs)