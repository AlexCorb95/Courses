import pickle


def save_object_to_filename(object_, filename):
    with open(filename, 'wb') as file:
        pickle.dump(object_, file)


def read_object_from_filename(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)


if __name__ == "__main__":
    dictionar = {}
    save_object_to_filename(dictionar, 'dictionar.pickle')
    dictionar_citit_din_fisier = read_object_from_filename('dictionar.pickle')
    print(dictionar_citit_din_fisier)
