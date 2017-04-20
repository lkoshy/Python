from Subclasses.cars.abs_car import AbsCar


class AbsDecorator(AbsCar):
    def __init__(self, car):
        self._car = car

    # composition: at run time.
    @property
    def car(self):
        return self._car
