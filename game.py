import random


class Flashcard:
    def __init__(self):
        self.fruits = {"Banana": "yellow", "Strawberries": "pink"}
        print("Welcome to the fruit quiz")
        self.fru()

    def fru(self):
        while True:
            fruit = random.choice(list(self.fruits.keys()))
            color = self.fruits[fruit]
            print("What is the color of the ", fruit)
            b = input("Enter the color of the fruit")
            if color == b:
                print("correct answer")
            else:
                print("wrong answer")
            play_again=input("play again ? yes/no").lower()
            if play_again!="yes":
                print("Thanks for your time")
                break


c=Flashcard()
c
