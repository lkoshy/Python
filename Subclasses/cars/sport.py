from .abs_car import AbsCar


class Sport(AbsCar):
    @property
    def description(self):
        return 'Sport model'

    @property
    def cost(self):
        return 18000.0
