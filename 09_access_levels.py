class Dice:
    def __init__(self, color, sides) -> None:
        # public instance attribute
        self.color = color

        # protected instance attribute
        # self._sides = sides

        # private instance attribute
        self.__sides = sides

    def __str__(self) -> str:
        return f"Color: {self.color} Sides: {self.__sides}"

d6 = Dice("white", 6)
d6.color = "blue"