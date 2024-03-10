
import sqlite3
from prettytable import PrettyTable, ALL

# connecting to the database
db = sqlite3.connect("recipe_finder.db")
db.execute("PRAGMA foreign_keys = ON")

# cursor object c
c = db.cursor()

fav_cmd = ""

while fav_cmd != "0":

    fav_cmd = ""
    favorites = []
    
    print("""
            FAVORITES MENU
            [1] View Favorites
            [2] Add recipe to Favorites
            [3] Remove recipe from Favorites
            
            
            [0] EXIT Favorites

        """)

    fav_cmd = input("Input a number, then press enter: ")

    if fav_cmd == "1":
        favorites = []
        # open favorites and store numbers into array
        with open('favorites.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
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

        print("""
              To view a favorite recipe, enter the correct ID and press enter.
              Otherwise, program will return to Favorites Menu.
              """)
        
        view_fav = input("Enter an ID, or return to Favorites Menu: ")

        # check if input is correct format
        if view_fav.isdigit():
            view_fav = int(view_fav)

            # check if ID is in favorites
            if view_fav in favorites: 
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

                # loading_animation(5)

                print("You selected the recipe '" + recipe_name + "'. Here are the ingredients" )
                #loading_animation(2)
                print(line_table)
                #loading_animation(5)

                print("Here are the instructions: ")
                #loading_animation(2)
                print(instructions)

                #loading_animation(5)

                print("For more information, visit the recipe source: ")
                #loading_animation(2)
                print(source)

            else:
                print("It seems that the ID input is not in your favorites. Please check input and try again.")
            
        else:
            print("It seems that the ID input is not in your favorites. Please check input and try again.")

db.close()