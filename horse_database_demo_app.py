import sqlite3
from race_horse import RaceHorse

def create_database():
    con = sqlite3.connect('horses.db')
    cur = con.cursor()
    print("Database created!")
    return [con,cur]
    
def create_table(con_obj,cur_obj):
    cur_obj.execute("CREATE TABLE if not exists horses (horse_name varchar(25), horse_color varchar(15), horse_b_year varchar(4), horse_races varchar(4))")
    con_obj.commit()
    print('\nTable Created')

def add_horses(con_obj,cur_obj,horses_list):
    for obj in horses_list:
        horse_list = obj.split(' ')
        horse_name = horse_list[0].replace('"','')
        horse_color = horse_list[1].replace('"','')
        horse_b_year = horse_list[2].replace('"','')
        horse_races = horse_list[3].replace('"','')
        cur_obj.execute("INSERT INTO horses VALUES ('"+ horse_name + "','" + horse_color + "','" + horse_b_year + "','" + horse_races + "')")
        
        
    con_obj.commit()     
        

def display_data(cur_obj):
    for row in cur_obj.execute("SELECT horse_name, horse_color, horse_b_year, horse_races  FROM horses"):
        print(row)
    
    

def search_horse(cur_obj,name):
    query_result = cur_obj.execute("SELECT * FROM horses where horse_name = '" + horse_name + "'")
    for row in query_result:
        print('Display horse found:')
        print(row)
    

#Main
cd = create_database()

create_table(cd[0],cd[1])

horses_list = []
print('\nCreate a list of Race Horses: \n')
while len(horses_list) < 5:
    horse_name = input('Enter horse name: ')
    horse_color = input('Enter horse color: ')
    horse_b_year = input('Enter horse birth year: ')
    horse_races = input('Enter horse races: ')
    horse_total = horse_name + ' ' + horse_color + ' ' + horse_b_year + ' ' + horse_races
    print('Adding the Race Horse to the database')
    print('Adding',horse_total,'to the database')
    horses_list.append(horse_total)

add_horses(cd[0],cd[1],horses_list)

print('\nDisplay all race horses in the database')
display_data(cd[1])

horse_search = input('\nSearch for a horse: ')

search_horse(cd[1],horse_search)
