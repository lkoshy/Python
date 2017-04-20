from Subclasses.decorators.abs_decorator import AbsDecorator


class Black(AbsDecorator):
    @property
    def description(self):
        return self.car.description + ', Black'

    @property
    def cost(self):
        return self.car.cost + 1500.00
