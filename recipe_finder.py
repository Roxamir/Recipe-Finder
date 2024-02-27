import sqlite3
import time
from tkinter import ALL
from prettytable import PrettyTable, ALL
import db_initialize

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

    #format data with PrettyTable
    table = PrettyTable()
    table.hrules = ALL      # horizontal separators
    table.field_names = ['Ingredient', 'Description']       # column titles
    table._max_width = {"Ingredient" : 25, "Description" : 75} # max width for columns
    table.align["Description"] = "l"    # left align description column
    table.add_rows(results) # add rows to table

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
    
   
    #format data with PrettyTable
    table = PrettyTable()
    table.hrules = ALL      # horizontal separators
    table.field_names = ['Recipe', 'Description']       # column titles
    table._max_width = {"Recipe" : 25, "Description" : 75} # max width for columns
    table.align["Description"] = "l"    # left align description column
    table.add_rows(results) # add rows to table
    print(table)
    
    db.close()

def favorite_recipes():
    # connecting to the database
    db = sqlite3.connect("recipe_finder.db")
    db.execute("PRAGMA foreign_keys = ON")

    # cursor object c
    c = db.cursor()

    fav_cmd = 9

    print("~~~~~~~ FAVORITES ~~~~~~~")

    print("""
          Please select an option:
          
          [1] View Favorites
          [2] Add Favorite
          [3] Remove Favorite

          [0] Return to Main Menu


          """)
    while fav_cmd != 0:

        fav_cmd = input("Input a number, then press ENTER: ")
    
        print("\nYou selected option " + str(fav_cmd) + ". Is this correct?")
        fav_confirm = input("\nPress ENTER to continue or type 'NO' to select again: ")

        if fav_confirm == 'NO':
            # reset variables
            fav_confirm = 'YES'
            fav_cmd = 9
        
        # view favorites
        if fav_cmd == 1:
            






def recipe_add():
    print("""
          Hello! Welcome to the Add Recipe Wizard.
          Follow the prompts to add a recipe.
          To exit the wizard, type EXIT at any prompt.
          """)  


# initialize values
cmd = 9

while cmd != 0:
    # welcome message and cmd prompts
    print("""
    Hello. Welcome to Recipe Finder v0.1. Please select an option:
    
    [1] Search for recipe
    [2] Search for ingredient
    [0] EXIT
          
      """)
    # user input for cmd
    cmd = int(input("Input a number, then press 'ENTER': "))

    # confirmation that correct option was selected
    print("\nYou selected option " + str(cmd) + ". Is this correct?")
    confirm = input("\nPress enter to continue or type 'RESTART' to restart program: ")
    if confirm == "RESTART":
        cmd == 9
    # recipe search selected
    elif cmd == 1:
        recipe = input("\nPlease input recipe: ")
        recipe_search(recipe)
    # ingredient search selected
    elif cmd == 2:
        ingredient = input("\nPlease input ingredient: ")
        ingredient_search(ingredient)
    # exit selected
    elif cmd == 0:
        print("""
            Thank you for using Recipe Finder
            Now exiting...
            """)
    # invalid input, program restarted.
    else:
        print("\nInvalid input. Please try again.")

    # reset variable
    cmd = 9