class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)


    def get_info(self, species):
        if species == 'mammal':
            return f'Mammals in {self.name}: {", ".join(self.mammals)}'
        elif species == 'fish':
            return f'Fishes in {self.name}: {", ".join(self.fishes)}'
        elif species == 'bird':
            return f'Birds in {self.name}: {", ".join(self.birds)}'
        return None


zoo_name = input()
number_of_animals = int(input())

zoo_name = Zoo(zoo_name)
__animals = number_of_animals

for animal in range(number_of_animals):
    species, name = input().split()

    zoo_name.add_animal(species, name)


info = input()

print(zoo_name.get_info(info))
print(f'Total animals: {number_of_animals}')