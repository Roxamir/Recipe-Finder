import sqlite3
import time
from prettytable import PrettyTable, ALL
import subprocess


def loading_animation(x):
    for i in range(x):
        time.sleep(1)
        print("*")

def show_ingredients():
    # connecting to the database
    db = sqlite3.connect("recipe_finder.db")
    db.execute("PRAGMA foreign_keys = ON")

    # cursor object c
    c = db.cursor()

    # Select all Names and Descriptions from ingredients
    ingredients = c.execute("SELECT ingredient_id, ingredient_name, ingredient_description FROM ingredients")

    #format data with PrettyTable
    table = PrettyTable()
    table.hrules = ALL      # horizontal separators
    table.field_names = ['ID','Ingredient', 'Description']       # column titles
    table._max_width = {"ID": 10, "Ingredient" : 25, "Description" : 75} # max width for columns
    table.align["Description"] = "l"    # left align description column
    table.add_rows(ingredients) # add rows to table

    print("Here are all the ingredients in the database: ")
    loading_animation(2)
    print(table)
    loading_animation(2)

    db.close()

def show_recipes():
    # connecting to the database
    db = sqlite3.connect("recipe_finder.db")
    db.execute("PRAGMA foreign_keys = ON")

    # cursor object c
    c = db.cursor()

    # Select all Names and Descriptions from ingredients
    recipes = c.execute("SELECT recipe_id, recipe_name, recipe_description FROM recipes")

    #format data with PrettyTable
    table = PrettyTable()
    table.hrules = ALL      # horizontal separators
    table.field_names = ['ID','Recipe', 'Description']       # column titles
    table._max_width = {"ID": 10, "Recipe" : 25, "Description" : 75} # max width for columns
    table.align["Description"] = "l"    # left align description column
    table.add_rows(recipes) # add rows to table

    print("Here are all the recipes in the database: ")
    loading_animation(2)
    print(table)
    loading_animation(2)

    db.close()

def ingredient_search(ingredient):
    # connecting to the database
    db = sqlite3.connect("recipe_finder.db")
    db.execute("PRAGMA foreign_keys = ON")

    # cursor object c
    c = db.cursor()

    # Ingredient Search SQL Query
    query = ("SELECT ingredient_name, ingredient_description FROM ingredients WHERE ingredient_name LIKE ? COLLATE NOCASE")

    # check if ingredient exists in DB
    results = c.execute(query, ("%" + ingredient + "%",))
    if c.fetchone() == None:
        loading_animation(2)
        print("Sorry. No ingredients with the word '" + ingredient + "' are found in the database. Please try again.")
        return

    results = c.execute(query, ("%" + ingredient + "%",))

    #format data with PrettyTable
    table = PrettyTable()
    table.hrules = ALL      # horizontal separators
    table.field_names = ['Ingredient', 'Description']       # column titles
    table._max_width = {"Ingredient" : 25, "Description" : 75} # max width for columns
    table.align["Description"] = "l"    # left align description column
    table.add_rows(results) # add rows to table

    print("Here are the ingredients that contain the word '" + ingredient + "'.")
    loading_animation(2)
    print(table)
    loading_animation(2)

    db.close()

def ingredient_add(added_ingredient):
    
    # connecting to the database
    db = sqlite3.connect("recipe_finder.db")
    db.execute("PRAGMA foreign_keys = ON")

    # cursor object c
    c = db.cursor()

    query = ("SELECT ingredient_name, ingredient_description FROM ingredients WHERE ingredient_name LIKE ? COLLATE NOCASE")

    ingredient_check = c.execute(query, ("%" + added_ingredient + "%",))

    # if similar ingredient is found, check with user if ingredient is in db
    if ingredient_check.fetchone() != None:
        table = PrettyTable()
        table.hrules = ALL      # horizontal separators
        table.field_names = ['Ingredient', 'Description']       # column titles
        table._max_width = {"Ingredient" : 25, "Description" : 75} # max width for columns
        table.align["Description"] = "l"    # left align description column
        ingredient_check = c.execute(query, ("%" + added_ingredient + "%",))
        table.add_rows(ingredient_check) # add rows to table
        print("""
              
              It looks like we found some similar ingredients. Do you mean any of these ingredients?
              
              """)
        print(table)

        confirm = input("Type 'YES' if ingredient exists in database, otherwise ingredient addition will continue: ")

        if confirm == 'YES':
            return
    

    ingredient_description = input("Please input a description for the ingredient (optional): ")

    insert_query = ("INSERT INTO ingredients (ingredient_name, ingredient_description) VALUES (?, ?)")



    # insert ingredient into db
    c.execute(insert_query, (added_ingredient, ingredient_description))
    db.commit()
    db.close()

    print("""
          
          Ingredient has been successfully added.
          
          """)
    loading_animation(2)

