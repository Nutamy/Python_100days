import pandas as pd
from random import choice
with open("animals.txt", "r") as data_animals:
    animals = data_animals.read().splitlines()
print(animals)

colors = pd.read_csv("colors.csv")["air_force_blue_raf"].tolist()
short_colors = []
short_animals = []
for color in colors:
    if len(color) < 7:
        short_colors.append(color)
for animal in animals:
    if len(animal) < 7:
        short_animals.append(animal)

class NameGenerator:
    def __init__(self):
        self.color = choice(short_colors)
        self.animal = choice(short_animals)
        self.name = f"{self.color}_{self.animal}"
