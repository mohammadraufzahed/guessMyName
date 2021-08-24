"""
Game Class
"""
import json
import platform
from os import path, system
from random import randint


class GuessMyName:
    """
    GuessMyName Class
    """

    def __init__(self):
        self.names = self.__get_names()

    def start(self):
        """
        Start the game
        :return: None
        """
        self.__clear_prompt()
        # Score
        score = 0
        # Ask the user
        wanna_play = input("Do you wanna play? (Y, N) ")
        # While the answer is not no keep going
        while wanna_play != "n" and wanna_play != "N":
            print(wanna_play)
            # Generate the data
            data = self.__generate_data()
            # Generate the game data
            data["game_data"]["name"], data["game_data"]["pieces"] = self.__generate_game_data(
                data["difficulty"],
                data["name"]
            )
            while len(data["game_data"]["pieces"]) > 0:
                # Print the name
                print(f"Name: {data['game_data']['name']}")
                # Get the answer from the user
                guess_name = input("Guess: ")[0]
                # Validate the answer
                if data["game_data"]["pieces"][0] == guess_name:
                    data["game_data"]["pieces"].remove(data["game_data"]["pieces"][0])
                    data["game_data"]["name"] = data["game_data"]["name"].replace("_", guess_name, 1)
                self.__clear_prompt()
            print("Correct!")
            print("You got 10 points")
            score += 10
            print(f"Your Current Score {score}")
            wanna_play = input("Do you wanna play? (Y, N) ")
        print("Goodbye!")

    def __random_name(self) -> str:
        """
        Return the random name
        :return: str
        """
        return self.names[(randint(1, len(self.names)))]

    def __generate_data(self) -> dict:
        """
        Generate the game data
        :return: dict
        """
        real_name = self.__random_name()
        difficulty = int(len(real_name) / 3) + 1
        return {
            "name": real_name,
            "difficulty": difficulty,
            "game_data": {
                "name": real_name,
                "pieces": []
            }
        }

    def __generate_game_data(self, difficulty: int, name: str) -> list:
        """
        Generate the game data
        :param difficulty:
        :param name:
        :return:
        """
        pieces = list()
        for _ in range(difficulty):
            char = name[len(name) - 1]
            if char != "_":
                name = name.replace(char, "_", 1)
                pieces.append(char)
        return [
            name,
            pieces
        ]

    def __clear_prompt(self):
        """
        Clear the prompt
        :return: None
        """
        os = platform.system()
        if os == "Windows":
            system("cls")
        else:
            system("clear")

    def __get_names(self):
        """
        Collect the names from the json
        :return: list
        """
        with open(path.normpath(path.dirname(__file__) + "\\names.json"), "r", encoding="utf8") as names_json:
            return json.load(names_json)

    def __del__(self):
        pass
