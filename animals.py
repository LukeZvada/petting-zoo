from datetime import date
from habitats.wetlands import Wetlands
from habitats import wetlands
from habitats.snakepit import SnakePit
from habitats.pettingzoo import PettingZoo
from slithering.models import Salamander, Slug, Snail, Snake, Worm
from swimming.models import Bass, Orca, Salmon, Seal, Tuna
from walking.models import Bear, Bigfoot, Cougar, Deer, Lion



Cougs = Cougar("Cougs", "Mountain Lion", "Morning", "Rabbits")
Bambi = Deer("Bambi", "Whitetail", "Evening", "Grass")
Bee = Bear("Bee", "Black Bear", "Night", "Salmon")
Bigboy = Bigfoot("Bigboy", "Sasquatch", "Midday", "Sticks")
Simba = Lion("Simba", "Cat", "Morning", "Zebra")

Jim = Bass("Jim", "Bigmouth Bass", "Morning", "Bugs")
Luna = Tuna("Luna", "Bigeye", "Evening", "Mino")
Sally = Salmon("Sally", "Pink", "Night", "Seaweed")
Willy = Orca("Willy", "Type A", "Midday", "Seals")
Neal = Seal("Neal", "Crabeater", "Morning", "Salmon")

Mal = Salamander("Mal", "Tiger", "Morning", "Flies")
Doug = Slug("Doug", "Leopard Slug", "Evening", "Dirt")
Blake = Snake("Blake", "Python", "Night", "Mice")
Ted = Worm("Ted", "Earthworm", "Midday", "Dirt")
Gary = Snail("Gary", "Garden Snail", "Morning", "Dirt")

print(f'{Cougs.name} the {Cougs.species} is available to pet during the {Cougs.shift} shift.') 
Cougs.feed()
print(Cougs)
Bigboy.feed()
Mal.feed()

varmint_village = PettingZoo("Varmint Village")

varmint_village.animals.append(Cougs)
varmint_village.animals.append(Bambi)
varmint_village.animals.append(Bee)
varmint_village.animals.append(Bigboy)
varmint_village.animals.append(Simba)

print(varmint_village.animals)

for animal in varmint_village.animals:
    print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')

snake_pit = SnakePit("Snake Pit")

snake_pit.animals.append(Mal)
snake_pit.animals.append(Doug)
snake_pit.animals.append(Blake)
snake_pit.animals.append(Ted)
snake_pit.animals.append(Gary)

print(snake_pit.animals)

for animal in snake_pit.animals:
    print(f'You can find {animal.name} the {animal.species} in the {snake_pit.attraction_name}')

wetlands = Wetlands("Wetlands")

wetlands.animals.append(Jim)
wetlands.animals.append(Luna)
wetlands.animals.append(Sally)
wetlands.animals.append(Willy)
wetlands.animals.append(Neal)

print(snake_pit.animals)

for animal in wetlands.animals:
    print(f'You can find {animal.name} the {animal.species} in the {wetlands.attraction_name}')