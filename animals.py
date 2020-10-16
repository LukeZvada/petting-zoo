from datetime import date
from slithering.models import Salamander, Slug, Snail, Snake, Worm
from swimming.models import Bass, Orca, Salmon, Seal, Tuna
from walking.models import Bear, Bigfoot, Cougar, Deer, Lion



Cougs = Cougar("Cougs", "Mountain Lion", "Morning")
Bambi = Deer("Bambi", "Whitetail", "Evening")
Bee = Bear("Bee", "Black Bear", "Night")
Bigboy = Bigfoot("Bigboy", "Sasquatch", "Midday")
Simba = Lion("Simba", "Cat", "Morning")

Jim = Bass("Jim", "Bigmouth Bass", "Morning")
Luna = Tuna("Luna", "Bigeye", "Evening")
Sally = Salmon("Sally", "Pink", "Night")
Willy = Orca("Willy", "Type A", "Midday")
Neal = Seal("Neal", "Crabeater", "Morning")

Mal = Salamander("Mal", "Tiger", "Morning")
Doug = Slug("Doug", "Leopard Slug", "Evening")
Blake = Snake("Blake", "Python", "Night")
Ted = Worm("Ted", "Earthworm", "Midday")
Gary = Snail("Gary", "Garden Snail", "Morning")

print(f'{Cougs.name} the {Cougs.species} is available to pet during the {Cougs.shift} shift.')