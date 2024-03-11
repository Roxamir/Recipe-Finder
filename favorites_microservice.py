import time

# list to store recipe IDs
fav_recipes = []

# read favorites.txt and store current favorites
with open("favorites.txt", 'r') as file:
    # store lines in an array
    lines = file.read().splitlines() # read().splitlines() reads all the lines from the files, but removes newline character

# iterate through lines array and add each line to list
for line in lines:
        fav_recipes.append(line)   # append favorite ID to fav_recipes


# run until stopped
while True:
    # check file every 2 seconds
    time.sleep(2)

    # open file and read first line
    with open("favorites.txt", 'r') as file:
        cmd = file.readline().strip('\n')   # remove newline charater so it isn't stored, otherwise cmd == "ADD\n"

    # if read line is "ADD", second line in text file will be an integer to add to list
    if cmd == "ADD":
        # open file and read all file lines
        with open("favorites.txt", 'r') as file: 
            lines = file.read().splitlines()    # store lines in an array w/o newline character
            fav_recipes.append(lines[1])        # append second line to list (the favorite recipe ID)
        # open favorites.txt, erase it and rewrite new favorites to file    
        with open("favorites.txt", 'w+') as file:
            for favorite in fav_recipes:        # iterate through fav_recipes
                if favorite != "\n":            # if line is newline character, do not add to array (not super necessary, just makes txt look nicer.)
                    file.write(favorite + "\n") # write favorite ID and newline 

    # if read line is "REMOVE", second line will be integer to remove from list.
    if cmd == "REMOVE":
        # open file and read all file lines
        with open("favorites.txt", 'r') as file:
            lines = file.read().splitlines()    # store lines in an array w/o newline character
            fav_recipes.remove(lines[1])        # remove second line value from list
        # open favorites.txt, erase it and rewrite new favorites to file
        with open("favorites.txt", 'w+') as file:
            for favorite in fav_recipes:        # iterate through fav_recipes
                if favorite != "\n":            # if line is newline character, do not add to array (not super necessary, just makes txt look nicer.)
                    file.write(favorite + "\n") # write favorite ID and newline
