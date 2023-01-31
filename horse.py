class Horse:
    def __init__(self,name,color,birth_year):
        self.__name = name
        self.__color = color
        self.__birth_year = birth_year

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,new_name):
        self.__name = new_name

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self,new_color):
        self.__name = new_color

    @property
    def birth_year(self):
        return self.__birth_year

    @birth_year.setter
    def birth_year(self,new_birth_year):
        self.__birth_year = new_birth_year
