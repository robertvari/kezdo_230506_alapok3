import random, time


class Player_BASE:
    def __init__(self) -> None:
        self._name = self.get_random_name()
        self.__credits = random.randint(50, 200)
        self.__hand = []
        self.__playing = True

    def draw_cards(self, deck):
        new_card = deck.draw()
        self.__hand.append(new_card)

    def init_hand(self, deck):
        self.__hand.clear()
        self.__playing = True

        self.__hand.append(deck.draw())

        # check new card and hand value before append
        new_card = deck.draw()
        if self.hand_value > 10 and new_card.value == 11:
            new_card.value = 1
        
        self.__hand.append(new_card)

    @property
    def hand_value(self):
        return sum([card.value for card in self.__hand])

    @staticmethod
    def get_random_name():
        first_names = ["Marnie", "Johnathan", "Mahnoor", "Hassan", "Alissa", "Millie", "Qasim", "Damon", "Shreya", "Carly"]
        last_names =  ["Roy", "Aguirre", "Sandoval", "Rogers", "Cole", "Matthams", "Allen", "Stokes", "Deleon", "Hampton"]

        return f"{random.choice(first_names)} {random.choice(last_names)}"

    def info(self):
        print("-"*50)
        print(f"Name: {self._name}")
        print(f"Credits: {self.__credits}")
        print(f"Hand: {self.__hand}")
        print(f"Hand value: {self.hand_value}")
        print("-"*50)

    def __repr__(self) -> str:
        return self._name

class HumanPlayer(Player_BASE):
    def __init__(self) -> None:
        super().__init__()
        # self._name = input("What is your name?")
        # TODO Remove this!!
        self._name = "Robert Vari"

class AI_Player(Player_BASE):
    pass


if __name__ == "__main__":
    from cards import Deck
    deck = Deck()
    ai_player1 = AI_Player()

    # ai_player1.draw_cards(deck)
    ai_player1.init_hand(deck)
    ai_player1.info()