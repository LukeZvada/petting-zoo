from datetime import date
from slithering.models import Salamander, Slug, Snail, Snake, Worm
from swimming.models import Bass, Orca, Salmon, Seal, Tuna
from walking.models import Bear, Bigfoot, Cougar, Deer, Lion



Cougs = Cougar("Cougs", "Mountain Lion")
Bambi = Deer("Bambi", "Whitetail")
Bee = Bear("Bee", "Black Bear")
Bigboy = Bigfoot("Bigboy", "Sasquatch")
Simba = Lion("Simba", "Cat")

Jim = Bass("Jim", "Bigmouth Bass")
Luna = Tuna("Luna", "Bigeye")
Sally = Salmon("Sally", "Pink")
Willy = Orca("Willy", "Type A")
Neal = Seal("Neal", "Crabeater")

Mal = Salamander("Mal", "Tiger")
Doug = Slug("Doug", "Leopard Slug")
Blake = Snake("Blake", "Python")
Ted = Worm("Ted", "Earthworm")
Gary = Snail("Gary", "Garden Snail")

print(Doug)