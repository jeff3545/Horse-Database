import horse

class RaceHorse(horse.Horse):

    def __init__(self,name,color,birth_year,num_races):
        horse.Horse.__init__(self,name,color,birth_year)
        self.__num_races = num_races

    @property
    def num_races(self):
        return self.__num_races

    @num_races.setter
    def num_races(self,new_num_races):
        self.__num_races = new_num_races

