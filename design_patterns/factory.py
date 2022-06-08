import abc


class Game(abc.ABC):
    def __init__(self):
        self.name = None
        self.type = None

    @abc.abstractmethod
    def get_name(self):
        pass

    @abc.abstractmethod
    def get_type(self):
        pass


class BoardGame(Game):
    def get_name(self):
        return self.name

    def get_type(self):
        return self.type


class PCGame(Game):

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type


class GameCreator(abc.ABC):
    @abc.abstractmethod
    def create(self):
        pass


class MonopolyGameCreator(GameCreator):
    def create(self):
        return BoardGame()


class ValorantGameCreator(GameCreator):
    def create(self):
        return PCGame()


object_ = MonopolyGameCreator()
monopoly = object_.create()
valorant = ValorantGameCreator().create()
print(monopoly,valorant)
