from re import T
import sqlite3
import time
from tkinter import ALL
from prettytable import PrettyTable, ALL
import db_initialize
def loading_animation(x):
    for i in range(x):
        time.sleep(1)
        print("*")

def ingredient_search(ingredient):
    # connecting to the database
    db = sqlite3.connect("recipe_finder.db")
    db.execute("PRAGMA foreign_keys = ON")

    # cursor object c
    c = db.cursor()

    # Ingredient Search SQL Query
    query = ("SELECT ingredient_name, ingredient_description FROM ingredients WHERE ingredient_name LIKE ? COLLATE NOCASE")
    
    # execute search query
    c.execute(query, (ingredient,))

    # execute search query
    results = c.execute(query, ("%" + ingredient + "%",))

    # check if ingredient exists in DB
    if c.fetchone() == None:
        loading_animation(2)
        print("Sorry. No ingredients with the word '" + ingredient + "' are found in the database. Please try again.")
        return

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

    db.close()

def recipe_search(recipe):

    # connecting to the database
    db = sqlite3.connect("recipe_finder.db")
    db.execute("PRAGMA foreign_keys = ON")

    # cursor object c
    c = db.cursor()

    # Recipe Search SQL Query
    query = ("SELECT recipe_name, recipe_description FROM recipes WHERE recipe_name LIKE ? COLLATE NOCASE")

    # execute search query
    results = c.execute(query, ("%" + recipe + "%",))

    # check if recipe exists in DB.
    if c.fetchone() == None:
        loading_animation(2)
        print("Sorry. No recipes with the word '" + recipe + "' are found in the database. Please try again.")
        return
    
   
    #format data with PrettyTable
    table = PrettyTable()
    table.hrules = ALL      # horizontal separators
    table.field_names = ['Recipe', 'Description']       # column titles
    table._max_width = {"Recipe" : 25, "Description" : 75} # max width for columns
    table.align["Description"] = "l"    # left align description column
    table.add_rows(results) # add rows to table

    print("Here are the recipes that contain the word '" + recipe + "'.")
    loading_animation(3)
    print(table)
    
    db.close()           

def ingredient_add(added_ingredient):
    
    # query database to check for ingredient
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

    # if recipe does not exist, rerun recipe_view
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
    

    



# ~~~~~~~~~~~~~~~~~~~~~~~ MAIN PROGRAM ~~~~~~~~~~~~~~~~~~~~~~~
# initialize values
cmd = 9
loading_animation(2)
while cmd != 0:
    # welcome message and cmd prompts
    print("""
          Hello. Welcome to Recipe Finder v0.1. Please select an option:
          [1] Search for recipe
          [2] Search for ingredient
          [3] Add ingredient to database
          [4] Add recipe to database
          [5] View recipe
          [6] Favorites
          [0] EXIT
          
      """)
    # user input for cmd
    loading_animation(2)
    cmd = int(input("Input a number, then press 'ENTER': "))
    loading_animation(2)

    # confirmation that correct option was selected
    print("You selected option " + str(cmd) + ". Is this correct?")
    loading_animation(2)
    confirm = input("Press enter to continue or type 'RESTART' to restart program: ")
    if confirm == "RESTART":
        cmd = 9

    # recipe search selected
    elif cmd == 1:
        loading_animation(2)
        recipe = input("Please input recipe: ")
        loading_animation(2)
        recipe_search(recipe)

    # ingredient search selected
    elif cmd == 2:
        loading_animation(2)
        ingredient = input("Please input ingredient: ")
        loading_animation(2)
        ingredient_search(ingredient)

    # add ingredient selected
    elif cmd == 3:
        loading_animation(2)
        added_ingredient = input("Enter an ingredient name to add: ")
        loading_animation(2)
        ingredient_add(added_ingredient)

    # view recipe selected
    elif cmd == 5:
        recipe_view()

    # exit selected
    elif cmd == 0:
        loading_animation(2)
        print("""
            Thank you for using Recipe Finder
            Now exiting...
            """)
        loading_animation(2)

    # invalid input, program restarted.
    else:
        loading_animation(2)
        print("Invalid input. Please try again.")
        loading_animation(2)
        # reset variable
        cmd = 9
