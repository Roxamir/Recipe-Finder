import sqlite3
import time

db = sqlite3.connect("recipe_finder.db")
db.execute("PRAGMA foreign_keys = ON")
c = db.cursor()
# 

def create_db():
    # create recipes, ingredients and recipe_lines tables. if table exists, it is reinitailized.
    c.executescript("""
                    DROP TABLE IF EXISTS [recipes];
                    CREATE TABLE recipes(
                    recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    recipe_name VARCHAR(50) UNIQUE,
                    recipe_description TEXT,
                    recipe_instructions TEXT,
                    recipe_source TEXT
                    );
                    
                    DROP TABLE IF EXISTS [ingredients];
                    CREATE TABLE ingredients(
                    ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ingredient_name VARCHAR(50) UNIQUE,
                    ingredient_description TEXT
                    );

                    DROP TABLE IF EXISTS [recipe_lines];
                    CREATE TABLE recipe_lines(
                    line_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    recipe_id INTEGER NOT NULL,
                    ingredient_id INTEGER NOT NULL,
                    quantity VARCHAR(50),
                    FOREIGN KEY(recipe_id) REFERENCES recipes(recipe_id)
                        ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY(ingredient_id) REFERENCES ingredients(ingredient_id)
                        ON DELETE CASCADE ON UPDATE CASCADE
                    );
                    """)
    
