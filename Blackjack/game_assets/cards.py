class Card:
    def __init__(self, name, value):
        self.__name = name
        self.__value = value

    def __str__(self) -> str:
        return f"Name: {self.__name} Value: {self.__value}"
    
    def __repr__(self) -> str:
        return f"{self.__name} {self.__value}"


# only for testing
# this condition True only when we runt THIS file
if __name__ == "__main__":
    card1 = Card("Club King", 10)
    card2 = Card("Spade Ace", 11)
    my_cards = [card1, card2]
    print(my_cards)