#This program seeks to find when the volume and surface area of a cube are equal
#for a given value of width

class Harmonic(object):
    def __init__(self, max_width):
        self.max_width = max_width
        
    def calculate_volume(self, width):
        volume = width**3
        return volume

    def calculate_surface_area(self, width):
        surface_area = 6*(width**2)
        return surface_area

    def harmonic(self):
        
        
        for width in range(1, self.max_width+1):
            volume = self.calculate_volume(width)
            surface_area = self.calculate_surface_area(width)

            if volume == surface_area:
                print("Volume and surface area are equal at width = ", width)
                break #since we have found when the volume and surface area are equal
                      #we can leave the loop


def main():
    width = int(input("Enter the max width to test the volume against width: "))
    harmo = Harmonic(width)
    harmo.harmonic()

    
if __name__ == '__main__':
    main()
