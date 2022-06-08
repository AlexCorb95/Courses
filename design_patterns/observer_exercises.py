import abc


class Observer(abc.ABC):
    @abc.abstractmethod
    def steps_made(self,steps):
        pass


class Human(Observer):
    def steps_made(self,steps):
        print(f"Human says dog made {steps} steps ")


class Pisica(Observer):
    def steps_made(self,steps):
        print("Our dog made ",steps, " until now..")

class Caine:
    def __init__(self):
        self.steps=25
        self.obs_steps=[]

    def add_oserver(self,observer):
        self.obs_steps.append(observer)

    def remove_observer(self,observer):
        self.obs_steps.remove(observer)

    def set_no_steps(self,steps):
        self.steps=steps
        for observer in self.obs_steps:
            observer:Pisica =observer

            observer.steps_made(steps)


pisica=Pisica()
catel=Caine()
om=Human()
catel.set_no_steps(30)
catel.add_oserver(pisica)
catel.set_no_steps(27)
catel.remove_observer(pisica)
catel.add_oserver(om)
catel.set_no_steps(30)
