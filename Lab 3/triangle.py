# This program calculates the hypotenuse of a right angle triangle
# The user enters the adjacent and then the opposite lengths
# The length of the hypotenuse is printed

def calc_hypotenuse(adjacent, opposite):
    hypotenuse = ((adjacent ** 2) + (opposite ** 2)) ** 0.5 # 0.5 calculates the square root
    return hypotenuse

def main():
    adjacent = float(input("Enter the lenght of the adjacent side: "))
    opposite = float(input("Enter the length of the opposite side: "))

    hypotenuse = calc_hypotenuse(adjacent, opposite)
    print("The length of the hypotenuse is", "%.2f" % hypotenuse)

main()

#Q7. Nothing both sides are squared!!!!!
