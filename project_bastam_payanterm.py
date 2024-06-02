import random
import mysql.connector as connect

class Food():
    def __init__(self, name:str, raw_material:list):
        self.name = name
        self.raw_material = raw_material
    def __str__(self):
        return f'name of this food: {self.name}\nRaw material: {self.raw_material}'

class Mangement():
    def __init__(self):
        self.foods_list = []
        self.raw_material_dic = dict()
        self.list_situavation = {
            'shanbe':{'nahar':None, 'sham':None},
            'yekshanbe' :{'nahar':None, 'sham':None},
            'doshanbe' :{'nahar':None, 'sham':None},
            'seshanbe' :{'nahar':None, 'sham':None},
            'charshanbe' :{'nahar':None, 'sham':None},
            'panjshanbe' :{'nahar':None, 'sham':None},
            'jome' :{'nahar':None, 'sham':None}
                            }
        
    

        # مثال استفاده:
        table_name = "food_name"

        if not tableExistance(table_name):
            # connecting to my database
            cnx = connect(user='bardia', password='b191282'
                        , host='127.0.0.1', database='food')

            # create a cursor for our database
            cursur = cnx.cursor()

            # create table for sign_in information
            cursur.execute('CREATE TABLE food_name (username VARCHAR(255), mavad_avalie VARCHAR(128))')

            # commit the all change
            cnx.commit()

            # showing message for user
            print('Data base is Create and Done!')

            # close the cursor and database in our program
            cnx.close()
    
    def tableExistance(table_name):
        cursor.execute("SHOW TABLES LIKE %s", (table_name,))
        result = cursor.fetchone()
        return result is not None

    def add_food(self, food):
        self.foods_list.append(food)
        for material in food.raw_material:
            self.raw_material_dic.update({material: 0})
        # connecting to my database
        cnx = connect(user='bardia', password='b191282'
                    , host='127.0.0.1', database='food')

        # create a cursor for our database
        cursur = cnx.cursor()

        # create table for sign_in information
        cursur.execute('CREATE TABLE food_name (foodname VARCHAR(255), mavad_avalie VARCHAR(128))')

        # commit the all change
        cnx.commit()


        # adding information to our DataBase
        cursur.execute(f"INSERT INTO sign_in VALUE (\'{food.name}\', \'{food.raw_material}\')")

        # commit the all change
        cnx.commit()

        # showing message for user
        print('Done!')

        # close the cursor and database in our program
        cnx.close()

    def remove_food(self, food):
        self.foods_list.remove(food)
        # connecting to my database
        cnx = connect(user='bardia', password='b191282'
                    , host='127.0.0.1', database='food')

        # create a cursor for our database
        cursur = cnx.cursor()

        # commit the all change
        cnx.commit()


        # adding information to our DataBase
        cursur.execute(f"DELETE FROM Customers WHERE foodname=\'{food.name}\'")

        # commit the all change
        cnx.commit()

        # showing message for user
        print('Done!')

        # close the cursor and database in our program
        cnx.close()

    def show_foods(self):
        for food in self.foods_list:
            print(food)
            print('-'*10)

    def buy_list(self):
        for key, value in self.raw_material_dic.items():
            if value == 0:
                print(key)

    def barname_ghazaei(self):
        lenth_of_food = len(self.foods_list)
        number_situation_on_week = 7 * 2
        number_of_each_food_in_week = number_situation_on_week / lenth_of_food

        week = [
            'shanbe',
            'yekshanbe',
            'doshanbe',
            'seshanbe',
            'charshanbe',
            'panjshanbe',
            'jome'
            ]
        vaede_ghazaei = ['nahar', 'sham']
        for day in week:
            for vaede in vaede_ghazaei:
                self.list_situavation[day][vaede] = random.choice(self.foods_list)

        for day in week:
            for vaede in vaede_ghazaei:
                print(f'{day}, {vaede}: \n{self.list_situavation[day][vaede]}') 

    def suggest(self):
        pass




man1 = Mangement()
man1.add_food( Food('Bandari', ['Sosis', 'Piaz', 'Sibzamani']))
man1.add_food( Food('Ghorme Sabzi', ['Sabzi', 'Piaz', 'Ghosht']))
# man1.buy_list()
# man1.show_foods()

man1.barname_ghazaei()