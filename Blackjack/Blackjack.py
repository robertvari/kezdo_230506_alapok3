import os, platform, time

class Blackjack:
    def __init__(self) -> None:
        self.clear_screen()
        self.intro()
    
    @staticmethod
    def clear_screen():
        os.system("cls") if platform.system() == "Windows" else os.system("clear")
    
    @staticmethod
    def intro():
        print("-"*50, "BLACKJACK", "-"*50)

Blackjack()