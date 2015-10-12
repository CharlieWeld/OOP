#This program gets the length and width of a rectangle and
#calculates the area and the perimeter

length = int(input("Enter the lenght of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

area = length * width
perimeter = 2*length + 2*width

print("The area of the rectangle is", area, "and the perimeter is", perimeter)
