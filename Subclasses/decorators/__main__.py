from Subclasses.cars.economy import Economy
from Subclasses.cars.luxury import Luxury
from Subclasses.decorators.v6 import V6
from Subclasses.decorators.black import Black


def main():
    car = Economy()
    show(car)

    car = V6(car)
    show(car)

    car = Black(car)
    show(car)

    car = Luxury()
    show(car)


def show(car):
    print('Description: {}; cost: ${}'.format(car.description, car.cost))

if __name__ == '__main__':
    main()
