############## Part 2 #####################


def natural_2(x):
    if x == 1:
        return str(x)
    else:
        return str(natural_2(x - 1)) + " " + str(x)


def natural(x):
    if x == 1:
        return str(x)
    else:
        return str(x) + " " + str(natural(x - 1)) + " " + str(x)


def sum_of_list(my_list):
    if len(my_list) == 1:
        return int(my_list[0])
    else:
        return int(my_list[0]) + int(sum_of_list(my_list[1::]))


############## Part 3 #####################

class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0

    def append(self, value):
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = value
        self.size += 1

    def remove_first(self):
        temp = [None] * self.capacity
        for ix in range(1, self.size):
            temp[ix - 1] = self.arr[ix]
        self.arr = temp
        self.size -= 1

    def get_size(self):
        return self.size

    def print(self):
        for ix in range(self.size):
            print("{}".format(self.arr[ix]), end=" ")
        print()

    def resize(self):
        self.capacity *= 2
        temp = [None] * self.capacity
        for ix in range(self.size):
            temp[ix] = self.arr[ix]
        self.arr = temp


############## Part 4 #####################


class Animal:
    def __init__(self, animal_id="", species="", weight=0):
        self.id = animal_id
        self.species = species
        self.weight = weight

    def get_id(self):
        return self.id

    def get_species(self):
        return self.species

    def get_weight(self):
        return self.weight

    def set_id(self, new_id):
        self.id = new_id

    def set_species(self, new_species):
        self.species = new_species

    def set_weight(self, new_weight):
        self.weight = new_weight

    def __repr__(self):
        return "{}: {}, {} kilograms".format(self.id, self.species, self.weight)

    # Breytti í __repr__ virkaði betur að prenta í Zoo þannig


class Zoo:
    def __init__(self):
        self.zoo_dict = {}

    def add_animal(self, animal_id="", species="", weight=0):
        new_animal = Animal(animal_id, species, weight)
        self.zoo_dict[animal_id] = new_animal

    def get_animal(self, animal_id):
        if animal_id in self.zoo_dict.keys():
            return self.zoo_dict[animal_id]

    def change_species(self, animal_id, new_species):
        new_animal = Animal(animal_id, new_species, self.zoo_dict[animal_id].get_weight())
        self.zoo_dict[animal_id] = new_animal

    def change_weight(self, animal_id, new_weight):
        new_animal = Animal(animal_id, self.zoo_dict[animal_id].get_species, new_weight)
        self.zoo_dict[animal_id] = new_animal

    def __str__(self):
        my_str = ""
        for animal_id, info in self.zoo_dict.items():
            my_str += "{}: {}, {}\n".format(info.get_id(), info.get_species(), info.get_weight())
        return my_str