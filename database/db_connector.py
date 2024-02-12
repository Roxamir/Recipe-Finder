# Python implementation to create a Database in MySQL
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
 
# fetching all the databases
c.execute("SHOW TABLES")
 
# printing all the databases
for i in c:
    print(i)
c = db.cursor()
 
# finally closing the database connection
db.close()