class Dice:
    # class attributes
    sides = 6
    color = "blue"

class Person:
    name = "Kiss Csaba"
    email = "csaba@gmail.com"
    address = "Pécs"


# This is an instance of a class: Dice
d6_blue = Dice()
print(d6_blue.color, d6_blue.sides)

d6_red = Dice()
d6_red.color = "red"
print(d6_red.color)

d6_green = Dice()
d6_green.color = "green"
print(d6_green.color)

d6_yellow = Dice()
d6_yellow.color = "yellow"
print(d6_yellow.color)

# Instances of the Person class
csaba = Person()
print(csaba.name, csaba.email, csaba.address)

tamas = Person()
tamas.name = "Nagy Tamás"
tamas.email = "tamas@gmail.com"
tamas.address = "Budapest"
print(tamas.name, tamas.email, tamas.address)