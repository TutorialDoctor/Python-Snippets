
import math
def areaCircle(radius):
    if type(radius) not in [int,float]:
        raise TypeError("Type radius must be a non-negative real number.")
    if radius <0:
        raise ValueError("The readius cannot be neggative.")
    area = math.pi * radius**2
    return area