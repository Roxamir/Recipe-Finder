import mysql.connector
 
# connecting to the mysql server
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Kawrcrc10717!!",
    database="recipe_finder"
)
 
# cursor object c
c = db.cursor()

# Ingredient Search SQL Query
query = ("SELECT ingredientName, ingredientDescription FROM ingredients WHERE ingredientName LIKE %s")

# user input for ingredient search
ingredient = input("Search for an ingredient: ")



c.execute(query, ("%" + ingredient + "%",))
 
# printing all the ingredients
for i in c:
    print(i)
c = db.cursor()
 
# finally closing the database connection
db.close()
