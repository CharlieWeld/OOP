from coordinate import Coordinate
def shell_function(airport_names, airport_coordinates, airport_codes):

        #The following while loop will let the user select to print out the list of airports
        #Calculate the distance between two coordinates
        #Calculate the distance between two airports based on their codes

        #Coordinates from here on will be objects (Coordinate type) instead of lists
        #For each set of coordinates there will be an object
        #These objects will use their own instance methods to calculate the distance
        #between themselves and another cooordinate object

        user = 'n'
        while user != 'q': 
            print("Select one of these options", "p - print airport distance table",\
                  "c - distance between two coordinates",\
                  "l - to enter two airport codes and calculate them using lists",\
                  "a - to enter two airport codes to find the distance", \
                  "q - quit",sep='\n')
            user = input("Enter option: ")
            print()
            if user == 'p': #user selects print list
                coord=Coordinate() #Create coordinate object
                coord.print_airport_distances(airport_names, airport_coordinates) #this method will print the distances
                
            elif user == 'c': #user selects coordinates
                coord1 = Coordinate([29,20]) #Give default values
                print("The first set of coordinates")
                coord1.setCoordinates()
                coord2 = Coordinate([30,39]) #Give default values or else it will create reference to coord1
                print("The second set of coordinates")
                coord2.setCoordinates()
                distance=coord1.get_distance_between_coordinates(coord2)
                print("The distance between the coordinates in km is", distance, end='\n')

            elif user == 'l': #user selects airport distances using lists

               error = True
               while error:
                   try:
                       code_one = input("Enter the first airport code: ")
                       code_two = input("Enter the second airport code: ")
                       code_one_index = airport_names.index(code_one)
                       code_two_index = airport_names.index(code_two)
                       coords_one = Coordinate(airport_coordinates[code_one_index])
                       coords_two = Coordinate(airport_coordinates[code_two_index])
                       error = False
                   except ValueError:
                        print()
                        print("Error enter valid airport codes")
                        print()
                        error = True

               distance = coords_one.get_distance_between_coordinates(coords_two)
               print("The distance between the two airports using list is: ", distance)

            elif user == 'a': #user selects airport distances
                error = True
                while error: #while there is an error with the input keep asking for valid airport codes
                    try: #Try this code
                        code_one = input("Enter the code of the first airport: ")
                        code_two = input("Enter the code of the second airport: ")
                        print()
                        coord1=Coordinate(airport_codes[code_one])
                        coord2=Coordinate(airport_codes[code_two])
                        distance = coord1.get_distance_between_coordinates(coord2)
                        error = False
                    except KeyError: #If there is a keyerror (dictionary does not conatin this key) print error message and ask for valid input
                        print()
                        print("You entered a code incorrectly! Prepare for a nuclear strike!!!")
                        print()
                        error = True
                print("The distance between the two airports in km is", distance, end='\n\n')
                

            elif user == 'q':
                print("Goodbye")
            else:
                print("Enter valid character")
        print("end")

