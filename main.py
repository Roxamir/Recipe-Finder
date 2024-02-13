import psycopg2
 
# connecting to the mysql server
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

# user input for ingredient search
ingredient = input("Search for an ingredient: ")



c.execute(query, ("%" + ingredient + "%",))
 
# printing all the ingredients
results = c.fetchall()

for result in results:
    print(result)
 
# finally closing the database connection
db.close()
