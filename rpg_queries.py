'''
imports sqlite3 and programmatically executes and reports results for the above queries

1. How many total Characters are there?
2. How many of each specific subclass?
3. How many total Items?
4. How many of the Items are weapons? How many are not?
5. How many Items does each character have? (Return first 20 rows)
6. How many Weapons does each character have? (Return first 20 rows)
7. On average, how many Items does each Character have?
8. On average, how many Weapons does each character have?

the charactercreator_* and armory_* tables and where you should focus your attention.

armory_item and charactercreator_character are the main tables for Items and Characters respectively -

It's also OK to figure out the results partially with a query and partially with a bit of logic or math afterwards, 
though doing things purely with SQL is a good goal. Subqueries and aggregation functions may be helpful for putting 
together more complicated queries.
'''

import os
import sqlite3

#construct a path to wherever your database exiSts; string path =? ABSOLUTE  FILE PATH CONSTRUCTION?
#DB_FILEPATH  = "chinook.db" a (hard-coded?) STRING for a path; (file..) works diff'ntly from how wld in app directory ... OTHER NON-reliable ways: 1) hardcoded with slashes 2) a STRING won't work depending on where yr trying to run it

#RELATIVE FILE PATH CONSTRUCTION
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3") # dirname(__file__) = metadata about the file

#RELIABLE CONNECTION PATH (to join filepaths.. https://www.youtube.com/watch?v=u8KHXaRUxjg&feature=youtu.be 1:51:11 in Mod1 vid)
connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:",connection)

cursor = connection.cursor()
print("CURSOR", cursor )   

#1. How many total Characters are there?
query1 = "SELECT count(distinct character_id) FROM charactercreator_character;"
#query1 = "SELECT count(character_id) FROM charactercreator_character_inventory;"
#

#result = cursor.execture(query)
#print("RESULT", RESULT) # returns cursor object w/o results (need to fetch the results)

#breakpoint()

result1 = cursor.execute(query1).fetchall()
print("RESULT 1. Total Characters: ", result1)

'''
2. How many of each specific (character) subclass? (mage-->necromancer, thief, cleric, fighter, )
    a) want a row per each subclass (ea subcls on its own row)
    b) want Result set to have 2 columns: 
       (i) 1 with subclass name; GROUP BY subclass name
       (ii) 1 with counts
    AGGREGATE/"drop" OTHER COLS WE'RE NOT GROUPING BY- we're Grouping by subclass?


query2 = "
SELECT 
	character_ptr_id,
	count(distinct character_ptr_id) 
	
FROM charactercreator_cleric,
     charactercreator_mage, 
     charactercreator_thief, 
     charactercreator_fighter,
     charactercreator_necromancer


GROUP BY character_ptr_id"  # in TablePlus gett err: Query 1 ERROR: ambiguous column name: character_ptr_id;
    # “Ambiguous column name” means that you are referencing an attribute or attributes that belong to more than one of the tables you are using in the query, and have not qualified the attribute reference. The SQL engine doesn't know which one you want.

    # What does the SQL 'ambiguous column name' error mean ...

#OR?: 
#-----------------------
SELECT 

FROM charactercreator_cleric.character_ptr_id  # then do for all other subclasses 

#------------------ 

# MORE CONCISE/FANCY with MUTLIPLE TABLES JOINS, iterating through the queries:

queries = [
    #"SELECT COUNT(customerId) FROM customers;"
    "SELECT * FROM all_character_subcls"  # TO DO: make a TABLE &? a list of subclasses; or list ALL TABLES proLLY eaySia
                                          #   OR!: JOIN TABLES or/and COLS
]

for query in queries:
    print("--------------------")
    print(f"QUERY: '{query}'")

    #obj = curs.execture(query)
    #print("OBJ", type(obj))
    #print(obj) #> <class 'sqlite3.Cursor'>

    results = curs.execute(query).fetchall()
    print("RESULTS:", type(results))
    print(results)

    print(type(results[0])) #> type(results[0])
    #breakpoint()
     
    '''
#2. How many of each specific (character) subclass?
query2a = "SELECT count(distinct character_ptr_id) as total_clerics FROM charactercreator_cleric;"
result2a = cursor.execute(query2a).fetchall()
print("RESULT 2a. Total clerics: ", result2a)
print("--------------------")

query2b = "SELECT count(distinct character_ptr_id) as total_mages FROM charactercreator_mage;"
result2b = cursor.execute(query2b).fetchall()
print("RESULT 2b. Total mages: ", result2b)
print("--------------------")

query2c = "SELECT count(distinct character_ptr_id) as total_thieves FROM charactercreator_thief;"
result2c = cursor.execute(query2c).fetchall()
print("RESULT 2c. Total thieves: ", result2c)
print("--------------------")

'''
query2e = "SELECT count(distinct character_ptr_id) as total_necromancers FROM charactercreator_necromancer;"
result2e = cursor.execute(query2d).fetchall()
print("RESULT 2e. Total necromancers: ", result2e)
print("--------------------")
'''

query2d = "SELECT count(distinct character_ptr_id) as total_fighters FROM charactercreator_fighter;"
result2d = cursor.execute(query2d).fetchall()
print("RESULT 2d. Total fighters: ", result2d)
print("--------------------")