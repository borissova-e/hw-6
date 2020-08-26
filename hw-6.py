class Animal:
    food_status = False
    sounds = 'Unknown'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def to_feed(self):
        self.food_status = True
        return print(f'{self.name} накормлен(а).')

    def to_recognize_sound(self):
        pass


class Bird(Animal):
    eggs = 0

    def __init__(self, name, weight, subclass='Unknown'):
        super().__init__(name, weight)
        self.subclass = subclass

    def to_collect_eggs(self):
        return print(f'Яйца собраны. {self.eggs} шт.')


class Mammals(Animal):
    milk_status = False
    cut_status = False

    def __init__(self, name, weight, subclass='Unknown'):
        super().__init__(name, weight)
        self.subclass = subclass

    def to_milk(self):
        self.milk_status = True
        return print(f'{self.name} подоина.')

    def to_cut(self):
        self.cut_status = True
        return print(f'{self.name} подстрижен(а).')


uncle_joes_farm = [Bird('Серый', 3.3, 'goose'), Bird('Белый', 2.6, 'goose'), Mammals('Манька', 600, 'cow'),
                   Mammals('Барашек', 80, 'sheep'), Mammals('Кудрявый', 75, 'sheep'), Bird('Ко-Ко', 1.8, 'hen'),
                   Bird('Кукареку', 2.1, 'hen'), Mammals('Рога', 110, 'goat'), Mammals('Копыта', 120, 'goat'),
                   Bird('Кряква', 1.4, 'duck')]

print(f'У дядюшки Джо живут:')
for animal in uncle_joes_farm:
    print(f'{animal.subclass} {animal.name}')

uncle_joes_farm[5].eggs = 10
uncle_joes_farm[6].eggs = 5
uncle_joes_farm[9].eggs = 2
collected_eggs = 0

print('=================')
for animal in uncle_joes_farm:
    animal.to_feed()
    if type(animal) == Bird:
        animal.to_collect_eggs()
        collected_eggs += animal.eggs
    elif animal.subclass == 'sheep':
        animal.to_cut()
    else:
        animal.to_milk()
    print()

print(f'Собрано {collected_eggs} яиц.')

print('=================')
list_weight = []
for animal in uncle_joes_farm:
    list_weight.append(animal.weight)
maximum_weight = max(list_weight)
print(f'Общий вес всех животных {round(sum(list_weight), 1)} кг.')

list_name_weight = []
for animal in uncle_joes_farm:
    list_name_weight.append({'name': animal.name, 'weight': animal.weight})
for animal in list_name_weight:
    if animal['weight'] == maximum_weight:
        print(f"Имя животного с макимальным весом {maximum_weight} кг - {animal['name']}.")
        break
