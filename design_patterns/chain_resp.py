import abc


class Handler(abc.ABC):
    @abc.abstractmethod
    def get_task(self, task):
        pass


class HandlerA(Handler):
    def get_task(self, task):
        print(f"A {task}")


class HandlerB(Handler):
    def get_task(self, task):
        print(f"B {task}")


class HandlerC(Handler):
    def get_task(self, task):
        print(f'C {task}')

class Chain:
    def __init__(self,*handlers):
        self.handlers=handlers

    def give_task(self,task):
        first_task:Handler=self.handlers[0]
        """Index 0 makes referance to class HandlerA"""
        second_task:Handler=self.handlers[1]
        """Index 1 makes referance to class HandlerB"""
        third_task:Handler=self.handlers[2]
        """Index 2 makes referance to class HandlerC"""

        if "First" in task:
            first_task.get_task(task)
        if "Second" in task:
            second_task.get_task(task)
        if "Third" in task:
            third_task.get_task(task)



if __name__ == '__main__':
    chian=Chain(HandlerA(),HandlerB(),HandlerC())
    chian.give_task("First Task")
    chian.give_task("Second Task")
    chian.give_task("Third Task")
