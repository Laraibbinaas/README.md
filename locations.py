# Course: CS 30
# Period: 2
# Date created: 21/02/08
# Date last modified: 25/02/08
# Name: Laraib Bin Aas
# Description: Creates the locations and what you can do in
# Code adpated from https://github.com/kynite/FishingRPG

from world import player
from enemies import *


def cave():
    while True:
        print("You enter a cave and a wild goblin approaches you")
        print("Would you like to [fight] or [leave]")
        print("(if you leave you will be put on the tile you were on before)")
        action = input("choose an action: ")
        # Checks to see if user typed in fight
        if action == "fight":
            player.fight(Goblin())
        # Checks to see if user typed in leave
        elif action == "leave":
            # Exits the area and goes back to map
            break
        # Checks to see if user typed q to quit aswell
        else:
            print("invalid input")


def mountain():
    while True:
        print("You climb a mountaina and see a golem standing in front of you")
        print("Would you like to [fight] or [leave]")
        print("(if you leave you will be put on the tile you were on before)")
        action = input("choose an action: ")
        # Checks to see if user typed in fight
        if action == "fight":
            player.fight(Golem())
        # Checks to see if user typed in leave
        elif action == "leave":
            # Exits the area and goes back to map
            break
        # Checks to see if user typed q to quit aswell
        else:
            print("invalid input")


def house():
    while True:
        print("You enter a house to rest up")
        print("You encounter no enemies")
        print("Would you like to [fight] or [leave]")
        print("(if you leave you will be put on the tile you were on before)")
        action = input("choose an action: ")
        # Checks to see if user typed in fight
        if action == "fight":
            print("There is no one to fight")
        # Checks to see if user typed in leave
        elif action == "leave":
            # Exits the area and goes back to map
            break
        # Checks to see if user typed q to quit aswell
        else:
            print("invalid input")


def jungle():
    while True:
        print("You swing through jungle when golbins start running at you.")
        print("Would you like to [fight] or [leave]")
        print("(if you leave you will be put on the tile you were on before)")
        action = input("choose an action: ")
        # Checks to see if user typed in fight
        if action == "fight":
            player.fight(Goblin())
        # Checks to see if user typed in leave
        elif action == "leave":
            # Exits the area and goes back to map
            break
        # Checks to see if user typed q to quit aswell
        else:
            print("invalid input")


def end():
    while True:
        print("This is the end of the game. Press W to win")
        print("(if you leave you will be put on the tile you were on before)")
        action = input("choose an action: ")
        # Checks to see if user typed in win
        if action == "a":
            quit()
        # Checks to see if user typed in leave
        elif action == "leave":
            # Exits the area and goes back to map
            break
        # Checks to see if user typed q to quit aswell
        else:
            print("invalid input")
