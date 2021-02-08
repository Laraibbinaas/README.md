# Course: CS 30
# Period: 2
# Date created: 21/02/08
# Date last modified: 21/02/08
# Name: Laraib Bin Aas
# Description: A map with items,locations and charcters in it

# Importing all the dictionaries from other file
from dictionaries import player
from dictionaries import goblin
from dictionaries import golem
from dictionaries import meat
from dictionaries import fish
from dictionaries import rocks
from dictionaries import sword
from dictionaries import mountain
from dictionaries import house
from dictionaries import jungle
from dictionaries import cave

# Putting all the items in tiles for map

tile1 = [mountain, golem, rocks]
tile2 = [mountain, golem, rocks]
tile3 = [mountain, golem, rocks]
tile4 = [cave, goblin, rocks]
tile5 = [player, house, sword]
tile6 = [jungle, meat, fish]
tile7 = [cave, goblin, rocks]
tile8 = [jungle, meat, fish]
tile9 = [jungle, meat, fish]

# Putting all the tiles in an array to print

Map = [tile1, tile2, tile3,
       tile4, tile5, tile6,
       tile7, tile8, tile9]

print(Map)
