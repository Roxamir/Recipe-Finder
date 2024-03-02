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
            

def recipe_add():
    print("""
          Hello! Welcome to the Add Ingredient Wizard.
          Follow the prompts to add an ingredient.
          To exit the wizard, type EXIT at any prompt.
          """) 

    added_ingredient = input("Enter an ingredient name to add: ")

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


    


# ~~~~~~~~~~~~~~~~~~~~~~~ MAIN PROGRAM ~~~~~~~~~~~~~~~~~~~~~~~
# initialize values
cmd = 9

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