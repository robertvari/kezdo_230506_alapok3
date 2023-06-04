import random

class Player_BASE:
    def __init__(self) -> None:
        self._name = self.get_random_name()
        self.__credits = random.randint(50, 200)
        self.__hand = []
        self.__playing = True

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
    human_player = HumanPlayer()
    ai_player1 = AI_Player()
    ai_player2 = AI_Player()
    ai_player3 = AI_Player()

    human_player.info()
    ai_player1.info()
    ai_player2.info()
    ai_player3.info()