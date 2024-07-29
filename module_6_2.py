class Vehicle:    #любой транспорт

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner                       #владелец транспорта
        self.__model = __model                   #модель (марка) транспорта
        self.__engine_power = __engine_power     #мощность двигателя
        self.__color = __color                   #название цвета

    def get_model(self, __model):
        return self.__model

    def get_horsepower(self, __engine_power):
        return self.__engine_power

    def get_color(self, __color):
        return self.__color

    def print_info(self):
        print(f'Модель: {self.__model}\nМощность двигателя: {self.__engine_power}\nЦвет: {self.__color}\nВладелец: {self.owner}')

    def set_color(self, new_color):
        for i in range(len(Vehicle.__COLOR_VARIANTS)):
            if new_color.lower() in Vehicle.__COLOR_VARIANTS[i].lower():
                self.__color = new_color
                return
        print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):      #наследник класса Vehicle

    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()