def ingredient_remove():
    # warning animation
    for i in range(3):
        print("""
              *** WARNING ***
              """)
        time.sleep(1)

    print("""
          PLEASE READ:
          DELETING AN INGREDIENT WILL ALSO DELETE THE RECIPE LINES ASSOCIATED WITH THAT INGREDIENT!!!
          ENSURE THAT INGREDIENT IS NOT PRESENT IN ANY RECIPES BEFORE DELETING TO ENSURE RECUPES ARE CORRECT!!!

          INPUT 'CONTINUE' TO PROCEED WITH INGREDIENT REMOVAL.
          OTHERWISE PROGRAM WILL RETURN TO THE MAIN MENU.
          """)
    
    loading_animation(2)
    
    cont = input("Input 'CONTINUE' to proceeed: ")

    loading_animation(2)

    if cont == 'CONTINUE':
        show_ingredients()
        loading_animation(2)
    
    else:
        print("CONTINUE not entered. Returning to main menu...")
        loading_animation(2)

    # connecting to the database
    db = sqlite3.connect("recipe_finder.db")
    db.execute("PRAGMA foreign_keys = ON")

    # cursor object c
    c = db.cursor()

    ingredient_id = input("Please enter ingredient ID of ingredient you wish to delete: ")
    loading_animation(2)

    # get name of ingrdient to display to user for confirmation
    name_query = ("SELECT ingredient_name FROM ingredients WHERE ingredient_id = ?")
    c.execute(name_query, (ingredient_id,))
    ingredient_name = c.fetchone()[0]

    # executing delete query
    c.execute("DELETE FROM ingredients WHERE ingredient_id = ?", (ingredient_id,))
    db.commit()

    print("'" + ingredient_name + "' deleted.")

    db.close()    
    
def recipe_search(recipe):

    # connecting to the database
    db = sqlite3.connect("recipe_finder.db")
    db.execute("PRAGMA foreign_keys = ON")

    # cursor object c
    c = db.cursor()

    # Recipe Search SQL Query
    query = ("SELECT recipe_name, recipe_description FROM recipes WHERE recipe_name LIKE ? COLLATE NOCASE")

    # check if recipe exists in DB.
    results = c.execute(query, ("%" + recipe + "%",))
    if c.fetchone() == None:
        loading_animation(2)
        print("Sorry. No recipes with the word '" + recipe + "' are found in the database. Please try again.")
        return
    
    # execute search query to display results
    results = c.execute(query, ("%" + recipe + "%",))
   
    #format data with PrettyTable
    table = PrettyTable()
    table.hrules = ALL      # horizontal separators
    table.field_names = ['Recipe', 'Description']       # column titles
    table._max_width = {"Recipe" : 50, "Description" : 100} # max width for columns
    table.align["Description"] = "l"    # left align description column
    table.add_rows(results) # add rows to table

    print("Here are the recipes that contain the word '" + recipe + "'.")
    loading_animation(2)
    print(table)
    loading_animation(2)
    
    db.close()           

