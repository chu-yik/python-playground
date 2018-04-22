from collections import namedtuple

# shorter than defininig a class
Car = namedtuple('Car', 'color mileage year')

my_car = Car('blue', 5000, 1997)

print(my_car.color)
print(my_car.mileage)
print(my_car.year)

# string REPR is given to use for free
print(my_car)

# named tuples are immutable, like tuples!

# my_car.mileage = 6000
# will give error "AttributeError: can't set attribute"
