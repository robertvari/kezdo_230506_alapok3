class Card:
    def __init__(self, name, value):
        self.__name = name
        self.__value = value

    def __str__(self) -> str:
        return f"Name: {self.__name} Value: {self.__value}"


# only for testing
# this condition True only when we runt THIS file
if __name__ == "__main__":
    card1 = Card("Club King", 10)
    print(card1)