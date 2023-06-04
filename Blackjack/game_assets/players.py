import random

class Player_BASE:
    def __init__(self) -> None:
        self.__name = None
        self.__credits = random.randint(50, 200)
        self.__hand = []
        self.__playing = True


class HumanPlayer(Player_BASE):
    pass

class AI_Player(Player_BASE):
    pass


if __name__ == "__main__":
    human_player = HumanPlayer()
    ai_player = AI_Player()