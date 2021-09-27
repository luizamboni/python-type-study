from typing import NamedTuple


Point = NamedTuple(
    'Point',
    [
        ('x',int), 
        ('y',int),
    ]
)


p = Point(x=1, y=2)

print(p.x, p.y)