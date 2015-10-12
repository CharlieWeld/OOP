#Get the length and width of a rectangle and print the area and perimeter

def calc_area(length, width):
    area = length * width
    return area

def calc_perimeter(length, width):
    perimeter = 2*length + 2*width
    return perimeter

def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = calc_area(length, width)
    perimeter = calc_perimeter(length, width)

    print("The area of the rectange is", area)
    print("The perimeter of the rectange is", perimeter)

main()