def recipe_view():
    # connecting to the database
    db = sqlite3.connect("recipe_finder.db")
    db.execute("PRAGMA foreign_keys = ON")

    # cursor object c
    c = db.cursor()

    recipes = c.execute("SELECT recipe_id, recipe_name, recipe_description FROM recipes")

    print("Select an ID from the following recipes in the database.")
    loading_animation(5)
    # table to display data
    recipe_table = PrettyTable()
    recipe_table.hrules = ALL      # horizontal separators
    recipe_table.field_names = ['ID', 'Recipe', 'Description']       # column titles
    recipe_table._max_width = {"ID" : 10, "Recipe" : 25, "Description" : 75} # max width for columns
    recipe_table.align["Description"] = "l"    # left align description column
    recipe_table.add_rows(recipes)
    print(recipe_table)

    loading_animation(5)
    recipe_id = input("Please input a recipe ID to view the recipe: ")

    # query for recipe name
    name_query = ("SELECT recipe_name FROM recipes WHERE recipe_id = ?")
    recipe_name = c.execute(name_query, (recipe_id,))
    recipe_name = c.fetchone()

    # if recipe does not exist, exit
    if recipe_name == None:
       loading_animation(5)
       print("The recipe you entered does not seem to be in the database. Please check the previous input and try again.")
       return
    else:
        recipe_name = recipe_name[0]
    # query for recipe instructions
    instructions_query = ("SELECT recipe_instructions FROM recipes WHERE recipe_id = ?")
    instructions = c.execute(instructions_query, (recipe_id,))
    instructions = c.fetchone()[0]

    # query for source
    source_query = ("Select recipe_source FROM recipes WHERE recipe_id = ?")
    source = c.execute(source_query, (recipe_id,))
    source = c.fetchone()[0]

    # query for ingredients line
    line_query = ("SELECT recipe_lines.quantity, ingredients.ingredient_name FROM recipe_lines INNER JOIN ingredients ON recipe_lines.ingredient_id = ingredients.ingredient_id WHERE recipe_lines.recipe_id = ?")
    recipe_lines = c.execute(line_query, (recipe_id,))

    line_table = PrettyTable()
    line_table.hrules = ALL      # horizontal separators
    line_table.field_names = ['Quantity', 'Ingredient']       # column titles
    line_table._max_width = {"Quantity" : 50, "Ingredient" : 50} # max width for columns
    line_table.align["Ingredient"] = "l"    # left align ingredient column
    line_table.add_rows(recipe_lines)

    loading_animation(5)

    print("You selected the recipe '" + recipe_name + "'. Here are the ingredients" )
    loading_animation(2)
    print(line_table)
    loading_animation(5)

    print("Here are the instructions: ")
    loading_animation(2)
    print(instructions)

    loading_animation(5)

    print("For more information, visit the recipe source: ")
    loading_animation(2)
    print(source)

    db.close()
    
def recipe_add():
    # connecting to the database
    db = sqlite3.connect("recipe_finder.db")
    db.execute("PRAGMA foreign_keys = ON")

    # cursor object c
    c = db.cursor()

    # recipe info
    recipe_name = input("Please input the NAME of your recipe (required): ")
    loading_animation(2)
    recipe_description = input("Please input the DESCRIPTION of your recipe (optional): ")
    loading_animation(2)
    recipe_instructions = input("Please input the INSTRUCTIONS of your recipe (required): ")
    loading_animation(2)
    recipe_source = input("Please input the SOURCE where your recipe is from  (optional): ")
    loading_animation(2)

    insert_query = ("INSERT INTO recipes (recipe_name, recipe_description, recipe_instructions, recipe_source) VALUES(?,?,?,?)")

    c.execute(insert_query, (recipe_name, recipe_description, recipe_instructions, recipe_source))

    db.commit()

    # save last inserted id
    recipe_id = c.lastrowid

    # ingredient ids
    print("Input all the required ingredient IDs, separating them with a space.")
    loading_animation(2)
    ingredient_str = input("(Example: '1 12 14 28 47 32'): ")
    ingredient_ids = ingredient_str.split()
    loading_animation(2)

    for i in range(len(ingredient_ids)):
        if not ingredient_ids[int(i)].isdigit():
            print(str(ingredient_ids[int(i)]) + " is not an accepted ID. Could not add.")
            loading_animation(2)
            continue
        c.execute("SELECT ingredient_name from ingredients WHERE ingredient_id = ?", (ingredient_ids[int(i)],))
        ingredient_name = c.fetchone()[0]
        quantity = input("Input the quantity for " + ingredient_name + ": " )
        loading_animation(2)
    
        c.execute("INSERT INTO recipe_lines (recipe_id, ingredient_id, quantity) VALUES (?,?,?)", (recipe_id, ingredient_ids[int(i)], quantity))
        db.commit()

    print("Recipe #" + str(recipe_id) + "(" + recipe_name + ") added! ")

    db.close()

