from tkinter import *
from coordinate import Coordinate

class create_gui(Frame):
    def __init__(self, master, airport_names, airport_coordinates, airport_codes):
        self.master = master
        Frame.__init__(self, master)
        self.pack()
        self.select_gui()
        self.airport_names = airport_names
        self.airport_coordinates = airport_coordinates
        self.airport_codes = airport_codes
        
    def select_gui(self):
        Label(self, text="Please Select an option").pack()
        self.user = StringVar()
        Button(self,width=15,text="Print distances",command=self.print_list_gui).pack()
        Button(self,width=15,text="Airport Codes",command=self.airport_gui).pack()
        Button(self,width=15,text="Coordinates",command=self.coord_gui).pack()
        self.mtext = Text(self,width=50,height=10)

    def print_list_gui(self):
        self.clear_gui()

        name_string = "       "
        for name in self.airport_names:
            name_string += name
            name_string += "    "
        self.mtext.pack()
        self.mtext.insert(END,name_string+'\n')
        for index,value in enumerate(self.airport_names):
           coord1 = Coordinate(self.airport_coordinates[index])
           self.mtext.insert(END,value)

           for index1, value1 in enumerate(self.airport_names):
               coord2 = Coordinate(self.airport_coordinates[index1])
               distance = coord1.get_distance_between_coordinates(coord2)
               int_distance = int(distance)
               self.mtext.insert(END,"{:>7}".format(int_distance))
           self.mtext.insert(END,'\n')
        self.mtext.insert(END,'\n')
        
    def airport_gui(self):
     self.clear_gui()
     Label(self, text="Enter two airport codes").pack()
     self.code_one = StringVar()
     self.code_two = StringVar()
     Entry(self, textvariable=self.code_one).pack()
     Entry(self, textvariable=self.code_two).pack()
     Button(self, text="Calculate",command=self.button_airport).pack()

    def button_airport(self):
     self.lat1a = self.airport_codes[self.code_one.get()][0]
     self.long1a = self.airport_codes[self.code_one.get()][1]
     self.lat2a = self.airport_codes[self.code_two.get()][0]
     self.long2a = self.airport_codes[self.code_two.get()][1]
     self.calculate_airport_gui()
     
    def calculate_airport_gui(self):
        c1 = [self.lat1a, self.long1a]
        c2 = [self.lat2a, self.long2a]
        coord1 = Coordinate(c1)
        coord2 = Coordinate(c2)
        distance=coord1.get_distance_between_coordinates(coord2)
        self.mtext.pack()
        str1 = "Distance between airports in km is " + str(distance)+'\n'
        self.mtext.insert(END,str1) 
                
    def coord_gui(self):
        self.clear_gui()
        self.lat1=DoubleVar()
        self.long1=DoubleVar()
        self.lat2=DoubleVar()
        self.long2=DoubleVar()
        Entry(self,textvariable=self.lat1).pack()
        Entry(self,textvariable=self.long1).pack()
        Entry(self,textvariable=self.lat2).pack()
        Entry(self,textvariable=self.long2).pack()
        Button(self, text="Calculate", command=self.calculate_coord_gui).pack()
        
    def calculate_coord_gui(self):
        c1 = [self.lat1.get(), self.long1.get()]
        c2 = [self.lat2.get(), self.long2.get()]
        coord1 = Coordinate(c1)
        coord2 = Coordinate(c2)
        distance=coord1.get_distance_between_coordinates(coord2)
        self.mtext.pack()
        str1 = "The distance between coordinates in km is " + str(distance)+'\n'
        self.mtext.insert(END,str1)
        
    def clear_gui(self):
        self.destroy()
        Frame.__init__(self, self.master)
        self.pack()
        self.select_gui()
