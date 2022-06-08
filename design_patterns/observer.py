class Observer:
    def size_changed(self, size):
        print(f"Received new value from Observable, size={size}")


class Subject:
    def __init__(self):
        self.size = 15
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def set_size(self, size):
        self.size = size
        for observer in self.observers:
            observer.size_changed(self.size)


observer = Observer()
subject = Subject()
subject.set_size(16)
subject.add_observer(observer)
subject.set_size(25)
subject.set_size(30)
subject.remove_observer(observer)
subject.set_size(10)