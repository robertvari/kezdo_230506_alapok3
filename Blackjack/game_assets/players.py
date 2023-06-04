import random

class Player_BASE:
    def __init__(self) -> None:
        self.__name = None
        self.__credits = random.randint(50, 200)
        self.__hand = []
        self.__playing = True

    @staticmethod
    def get_random_name():
        first_names = ["Marnie", "Johnathan", "Mahnoor", "Hassan", "Alissa", "Millie", "Qasim", "Damon", "Shreya", "Carly"]
        last_names =  ["Roy", "Aguirre", "Sandoval", "Rogers", "Cole", "Matthams", "Allen", "Stokes", "Deleon", "Hampton"]

class HumanPlayer(Player_BASE):
    pass

class AI_Player(Player_BASE):
    pass


if __name__ == "__main__":
    human_player = HumanPlayer()
    ai_player = AI_Player()