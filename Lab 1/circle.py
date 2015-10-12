#First lab
#circle.py
#Calculate the area of a circle

#import pi from the math library
from math import pi

radius = 12

#area of a circle is (pi x radius^2)
#The double asterisk (**) is "the power of" operator
area = pi * (radius ** 2)

#the circumference of a circle is: 2 x pi x radius
circumference = 2 * pi * radius

print("The area of a cirle with radius", radius, "is", "%.2f" % area)
print("The circumference of a circle with radius", radius, "is", format(circumference, '.2f'))
#The "%.2f" is used to truncate the number of decimal points show
