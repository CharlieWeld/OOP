from math import pi, acos, sin, cos

class Coordinate():
    earth_radius = 6371 #Define class variables

    def __init__(self, coordinates=[0,0]):
        self.coordinates = coordinates


    def setCoordinates(self):
        self.coordinates[0] = float(input("Enter the latitude: "))
        self.coordinates[1] = float(input("Enter the longitude: "))
        print()
             
    def calculate_distance(self, phi, theta):
        distance = acos((sin(phi[0])*sin(phi[1]))*(cos(theta[0]-theta[1]))\
                        +(cos(phi[0])*cos(phi[1]))) * Coordinate.earth_radius
     
        return distance

    def get_distance_between_coordinates(self, other):
        
        if self.coordinates[0] > 0:
            latitude1_angle = 90 - self.coordinates[0]
        else:
            latitude1_angle  = 90 - self.coordinates[0]

        if other.coordinates[0] > 0:
            latitude2_angle = 90 - other.coordinates[0]
        else:
            latitude2_angle = 90 - other.coordinates[0]

    
        phi=[0,0]
        theta=[0,0]
        
        phi[0] =  latitude1_angle * ((2*pi)/360)
        phi[1] =  latitude2_angle * ((2*pi)/360)
        theta[0] = self.coordinates[1]* ((2*pi)/360)
        theta[1] = other.coordinates[1]* ((2*pi)/360)
        
        distance = int(self.calculate_distance(phi, theta))
        
        return distance

    def print_airport_distances(self, airport_names, airport_coordinates):
        i=0
        
        name_string = "       "
        for name in airport_names:
            name_string += name
            name_string += "    "
        print(name_string)
        for index,value in enumerate(airport_names):
           coord1 = Coordinate(airport_coordinates[index])
           print(value, end='')
           i+=1
           for index1, value1 in enumerate(airport_names):
               coord2 = Coordinate(airport_coordinates[index1])
               distance = coord1.get_distance_between_coordinates(coord2)
               int_distance = int(distance)
               print("{:>7}".format(int_distance), end='')
            
           print(end='\n')
        print() #Newline after table
