from .abs_car import AbsCar


class Luxury(AbsCar):
    @property
    def description(self):
        return 'Luxury model'

    @property
    def cost(self):
        return 15000.0
