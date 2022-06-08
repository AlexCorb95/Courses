import abc

class AbstractClassWithSkeleton(abc.ABC):
    @abc.abstractmethod
    def step_a(self):
        pass
    @abc.abstractmethod
    def step_b(self):
        pass
    @abc.abstractmethod
    def step_c(self):
        pass

    def algorithm_skeleton(self):
        self.step_a()
        self.step_b()
        self.step_c()

class AlgImpleA(AbstractClassWithSkeleton):
    def step_a(self):
        print("Alg A step a")
    def step_b(self):
        print("Alg A step b")
    def step_c(self):
        print("Alg A step c")

class AlgImpleB(AbstractClassWithSkeleton):
    def step_a(self):
        print("Alg B step a")
    def step_b(self):
        print("Alg B step b")
    def step_c(self):
        print("Alg B step c")


algorithm_a = AlgImpleA()
algorithm_a.algorithm_skeleton()
algorithm_b = AlgImpleB()
algorithm_b.algorithm_skeleton()

# import abc
#
#
# class AbstractClassWithSkeleton(abc.ABC):
#     @abc.abstractmethod
#     def step_a(self):
#         pass
#
#     @abc.abstractmethod
#     def step_b(self):
#         pass
#
#     @abc.abstractmethod
#     def step_c(self):
#         pass
#
#     def algorithm_skeleton(self):
#         self.step_a()
#         self.step_b()
#         self.step_c()
#
#
# class AlgorithmImplementationClassA(AbstractClassWithSkeleton):
#
#     def step_a(self):
#         print("AlgorithmImplementationClassA: step A ")
#
#     def step_b(self):
#         print("AlgorithmImplementationClassA: step B ")
#
#     def step_c(self):
#         print("AlgorithmImplementationClassA: step C ")
#
#
# class AlgorithmImplementationClassB(AbstractClassWithSkeleton):
#
#     def step_a(self):
#         print("AlgorithmImplementationClassB: step A ")
#
#     def step_b(self):
#         print("AlgorithmImplementationClassB: step B ")
#
#     def step_c(self):
#         print("AlgorithmImplementationClassB: step C ")
#
#
# algorithm_a = AlgorithmImplementationClassA()
# algorithm_a.algorithm_skeleton()
# algorithm_b = AlgorithmImplementationClassB()
# algorithm_b.algorithm_skeleton()