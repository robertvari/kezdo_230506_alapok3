import random, time


class Player_BASE:
    def __init__(self) -> None:
        self._name = self.get_random_name()
        self.__credits = random.randint(50, 200)
        self.__hand = []
        self.__playing = True

    @property
    def hand(self):
        return tuple(self.__hand)
    
    @property
    def playing(self):
        return self.__playing
    
    @playing.setter
    def playing(self, new_playing):
        assert isinstance(new_playing, bool), "new_playing must be of type bool"
        self.__playing = new_playing

    def _add_card(self, new_card):
        if self.hand_value > 10 and new_card.value == 11:
            new_card.value = 1
        self.__hand.append(new_card)

    def draw_cards(self, deck):
        assert len(self.__hand) == 2, "Player hand must be inited!"

        if not self.__playing:
            print(f"{self._name} not playing this time.")
            return
        
        print(f"{self._name} starts his/her turn...")
        time.sleep(2)
        
        while self.__playing:
            # check hand value
            hand_value = self.hand_value

            if hand_value < random.randint(16, 19):
                print(f"{self._name} draws a card")
                time.sleep(2)
             
                self._add_card(deck.draw())
            else:
                print(f"{self._name} finishes his/her turn.")
                time.sleep(2)
                self.__playing = False

    def init_hand(self, deck):
        self.__hand.clear()
        self.__playing = True

        self._add_card(deck.draw())
        self._add_card(deck.draw())

    def give_bet(self, min_bet) -> int:
        return_credits = min_bet
        
        if self.__credits < min_bet:
            self.__playing = False
            return 0

        if self.hand_value >= 18 and self.hand_value < 21:
            return_credits += (self.__credits - min_bet) // 2

        if self.hand_value == 21:
            return_credits = self.__credits

        return return_credits

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

    def draw_cards(self, deck):
        print(f"This is your turn {self._name.split()[0]}")

        while self.playing:
            print(f"Your cards: {self.hand}")
            print(f"Hand value: {self.hand_value}")
            
            if self.hand_value > 20:
                self.playing = False
                print(f"You finished your turn. Your hand value: {self.hand_value}")
                break

            player_choice = input("Do you want to draw a new card? (y/n)")
            if player_choice.lower() == "y":
                new_card = deck.draw()
                print(f"Your card: {new_card}")
                self._add_card(new_card)
                time.sleep(3)
            else:
                if self.hand_value < 16:
                    print("You have to draw a card. Your hand value less thand 16.")
                else:
                    self.playing = False

class AI_Player(Player_BASE):
    pass


if __name__ == "__main__":
    from cards import Deck
    deck = Deck()
    
    player = HumanPlayer()
    player.init_hand(deck)
    player_bet = player.give_bet(10)
    player.draw_cards(deck)

    player.info()
    print(player_bet)