def insert_data():
    # insert recipe data into recipes table
    c.executescript("""
                    INSERT INTO recipes(recipe_name, recipe_description, recipe_instructions, recipe_source)
                    VALUES(
                    'Chocolate Chip Cookies',
                    'A chocolate chip cookie is a drop cookie that features chocolate chips or chocolate morsels as its distinguishing ingredient.',
                    'Preheat oven to 375 degrees F. Line three baking sheets with parchment paper and set aside.
In a medium bowl mix flour, baking soda, baking powder and salt. Set aside.
Cream together butter and sugars until combined.
Beat in eggs and vanilla until light (about 1 minute).
Mix in the dry ingredients until combined.
Add chocolate chips and mix well.
Roll 2-3 Tablespoons (depending on how large you like your cookies) of dough at a time into balls and place them evenly spaced on your prepared cookie sheets.
Bake in preheated oven for approximately 8-10 minutes.
Take them out when they are just barely starting to turn brown.
Let them sit on the baking pan for 2 minutes before removing to cooling rack.',
                    'https://joyfoodsunshine.com/the-most-amazing-chocolate-chip-cookies/'
                    );
                    
                    INSERT INTO recipes(recipe_name, recipe_description, recipe_instructions, recipe_source)
                    VALUES(
                    'Grilled Cheese',
                    'The grilled cheese (sometimes known as a toasted sandwich or cheese toastie) is a hot cheese sandwich typically prepared by heating slices of cheese between slices of bread with a cooking fat such as butter or mayonnaise on a frying pan, griddle, or sandwich toaster, until the bread browns and the cheese melts.',
                    'In a large bowl, beat cream cheese and mayonnaise until smooth.
Stir in the cheeses, garlic powder and seasoned salt.
Spread 5 slices of bread with the cheese mixture, about 1/3 cup on each.
Top with remaining bread.
Butter the outsides of sandwiches.
In a skillet over medium heat, toast sandwiches for 4-5 minutes on each side or until bread is lightly browned and cheese is melted.',
                    'https://www.tasteofhome.com/recipes/the-ultimate-grilled-cheese/'
                    );

                    INSERT INTO recipes(recipe_name, recipe_description, recipe_instructions, recipe_source)
                    VALUES(
                    'Spinach-Mushroom Scrambled Eggs',
                    'A simple and classic breakfast dish that incorporates eggs, spinach and mushrooms.',
                    'In a small bowl, whisk eggs, egg whites, salt and pepper until blended.
In a small nonstick skillet, heat butter over medium-high heat.
Add mushrooms; cook and stir 3-4 minutes or until tender.
Add spinach; cook and stir until wilted. Reduce heat to medium.
Add egg mixture; cook and stir just until eggs are thickened and no liquid egg remains.
Stir in cheese.',
                    'https://www.tasteofhome.com/recipes/spinach-mushroom-scrambled-eggs/'
                    );

                    INSERT INTO recipes(recipe_name, recipe_description, recipe_instructions, recipe_source)
                    VALUES(
                    'Roasted Tomato Soup',
                    'Tomato soup is a soup with tomatoes as the primary ingredient.
It can be served hot or cold, and may be made in a variety of ways.
It may be smooth in texture, and there are also recipes that include chunks of tomato, cream, chicken or vegetable stock, vermicelli, chunks of other vegetables and meatballs.
Many companies have their own versions of tomato soup which all vary in taste, portions and ingredients.',
                    'Preheat oven to 400°.
Place tomatoes, onion and garlic in a greased 15x10x1-in. baking pan.
Drizzle with oil, sprinkle with thyme, salt and pepper and toss to coat.
Roast until tender, 25-30 minutes, stirring once. Cool slightly.
Working in batches, process tomato mixture and basil leaves in a blender until smooth.
Transfer to a large saucepan; heat through. If desired, top with croutons and fresh basil.',
                    'https://www.tasteofhome.com/recipes/roasted-tomato-soup-with-fresh-basil/'
                    );  

                    INSERT INTO recipes(recipe_name, recipe_description, recipe_instructions, recipe_source)
                    VALUES(
                    'Garlic Bread',
                    'Garlic bread (also called garlic toast) consists of bread (usually a baguette, sour dough, or bread such as ciabatta), topped with garlic and occasionally olive oil or butter and may include additional herbs, such as oregano or chives.
It is then either grilled until toasted or baked in a conventional or bread oven.',
                    'In a small bowl, mix the butter, cheese, basil, parsley and garlic until blended.
Cut baguette crosswise in half; cut each piece lengthwise in half.
Spread cut sides with butter mixture.
Place on an ungreased baking sheet.
Bake, uncovered, at 425° until lightly toasted, 7-9 minutes.
Sprinkle with goat cheese; bake until goat cheese is softened, 1-2 minutes longer.
Cut into smnaller slices.',
                    'https://www.tasteofhome.com/recipes/herb-happy-garlic-bread/'
                    );  

                    INSERT INTO recipes(recipe_name, recipe_description, recipe_instructions, recipe_source)
                    VALUES(
                    'Spaghetti Sauce',
                    'A tomato sauce typically served with spaghetti. Usually contains herbs and meat.',
                    'In a Dutch oven, cook the beef, sausage, onions and garlic over medium heat until meat is no longer pink; drain.
Transfer to a 5-qt. slow cooker.
Stir in the tomatoes, tomato paste, water, sugar, Worcestershire sauce, oil and seasonings.
Cook, covered, on low 8-10 hours. Discard bay leaves. Serve with spaghetti.',
                    'https://www.tasteofhome.com/recipes/stamp-of-approval-spaghetti-sauce/'
                    );  

                    INSERT INTO recipes(recipe_name, recipe_description, recipe_instructions, recipe_source)
                    VALUES(
                    'Guacamole',
                    'Guacamole is an avocado-based dip, spread, or salad first developed in Mexico.
In addition to its use in modern Mexican cuisine, it has become part of international cuisine as a dip, condiment and salad ingredient.',
                    'Mash avocados with garlic and salt. Stir in remaining ingredients, adding tomatoes and mayonnaise if desired.',
                    'https://www.tasteofhome.com/recipes/homemade-guacamole/'
                    );  

                    INSERT INTO recipes(recipe_name, recipe_description, recipe_instructions, recipe_source)
                    VALUES(
                    'Chicken Noodle Soup',
                    'Chicken soup is a soup made from chicken, simmered in water, usually with various other ingredients.
The classic chicken soup consists of a clear chicken broth, often with pieces of chicken or vegetables; common additions are pasta, noodles, dumplings, or grains such as rice and barley.
Chicken soup has acquired the reputation of a folk remedy for colds and influenza, and in many countries is considered a comfort food.',
                    'Pat chicken dry with paper towels; sprinkle with salt and pepper.
In a 6-qt. stockpot, heat oil over medium-high heat.
Add chicken in batches, cook until dark golden brown, 3-4 minutes.
Remove chicken from pan; discard all but 2 tablespoons drippings.
Add onion to drippings; cook and stir over medium-high heat until tender, 4-5 minutes.
Add garlic; cook 1 minute longer.
Add broth, stirring to loosen browned bits from pan. Bring to a boil.
Return chicken to pan.
Add celery, carrots, bay leaves and thyme.
Reduce heat; simmer, covered, until chicken is tender, 25-30 minutes.
Transfer chicken to a plate. Remove soup from heat.
Add noodles; let stand, covered, until noodles are tender, 20-22 minutes.
Meanwhile, when chicken is cool enough to handle, remove meat from bones; discard bones. Shred meat into bite-sized pieces.
Return meat to stockpot. Stir in parsley and lemon juice.
If desired, adjust seasoning with additional salt and pepper. Discard bay leaves.',
                    'https://www.tasteofhome.com/recipes/the-ultimate-chicken-noodle-soup/'
                    );  

                    INSERT INTO recipes(recipe_name, recipe_description, recipe_instructions, recipe_source)
                    VALUES(
                    'Banana Bread',
                    'Banana bread is a type of sweet bread made from mashed bananas.
It is often a moist and sweet quick bread but some recipes are yeast raised.',
                    'Preheat oven to 350°.
In a large bowl, stir together flour, sugar, baking soda and salt.
In another bowl, combine the eggs, bananas, oil, buttermilk and vanilla; add to flour mixture, stirring just until combined. If desired, fold in nuts.
Pour into a greased or parchment-lined 9x5-in. loaf pan. Bake until a toothpick comes out clean, 1-1/4 to 1-1/2 hours. Cool in pan for 15 minutes before removing to a wire rack.',
                    'https://www.tasteofhome.com/recipes/best-ever-banana-bread/'
                    );  

                    INSERT INTO recipes(recipe_name, recipe_description, recipe_instructions, recipe_source)
                    VALUES(
                    'Homemade Bread',
                    'Bread is a staple food prepared from a dough of flour (usually wheat) and water, usually by baking.
Throughout recorded history and around the world, it has been an important part of many cultures'' diet.
It is one of the oldest human-made foods, having been of significance since the dawn of agriculture, and plays an essential role in both religious rituals and secular culture.',
                    'In a large bowl, dissolve yeast in warm water.
Using a rubber spatula, stir in 3-1/2 cups flour and salt to form a soft, sticky dough. Do not knead.
Cover and let rise at room temperature 1 hour.
Stir down dough (dough will be sticky). Turn onto a floured surface; with floured hands pat into a 9-in. square.
Fold square into thirds, forming a 9x3-in. rectangle. Fold rectangle into thirds, forming a 3-in. square.
Place in a large greased bowl, turning once to grease the top. Cover and let rise at room temperature until almost doubled, about 1 hour.
Punch down dough and repeat folding process. Return dough to bowl; refrigerate, covered, overnight.
Grease the bottom of a disposable foil roasting pan with sides at least 4 in. high; dust pan with cornmeal.
Turn dough onto a floured surface. Knead gently 6-8 times; shape into a 6-in. round loaf. Place into prepared pan; dust top with remaining 1 tablespoon flour.
Cover pan and let rise at room temperature until dough expands to a 7-1/2-in. loaf, about 1-1/4 hours.
Preheat oven to 500°. Using a sharp knife, make a slash (1/4 in. deep) across top of loaf. Cover pan tightly with foil. Bake on lowest oven rack 25 minutes.
Reduce oven setting to 450°. Remove foil; bake bread until deep golden brown, 25-30 minutes. Remove loaf to a wire rack to cool.',
                    'https://www.tasteofhome.com/recipes/crusty-homemade-bread/'
                    );             
                    """)
    
    # insert ingredient data into ingredients table
    c.executescript("""
                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Butter (unsalted)',
                    'Butter is a dairy product made from the fat and protein components of churned cream.
It is a semi-solid emulsion at room temperature, consisting of approximately 80% butterfat.
It is used at room temperature as a spread, melted as a condiment, and used as a fat in baking, sauce-making, pan frying, and other cooking procedures.'
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Sugar',
                    'White sugar, also called table sugar, granulated sugar, or regular sugar, is a commonly used type of sugar, made either of beet sugar or cane sugar, which has undergone a refining process.'
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Brown Sugar',
                    'Brown sugar is a sucrose sugar product with a distinctive brown color due to the presence of molasses.
It is by tradition an unrefined or partially refined soft sugar consisting of sugar crystals with some residual molasses content (natural brown sugar), but is now often produced by the addition of molasses to refined white sugar (commercial brown sugar).'
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Vanilla Extract',
                    'Vanilla extract is a solution made by macerating and percolating vanilla pods in a solution of ethanol and water.
It is considered an essential ingredient in many Western desserts, especially baked goods like cakes, cookies, brownies, and cupcakes, as well as custards, ice creams, and puddings.
Although its primary flavor compound is vanillin, pure vanilla extract contains several hundred additional flavor compounds, which are responsible for its complex, deep flavor.'
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Eggs',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Egg Whites',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Salt',
                    ''
                    );

                     INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Black Pepper',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Baking Soda',
                    ''

                    );
                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'All Purpose Flour',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Chocolate Chips',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Mushrooms',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Spinach',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Shredded Provolone',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Tomatoes',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Onion',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Garlic',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Olive Oil',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Thyme',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Basil',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Cream Cheese',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Mayonnaise',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Cheddar Cheese',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Garlic Powder',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Italian Bread',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Romano Cheese',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Parsley',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'French Bread',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Goat Cheese',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Ground Beef',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Italian Sausage',
                    ''
                    );


                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Diced Tomatoes',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Tomato Paste',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Water',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Worcestershire Sauce',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Canola Oil',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Oregano',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Bay Leaves',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Marjoram',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Spaghetti',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Avocados',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Lime Juice',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Cilantro',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Chicken Thighs',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Chicken Broth',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Celery',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Carrots',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Egg Noodles',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Lemon Juice',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Bananas',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Buttermilk',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Walnuts',
                    ''
                    );


                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Active Dry Yeast',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Cornmeal',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Seasoned Salt',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Baking Powder',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Shredded Mozzarella',
                    ''
                    );

                    INSERT INTO ingredients (ingredient_name, ingredient_description)
                    VALUES(
                    'Sage',
                    ''
                    );
                    """)
    
    # insert recipe line data into recipe_lines table
    c.executescript("""
                    INSERT INTO recipe_lines(recipe_id, ingredient_id, quantity)
                    VALUES
                    (1, 1, '1 cup'),
                    (1, 2, '1 cup'),
                    (1, 3, '1 cup'),
                    (1, 4, '2 teaspoons'),
                    (1, 5, '2 large'),
                    (1, 7, '1 teaspoon'),
                    (1, 9, '1 teaspoon'),
                    (1, 56, '½ teaspoon'),
                    (1, 10, '3 cups'),
                    (1, 11, '2 cups'),

                    (2, 21, '3 ounces'),
                    (2, 22, '¾ cup'),
                    (2, 57, '1 cup'),
                    (2, 23, '1 cup'),
                    (2, 24, '½ teaspoon'),
                    (2, 25, '10 Slices (½ inch thick)'),
                    (2, 1, '2 tablespoons'),

                    (3, 5, '2 large'),
                    (3, 6, '2 large'),
                    (3, 7, '⅛ teaspoon'),
                    (3, 8, '⅛ teaspoon'),
                    (3, 1, '1 teaspoon'),
                    (3, 12, '½ cup'),
                    (3, 13, '½ cup'),
                    (3, 14, '2 tablespoons'),

                    (4, 15, '3½ pounds'),
                    (4, 16, '1 small'),
                    (4, 17, '2 cloves'),
                    (4, 18, '2 tablespoons'),
                    (4, 19, '2 tablespoons'),
                    (4, 7, '1 teaspoon'),
                    (4, 8, '¼ teaspoon'),
                    (4, 20, '12 leaves'),
                    
                    (5, 1, '½ cup'),
                    (5, 26, '¼ cup'),
                    (5, 20, '2 tablespoons'),
                    (5, 27, '1 tablespoon'),
                    (5, 3, '3 cloves'),
                    (5, 38, '1 baguette'),
                    (5, 29, '4 ounces'),

                    (6, 30, '2 pounds'),
                    (6, 31, '¾ pound'),
                    (6, 16, '4 medium'),
                    (6, 17, '8 cloves'),
                    (6, 32, '4 cans (14-½ ounces each)'),
                    (6, 33, '4 cans (6 ounces each)'),
                    (6, 34, '½ cup'),
                    (6, 2, '¼ cup'),
                    (6, 35, '¼ cup'),
                    (6, 36, '1 tablespoon'),
                    (6, 27, '¼ cup'),
                    (6, 20, '2 tablespoons'),
                    (6, 37, '1 tablespoon'),
                    (6, 38, '4'),
                    (6, 58, '1 teaspoon'),
                    (6, 7, '½ teaspoon'),
                    (6, 39, '½ teaspoon'),
                    (6, 8, '½ teaspoon'),

                    (7, 41, '3 medium'),
                    (7, 17, '1 clove'),
                    (7, 7, '¼-½ teaspoon'),
                    (7, 16, '1 small'),
                    (7, 42, '1-2 tablespoons'),
                    (7, 43, '1 tablespoon'),
                    (7, 15, '2 medium'),
                    (7, 22, '¼ cup'),

                    (8, 44, '2½ pounds (bone-in)'),
                    (8, 7, '½ teaspoon'),
                    (8, 8, '½ teaspoon'),
                    (8, 36, '1 tablespoon'),
                    (8, 16, '1 large'),
                    (8, 17, '1 clove'),
                    (8, 45, '10 cups'),
                    (8, 46, '4 stalks'),
                    (8, 47, '4 medium'),
                    (8, 38, '2'),
                    (8, 19, '1 teaspoon'),
                    (8, 48, '3 cups'),
                    (8, 27, '1 tablespoon'),
                    (8, 49, '1 tablespoon'),

                    (9, 10, '1¾ cups'),
                    (9, 2, '1½ cups'),
                    (9, 9, '1 teaspoon'),
                    (9, 7, '½ teaspoon'),
                    (9, 5, '2 large'),
                    (9, 50, '2 medium'),
                    (9, 36, '½ cup'),
                    (9, 51, '¼ cup + 1 tablespoon'),
                    (9, 4, '1 teaspoon'),
                    (9, 52, '1 cup'),

                    (10, 53, '1½ teaspoons'),
                    (10, 34, '1¾ cups'),
                    (10, 10, '3½ cups + 1 tablespoon'),
                    (10, 7, '2 teaspoons'),
                    (10, 54, '1 tablespoon'); 
                    """)
create_db()
insert_data()