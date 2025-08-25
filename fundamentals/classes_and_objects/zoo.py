class Zoo:
    __animals = 0

    def __init__(self, zoo_name:str):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "birds":
            self.fishes.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = " "
        if species == "mammal":
            result += f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\n"
        elif species == "birds":
            result += f"Birds in {self.zoo_name}: {', '.join(self.fishes)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result

zoo_name_ = input()
zoo = Zoo(zoo_name_)
count = int(input())

for _ in range(count):
    animal_ = input().split()
    species_ = animal_[0]
    name_ = animal_[1]
    zoo.add_animal(species_, name_)

info = input()
print(zoo.get_info(info))