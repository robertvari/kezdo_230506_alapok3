import time, random

class Dice:
    def __init__(self, color, sides):
        self.color = color
        self.sides = sides
    
    def roll(self):
        print(f"The {self.color} {self.sides} is rolling...")
        time.sleep(random.randint(1, 4))
        print(f"The number is: {random.randint(1, self.sides)}")

d6 = Dice("white", 6)

class Person:
    def __init__(self, name) -> None:
        self.name = name

    def say_hello(self):
        print(f"Hello. My name is {self.name}")

csaba = Person("Kiss Csaba")
tamas = Person("Nagy Csaba")
csilla = Person("Kovács Csilla")
csaba.say_hello()
tamas.say_hello()
csilla.say_hello()