"""
Fiind dat un obiect din clasa PCGame, cu requirements fiind o instanta din Requirements, si Requirements fiind o compozitie din Processor(), Ram(), VideoBoard().
Clasa PCGame contine si o instanta din AgeRating.
Sa se scrie un Adapter pentru  PCGame, care poate sa returneze o lista cu toate sprecificatiile, age rating, etc din simple metode aplelate pe el.
"""


class Cpu:
    def __init__(self, model, putere):
        self.model = model
        self.putere = putere


class Ram:
    def __init__(self, tip, capacitate):
        self.tip = tip
        self.capacitate = capacitate


class Gpu:
    def __init__(self, bitrate):
        self.bitrate = bitrate


class Requierments:
    def __init__(self,cpu,ram,gpu):
        self.cpu=cpu
        self.ram=ram
        self.gpu=gpu


class AgeRating:
    def __init__(self,age):
        self.age=age


class PcGames:
    def __init__(self, req, age_rating):
        self.req=req
        self.age_rating=age_rating

class PcGamesAdapter:
    def __init__(self,pc_games):
        self.pc_games=pc_games

    def get_req(self):
        return f"""
-==-PC REQ-==-
CPU:{self.pc_games.req.cpu.model}
Ram:{self.pc_games.req.ram.capacitate}
GPU:{self.pc_games.req.gpu.bitrate}
"""
    def get_age(self):
        return f"Minimum age is {self.pc_games.age_rating.age}"
agert=AgeRating(16)
cpu=Cpu("I7 6700k","4,2Ghz")
ram=Ram("DDR5","128 GB")
gpu=Gpu(512)
req=Requierments(cpu,ram,gpu)
gioc=PcGames(req,agert)
adapter=PcGamesAdapter(gioc)
print(adapter.get_age())
print(adapter.get_req())