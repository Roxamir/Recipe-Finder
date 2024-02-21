import sqlite3
import time

db = sqlite3.connect("recipe_finder.db")
db.execute("PRAGMA foreign_keys = ON")
c = db.cursor()
# 

def create_db():
    # create recipes, ingredients and recipe_lines tables
    c.executescript("""
                    CREATE TABLE recipes(
                    recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    recipe_name VARCHAR(50), recipe_cuisine VARCHAR(50),
                    recipe_description TEXT, recipe_instructions TEXT
                    );
                    
                    CREATE TABLE ingredients(
                    ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ingredient_name VARCHAR(50),
                    ingredient_description TEXT
                    );
                    
                    CREATE TABLE recipe_lines(
                    line_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    recipe_id INTEGER NOT NULL,
                    ingredient_id INTEGER NOT NULL,
                    quantity DECIMAL,
                    unit VARCHAR(50),
                    FOREIGN KEY(recipe_id) REFERENCES recipes(recipe_id)
                        ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY(ingredient_id) REFERENCES ingredients(ingredient_id)
                        ON DELETE CASCADE ON UPDATE CASCADE
                    );
                    """)
    
def insert_data():
    # insert recipe data
    c.executescript("""
                    INSERT INTO recipes(recipe_name, recipe_cuisine, recipe_description, recipe_instructions)
                    VALUES(
                    'Chocolate Chip Cookies',
                    'American',
                    'A chocolate chip cookie is a drop cookie that features chocolate chips or chocolate morsels as its distinguishing ingredient.',
                    'In the bowl of an electric mixer fitted with the paddle attachment or beaters, beat the butter and both sugars on medium speed (or high speed if using a hand mixer) for 3 minutes, or until light and fluffy, scraping down the sides and bottom of the bowl as necessary. Add the vanilla and eggs and beat for 2 minutes more. Scrape down the bowl. Add the salt and baking soda and beat briefly until evenly combined. Add the flour and mix on low speed until the dough is uniform. Mix in the chocolate chips.
                    Cover the bowl with plastic wrap or scrape the dough into an airtight container and let rest in the refrigerator until firm, a few hours or overnight. (Alternatively, if you do not want to wait, form the dough into balls on the baking sheets as instructed below, and chill in the fridge until firm, about 30 minutes.)
                    Preheat the oven to 350°F and set a rack in the middle position. Line a 13 x 18-inch baking sheet with parchment paper.
                    Drop the dough in firmly packed 1.5-tablespoon balls onto the prepared baking sheet, spacing them about 2 inches apart. (I use a #40/1.5-T cookie scoop with a wire trigger.) For thick cookies, it is important to really pack the dough in the scooper or with your hands. Bake for 11 to 13 minutes, until golden around the edges but still soft and pale in the center. Let cool for a few minutes on the baking sheet, then transfer to a wire rack to cool completely. Repeat with the remaining cookie dough, refrigerating the dough between batches. The cookies will keep in an airtight container at room temperature for up to 3 days.
                    Note: I highly recommend King Arthur All-Purpose Flour for this recipe - it is higher in protein than other brands and helps the cookies plump up and hold their shape.
                    Freezer-Friendly Instructions: The cookie dough can be frozen for up to 3 months. To freeze, roll the dough into balls, let set on a baking sheet in the freezer for about 1 hour, then place in a sealable bag and press out as much air as possible. Bake as needed directly from the freezer. (Allow 1 to 2 minutes longer in the oven.) The baked cookies can also be frozen for up to 3 months. Let the cookies cool completely and store in an airtight container separating layers with parchment paper or aluminum foil. Before serving, remove the cookies from the container and let them come to room temperature.');
                    """)
    
insert_data()