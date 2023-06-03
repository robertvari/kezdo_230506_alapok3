class Dice:
    colors = ["white", "red", "blue", "yellow"]
    allowed_sides = [6, 10, 20]

    def __init__(self, color, sides) -> None:
        self.__check_color(color)
        self.__check_sides(sides)

        self.__color = color
        self.__sides = sides
    
    def get_color(self):
        return self.__color
    
    def set_color(self, new_color):
        self.__check_color(new_color)
        self.__color = new_color

    # public method
    def get_sides(self):
        return self.__sides
    
    # public method
    def set_sides(self, new_sides):
        self.__check_sides(new_sides)
        self.__sides = new_sides
    
    # private method
    def __check_color(self, new_color):
        assert new_color in Dice.colors, f"Color must be {Dice.colors}"

    def __check_sides(self, new_sides):
        assert new_sides in Dice.allowed_sides, f"Sides must be: {Dice.allowed_sides}"

    def __str__(self) -> str:
        return f"Color: {self.__color} Sides: {self.__sides}"

d6 = Dice(10, "Robert")