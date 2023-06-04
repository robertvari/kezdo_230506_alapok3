import os, platform, time
from game_assets.cards import Deck


class Blackjack:
    def __init__(self) -> None:
        # self.clear_screen()
        self.intro()

        self._deck = Deck()
    
    @staticmethod
    def clear_screen():
        os.system("cls") if platform.system() == "Windows" else os.system("clear")
    
    @staticmethod
    def intro():
        print("-"*50, "BLACKJACK", "-"*50)

Blackjack()