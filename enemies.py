# Course: CS 30
# Period: 2
# Date created: 21/02/08
# Date last modified: 25/02/08
# Name: Laraib Bin Aas
# Description: Creating all the enemies in the game
# Code adpated from https://github.com/kynite/FishingRPG


class Enemy():
    """Enemy Class to raise errors and return the enemy's name"""
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects")

    def __str__(self):
        return self.name


class Goblin(Enemy):
    """Hostle goblin with name, health points and damage"""
    def __init__(self):
        self.name = "Green Goblin"
        self.hp = 10
        self.damage = 2


class Golem(Enemy):
    """Rocky golem with name, health points and damage"""
    def __init__(self):
        self.name = "Rock Golem"
        self.hp = 25
        self.damage = 1
