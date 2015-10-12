#spherevolume.py
from math import pi
#import the power function from math library
from math import pow

radius = float(input("Enter the radius of a sphere: "))

volume = (4/3) * pi * (pow(radius, 2))
print("The volume of a sphere with radius", radius, "is", format(volume, '.2f'))
