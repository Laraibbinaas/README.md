# dictionaries of all the characters
player = {"Player":
          {"health": 100, "attack": 30, "description":
              "an adventurer controlled by you"}}
goblin = {"Goblin":
          {"health": 20, "attack": 2, "description":
              "tiny green creatures that like to feast on anything"}}
golem = {"Golem":
         {"health": 50, "attack": 5, "description":
             "pile of rocks combined to make a golem"}}

# putting all the characters in a list
characters = [player, goblin, golem]

# dicitionaries of all the inventory items
meat = {"Meat":
        {"healing": 20, "description": "big slab of cooked meat"}}
fish = {"Fish":
        {"healing": 10, "description":
            "big slab of cooked fish"}}
rocks = {"Rocks":
         {"healing": 1, "description": "rocks you found on the ground"}}
sword = {"Sword":
         {"attack": 1, "description":
             "a weapon forged of metal to slice through enemies"}}

# putting all the inventory items in a list
inventory = [meat, fish, rocks, sword]

# dicionaries of the locations
mountain = {"Mountains":
            {"enemies": "golem", "description":
                "a steep mountain with many giant rocks lying around"}}
house = {"House":
        {"items": "sword", "descritpion": "your house with all your items"}}
jungle = {"Jungle":
          {"items": "meat and fish", "description": "a big jungle with many animals"}}
cave = {"Cave":
        {"enemies": "goblin", "description": "a dark, spooky cave"}}

# puts all the loctions in a list
locations = [mountain, house, jungle, cave]
