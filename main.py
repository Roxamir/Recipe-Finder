import psycopg2
import time

def ingredient_search(ingredient):

    # connecting to the postgres server
    db = psycopg2.connect(
    database="recipe_finder",
    host="localhost",
    user="postgres",
    password="cs361",
    port="5432"
    )

    # cursor object c
    c = db.cursor()

    # Ingredient Search SQL Query
    query = ("SELECT ingredient_name, ingredient_description FROM ingredients WHERE ingredient_name ILIKE %s")
    
    # execute search query
    c.execute(query, ("%" + ingredient + "%",))

    # searching animation
    print("Searching")
    for i in range(0,5):
        time.sleep(1)
        print("*")

    # storing results and printing matching ingredients
    results = c.fetchall()
    for result in results:
        print(result)
        print("\n")

    # closing the database connection
    db.close()

def recipe_search(recipe):

    # connecting to the postgres server
    db = psycopg2.connect(
    database="recipe_finder",
    host="localhost",
    user="postgres",
    password="cs361",
    port="5432"
    )

    # cursor object c
    c = db.cursor()

    # Recipe Search SQL Query
    query = ("SELECT recipe_name, recipe_description FROM recipes WHERE recipe_name ILIKE %s")

    # execute search query
    c.execute(query, ("%" + recipe + "%",))

    # searching animation
    print("Searching")
    for i in range(0,5):
        time.sleep(1)
        print("*")

    # storing results and printing matching ingredients
    results = c.fetchall()
    for result in results:
        print(result)
        print("/n")

    # closing the database connection
    db.close()


cmd = 9

while cmd != 0:
    print("""
    Hello. Welcome to Recipe Finder v0.1. Pl an option:
    
    [1] Search for recipe
    [2] Search for ingredient
    [0] EXIT
          
      """)
    cmd = int(input("Input a number then press 'ENTER': "))

    if cmd == 1:
        recipe = input("Please input recipe: ")
        recipe_search(recipe)
    elif cmd == 2:
        ingredient = input("Please input ingredient: ")
        ingredient_search(ingredient)