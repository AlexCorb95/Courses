# Sa se scrie un Singleton care isi salveaza/incarca proprietatile intr-un/dintr-un fisier.

import pickle
import os


class Singleton:
    instance = None  # proprietate statica, adica a clasei, si nu a instantei.

    def __new__(cls, *args, **kwargs):  # cls refera clasa curenta, Singleton, NU o instanta a ei.
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            # lazy init pe o proprietate
            cls.instance.load_info()

        return cls.instance

    def save_info(self):
        with open('our_info.pickle', 'wb') as file:
            pickle.dump(self, file)

    def load_info(self):
        if os.path.exists('our_info.pickle'):
            with open('our_info.pickle', 'rb') as file:
                self = pickle.load(file)
        else:
            self.color = 'brown'
            self.font_size = 156
            self.language = 'Ro'
            self.save_info()


singleton_obj = Singleton()
singleton_obj.save_info()
singleton_obj.load_info()

print(singleton_obj.color)
print(singleton_obj.language)
print(singleton_obj.font_size)