def recipe_remove():
    # warning animation
    for i in range(3):
        print("""
              *** WARNING ***
              """)
        time.sleep(1)
    print("""
          PLEASE READ:
          DELETING A RECIPE IS IRREVERSIBLE!!!
          ENSURE THAT RECIPE SELECTED IS THE ONE TO BE DELETED!!!

          INPUT 'CONTINUE' TO PROCEED WITH RECIPE REMOVAL.
          OTHERWISE PROGRAM WILL RETURN TO THE MAIN MENU.
          """)
    loading_animation(2)

    cont = input("Input 'CONTINUE' to proceeed: ")
    loading_animation(2)

    if cont == 'CONTINUE':
        show_recipes()
        loading_animation(2)
    
    else:
        print("CONTINUE not entered. Returning to main menu...")
        loading_animation(2)

    # connecting to the database
    db = sqlite3.connect("recipe_finder.db")
    db.execute("PRAGMA foreign_keys = ON")

    # cursor object c
    c = db.cursor()

    recipe_id = input("Please enter recipe ID of recipe you wish to delete: ")
    loading_animation(2)

    # get name of ingrdient to display to user for confirmation
    name_query = ("SELECT recipe_name FROM recipes WHERE recipe_id = ?")
    c.execute(name_query, (recipe_id,))
    recipe_name = c.fetchone()[0]

    # executing delete query
    c.execute("DELETE FROM recipes WHERE recipe_id = ?", (recipe_id,))
    db.commit()

    print("'" + recipe_name + "' deleted.")

    db.close()    

