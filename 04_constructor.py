class Dice:
    # Dice lass methods
    def __init__(self, sides, color):
        # instance attribute
        self.sides = sides
        self.color = color

d6_blue = Dice(6, "blue")
d10_red = Dice(10, "red")
d14_green = Dice(14, "green")
d20_yellow = Dice(20, "yellow")

class Person:
    def __init__(self, name, email, address) -> None:
        self.name = name
        self.email = email
        self.address = address

csaba = Person("Kiss Csaba", "csaba@gmail.com", "Pécs")
tamas = Person("Nagy Tamás", "tamas@gmail.com", "Budapest")

print(csaba.name, csaba.email, csaba.address)
print(tamas.name, tamas.email, tamas.address)