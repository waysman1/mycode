#!/usr/bin/env python3

from random import randint

class Player:
    def __init__(self):
        self.dice = []

    def roll(self):
        self.dice = []
        for i in range(3):
            self.dice.append(randint(1,6))

    def get_dice(self):
        return self.dice

player1 = Player()
player2 = Player()

player1.roll()

print("Player 1 rolled " + str(player1.get_dice()))
        

