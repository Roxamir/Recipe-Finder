from opcode import opname
import time


fav_recipes = []

while True:
    # check file every second
    time.sleep(1)

    # open file and read line
    with open("favorites.txt", 'r') as file:
        cmd = file.readline().strip('\n')
    
    # if read line is "ADD", second line will be integer to add to list
    if cmd == "ADD":
        with open("favorites.txt", 'r') as file:
            lines = file.readlines()
            fav_recipes.append(str(lines[1]))    # append second line to list
        with open("favorites.txt", 'w+') as file:
            for favorite in fav_recipes:
                file.write(favorite + "\n")

    # if read line is "REMOVE", second line will be integer to remove from list.
    if cmd == "REMOVE":
        with open("favorites.txt", 'r') as file:
            lines = file.readlines()
            fav_recipes.remove(str(lines[1])) # remove second line from list
        # rewrite file with new array 
        with open("favorites.txt", 'w+') as file:
            for favorite in fav_recipes:
                file.write(favorite + "\n")