def show_favorites():

    # connecting to the database
    db = sqlite3.connect("recipe_finder.db")
    db.execute("PRAGMA foreign_keys = ON")

    # cursor object c
    c = db.cursor()
        
    favorites = []
    # open favorites and store numbers into array
    with open('favorites.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.replace("\n", "").isdigit():
                favorites.append(int(line.replace("\n", "")))

    # table to display favorites
    fav_table = PrettyTable()
    fav_table.hrules = ALL      # horizontal separators
    fav_table.field_names = ['ID', 'Recipe', 'Description']       # column titles
    fav_table._max_width = {"ID" : 10, "Recipe" : 25, "Description" : 75} # max width for columns
    fav_table.align["Description"] = "l"    # left align description column

    for favorite in favorites:
        fav_recipe = c.execute("SELECT recipe_id, recipe_name, recipe_description FROM recipes WHERE recipe_id = ?", (favorite,))
        fav_table.add_rows(fav_recipe)

    print(fav_table)

    return favorites

def favorites():

    fav_cmd = ""
    loading_animation(2)
    while fav_cmd != "0": 
        print("""
              FAVORITES MENU
              [1] View Favorites
              [2] Add recipe to Favorites
              [3] Remove recipe from Favorites
              
              
              [0] EXIT Favorites

          """)

        fav_cmd = input("Input a number, then press enter: ")
        loading_animation(2)

        # view favorites
        if fav_cmd == "1":
            favorites = show_favorites()
            loading_animation(2)
            print("""
                  To view a favorite recipe, enter the correct ID and press enter.
                  Otherwise, program will return to Favorites Menu.
                  """)
            loading_animation(2)

            view_fav = input("Enter an ID, or return to Favorites Menu: ")
            loading_animation(2)

            # check if input is correct format
            if view_fav.isdigit():
                view_fav = int(view_fav)

                # check if ID is in favorites
                if view_fav in favorites:
                    # connecting to the database
                    db = sqlite3.connect("recipe_finder.db")
                    db.execute("PRAGMA foreign_keys = ON")

                    # cursor object c
                    c = db.cursor()
                    # query for recipe name
                    name_query = ("SELECT recipe_name FROM recipes WHERE recipe_id = ?")
                    recipe_name = c.execute(name_query, (view_fav,))
                    recipe_name = c.fetchone()[0]

                    # query for recipe instructions
                    instructions_query = ("SELECT recipe_instructions FROM recipes WHERE recipe_id = ?")
                    instructions = c.execute(instructions_query, (view_fav,))
                    instructions = c.fetchone()[0]

                    # query for source
                    source_query = ("Select recipe_source FROM recipes WHERE recipe_id = ?")
                    source = c.execute(source_query, (view_fav,))
                    source = c.fetchone()[0]

                    # query for ingredients line
                    line_query = ("SELECT recipe_lines.quantity, ingredients.ingredient_name FROM recipe_lines INNER JOIN ingredients ON recipe_lines.ingredient_id = ingredients.ingredient_id WHERE recipe_lines.recipe_id = ?")
                    recipe_lines = c.execute(line_query, (view_fav,))

                    line_table = PrettyTable()
                    line_table.hrules = ALL      # horizontal separators
                    line_table.field_names = ['Quantity', 'Ingredient']       # column titles
                    line_table._max_width = {"Quantity" : 50, "Ingredient" : 50} # max width for columns
                    line_table.align["Ingredient"] = "l"    # left align ingredient column
                    line_table.add_rows(recipe_lines)

                    loading_animation(5)

                    print("You selected the recipe '" + recipe_name + "'. Here are the ingredients" )
                    loading_animation(2)
                    print(line_table)
                    loading_animation(5)

                    print("Here are the instructions: ")
                    loading_animation(2)
                    print(instructions)

                    loading_animation(5)

                    print("For more information, visit the recipe source: ")
                    loading_animation(2)
                    print(source)

                else:
                    print("It seems that the ID input is not in your favorites. Please check input and try again.")
                    loading_animation(2)
            else:
                print("It seems that the ID input is not in your favorites. Please check input and try again.")
                fav_cmd = ""
                loading_animation(2)
        
        # add favorite
        if fav_cmd == "2":
            favorites = show_favorites()
            loading_animation(2)
            print("""
                  As a reminder, these are your current favorites.
                  To add a favorite please input a recipe ID:
                  """)
            loading_animation(2)

            add_fav = input("Input an ID to add to your favorites: ")
            loading_animation(2)
            if add_fav.isdigit():
                add_fav = int(add_fav)
                if add_fav not in favorites:
                    with open("favorites.txt", 'w+') as file:
                        file.write("ADD\n" + str(add_fav))
                    print("Favorite added!")
                    show_favorites()
                    loading_animation(2)

                else:
                    print("Entered ID is alread in your favorites. Please check input and try again.")
                    loading_animation(2)
            else:
                print("Invalid input. Please try again.")
                loading_animation(2)

        # remove favorite
        if fav_cmd == "3":
            favorites = show_favorites()
            loading_animation(2)
            print("""
                  As a reminder, these are your current favorites.
                  To remove a favorite please input a recipe ID:
                  """)
            loading_animation(2)

            remove_fav = input("Input an ID to remove from your favorites: ")
            loading_animation(2)
            if remove_fav.isdigit():
                remove_fav = int(remove_fav)
                if remove_fav in favorites:
                    with open("favorites.txt", 'w+') as file:
                        file.write("REMOVE\n" + str(remove_fav))
                    print("Favorite removed!")
                    show_favorites()
                    loading_animation(2)

                else:
                    print("Entered ID is not in your favorites. Please check input and try again.")
                    loading_animation(2)
            else:
                print("Invalid input. Please try again.")
                loading_animation(2)
# ~~~~~~~~~~~~~~~~~~~~~~~ MAIN PROGRAM ~~~~~~~~~~~~~~~~~~~~~~~ #
# initialize values
if __name__ == '__main__':

    # run microservice
    microservice = subprocess.Popen(["microservice.exe"], creationflags=subprocess.DETACHED_PROCESS)

    print(r" ____           _              _____ _           _                   _   ___")
    time.sleep(1)
    print(r"|  _ \ ___  ___(_)_ __   ___  |  ___(_)_ __   __| | ___ _ __  __   _/ | / _ \ ")
    time.sleep(1)
    print(r"| |_) / _ \/ __| | '_ \ / _ \ | |_  | | '_ \ / _` |/ _ \ '__| \ \ / / || | | |")
    time.sleep(1)
    print(r"|  _ <  __/ (__| | |_) |  __/ |  _| | | | | | (_| |  __/ |     \ V /| || |_| |")
    time.sleep(1)
    print(r"|_| \_\___|\___|_| .__/ \___| |_|   |_|_| |_|\__,_|\___|_|      \_/ |_(_)___/")
    time.sleep(1)
    print(r"                 |_|                                                          ")
    
    # reset cmd before program start
    cmd = ""
    loading_animation(2)
    while cmd != "0":

        # reset command after each function
        cmd = ""
        
        # welcome message and cmd prompts
        print("""
              Welcome to Recipe Finder v1.0!

              Please select an option:

              [1] Search for recipe
              [2] Search for ingredient
              [3] Add ingredient to database
              [4] Add recipe to database
              [5] View recipe
              [6] Favorites
              [7] Delete ingredient from database
              [8] Delete recipe from database
              [9] Re-initialize database

              [0] EXIT
              """)
        
        # user input for cmd
        loading_animation(2)
        cmd = input("Input a number, then press 'ENTER': ")
        loading_animation(2)

        # confirmation that correct option was selected
        print("You selected option " + cmd + ". Is this correct?")
        loading_animation(2)
        confirm = input("Press enter to continue or type 'RESTART' to restart program: ")
        loading_animation(2)
        if confirm == "RESTART":
            cmd = ""

        # recipe search
        elif cmd == "1":
            recipe = input("Please input recipe: ")
            loading_animation(2)
            recipe_search(recipe)

        # ingredient search
        elif cmd == "2":
            ingredient = input("Please input ingredient: ")
            loading_animation(2)
            ingredient_search(ingredient)

        # add ingredient
        elif cmd == "3":
            added_ingredient = input("Enter an ingredient name to add: ")
            loading_animation(2)
            ingredient_add(added_ingredient)

        # add recipe
        elif cmd == "4":
            print("""
                  PLEASE READ:
                  Before adding a recipe, ensure that all ingredients are already added to the database.

                  If you would like to see all the ingredients before continuing, please enter 'YES'.
                  Otherwise, the Add Recipe Wizard will continue.
                  """)
            
            loading_animation(2)
                  
            ingredient_cmd = input("Would you like to view all the ingredients in the database?: ")
            if ingredient_cmd == "YES":
                show_ingredients()

            print("Are all the ingredients for your recipe in the database?")
            ingredient_cmd = input("Type 'NO' to exit. Otherwise, installer will continue: ")

            if ingredient_cmd != "NO":
                recipe_add()
        
                
        # view recipe
        elif cmd == "5":
            recipe_view()
            loading_animation(2)

        # favorites
        elif cmd == "6":
            favorites()
            loading_animation(2)
        
        # remove ingredient
        elif cmd == "7":
            ingredient_remove()
            loading_animation(2)

        # removce recipe
        elif cmd == "8":
            recipe_remove()
            loading_animation(2)
            
        # re-initialize db    
        elif cmd == "9":
            subprocess.run(["python", "db_initialize.py"])
            print("Database has been re-initialized with default data.")
            loading_animation(2)

        # exit
        elif cmd == "0":
            loading_animation(2)
            print("""
                Thank you for using Recipe Finder
                Now exiting...
                """)
            # stop microservice
            microservice.kill()
            loading_animation(2)

        # invalid input, program restarted.
        else:
            print("Invalid input. Please try again.")
            loading_animation(2)
