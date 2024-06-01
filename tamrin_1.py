import random

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

    def add_food(self, food):
        self.foods_list.append(food)
        for material in food.raw_material:
            self.raw_material_dic.update({material: 0})

    def remove_food(self, food):
        self.foods_list.remove(food)
    
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




    
man1 = Mangement()
man1.add_food( Food('Bandari', ['Sosis', 'Piaz', 'Sibzamani']))
man1.add_food( Food('Ghorme Sabzi', ['Sabzi', 'Piaz', 'Ghosht']))
# man1.buy_list()
# man1.show_foods()

man1.barname_ghazaei()
