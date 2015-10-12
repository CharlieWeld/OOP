#cube.py

#Calculate the volume and surface area
#volume = width cubed
#surface area = 6 x a^2

def calc_volume(width):
    volume = width ** 3
    return volume

def calc_surface_area(width):
    surface_area = 6 * (width ** 2)
    return surface_area

def main():
    width = float(input("Enter width of cube: "))
    volume = calc_volume(width)
    surface_area = calc_surface_area(width)
    print("Volume of cube: ", "%.2f" % volume)
    print("Surface area of cube: ", "%.2f" % surface_area)

main()
