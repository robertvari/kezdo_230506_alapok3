import os, platform, time
from game_assets.cards import Deck
from game_assets.players import HumanPlayer, AI_Player


class Blackjack:
    def __init__(self) -> None:
        self.__deck = Deck()
        self.__player = None
        self.__player_list = []
        self.__reward = 0
        self.__min_bet = 10

        self.__clear_screen()
        self.__intro()
        self.__create_player_list()
        self.__game_loop()
    
    def __game_loop(self):
        self.__deck.create()
        self.__reward = 0

        # init players
        for player in self.__player_list:
            player.init_hand(self.__deck)
            self.__reward += player.give_bet(self.__min_bet)
            time.sleep(2)

        # start rounds
        for player in self.__player_list:
            player.draw_cards(self.__deck)
        
    def __get_winner(self):
        self.__clear_screen()
        for player in self.__player_list:
            player.info()

    def __create_player_list(self):
        self.__player = HumanPlayer()
        self.__player_list = [
            self.__player,
            AI_Player(),
            AI_Player(),
            AI_Player()
        ]

    @staticmethod
    def __clear_screen():
        os.system("cls") if platform.system() == "Windows" else os.system("clear")
    
    @staticmethod
    def __intro():
        print("-"*50, "BLACKJACK", "-"*50)

Blackjack()