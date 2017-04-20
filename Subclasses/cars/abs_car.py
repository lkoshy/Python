import abc


# Abstract base class for all car models
class AbsCar(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def description(self):
        pass

    @abc.abstractmethod
    def cost(self):
        pass

'''
# Abstract base class for all car models
class AbsCar(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def description(self):
        pass

    @abc.abstractmethod
    def engine(self):
        pass

    @abc.abstractmethod
    def paint(self):
        pass

    @abc.abstractmethod
    def upholstery(self):
        pass

    def cost(self):
        cost = 0.0
        if self.engine == '4 cyl':
            cost += 0.00
        elif self.engine == '6 cyl':
            cost += 1200

        if self.paint == 'white':
            cost += 0.00
        elif self.paint == 'black':
            cost += 1000.00
        elif self.paint == 'red':
            cost += 2000.00

        if self.upholstery == 'vinyl':
            cost += 0.00
        elif self.upholstery == 'leather':
            cost += 2000.00

        return cost

'''
