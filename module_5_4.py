class House:
    houses_history = []
    def __new__(cls, *args,**kwargs):
        cls.name = args[0]
        cls.number_of_floors = args[1]
        cls.houses_history.append(cls.name)
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        return House(self.name, self.number_of_floors + value)

    def __radd__(self, value):
        return House(self.name, self.number_of_floors + value)

    def __iadd__(self, value):
        return House(self.name, self.number_of_floors + value)

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __del__(self):
        print(f' {self.name} снесён, но он останется в истории')
        #House.houses_history.remove(self.name)

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует"')
        else:
            for i in range(1, new_floor+1):
                print(i)

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)


#
# Удаление объектов
del h2
del h3

print(House.houses_history)