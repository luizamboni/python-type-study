from typing import NewType

CicleRadius = NewType('CicleRadius', float)

circle_rad = CicleRadius(10.5)

print(circle_rad)

def draw_circle(radius: CicleRadius):
    print(f"drawing... {radius}")


# draw_circle(3.3) problem

draw_circle(circle_rad)
