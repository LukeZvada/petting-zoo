from datetime import date
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