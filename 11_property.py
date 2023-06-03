class Dice:
    def __init__(self, color, sides):
        self.__color = color
        self.__sides = sides

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, new_color):
        self.__color = new_color
    
    @property
    def sides(self):
        return self.__sides

    def __str__(self) -> str:
        return f"{self.__color} {self.__sides}"

d6 = Dice("white", 6)
d6.color = "red"
print(d6.color, d6.sides)