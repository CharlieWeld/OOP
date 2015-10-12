# OOP - Lab 5 - Q's 4 & 5 - Temperature Convert
# This program will solve the problem two ways simutaneously using Threads
# 1. In the console style
# 2. Using a GUI

# Import threading and tkinter modules
from threading import *
from tkinter import *

##################################    GUI   #####################################################
#Create a class for the GUI called TempConvert

class TempConvert(object):
    def __init__(self, root): #The constructor takes the main window object
        #Set instance variables and create GUI
        self.root = root 
        self.create_GUI()
                        
    def create_GUI(self): #This method will draw the widgets
        # Create label widget for user prompt
        Label(self.root, text="Enter the temperature in celsius").pack()
        self.celsius = DoubleVar() # Assign a tkinter variable to store the value in the entry box
        Entry(self.root, textvariable=self.celsius).pack() #Create entry box for user input
        Button(self.root, text="Convert", command=self.convert_temp).pack() #Create button for user
        self.text = StringVar() #Assign string variable to hold the conversion result
        Label(self.root, textvariable=self.text).pack() #Create Label widget to display result

        #Call method to draw the conversion table 
        self.draw_table()

    def convert_temp(self): #Convert celsius to fahrenheit and display on GUI

        # Create two lists to hold temperature ranges and temperature phrases
        temp_ranges = [-30, -20,-19, -10, -9, 2, 3, 10, 11, 20,]
        temp_phrases = ["Artic", "Baltic", "Freezing", "Chilly", "Not Bad", "Great"]

        # create local variable and assign it the value of the instance variable "self.celsius"
        celsius = self.celsius.get()

        fahrenheit = (32+celsius*9/5)
        
        #This part creates a string with the converted temp and then adds a phrase
        #based on the celsius temperature
        
        str1 = "Temperature in Fahrenheit: " + "{:0.2f}".format(fahrenheit) + '\u00b0' + " - "

        #NB I using the two list above can be used to more easily insert the right phrase
        if (celsius >= temp_ranges[0]) & (celsius <= temp_ranges[1]):
            str1 += temp_phrases[0]
        elif (celsius >= temp_ranges[2]) & (celsius <= temp_ranges[3]):
            str1 += temp_phrases[1]
        elif (celsius >= temp_ranges[4]) & (celsius <= temp_ranges[5]):
            str1 += temp_phrases[2]
        elif (celsius >= temp_ranges[6]) & (celsius <= temp_ranges[7]):
            str1 += temp_phrases[3]
        elif (celsius >= temp_ranges[8]) & (celsius <= temp_ranges[9]):
            str1 += temp_phrases[4]
        elif (celsius > temp_ranges[9]):
             str1 += temp_phrases[5]

        self.text.set(str1) #Change the label text using the "self.text" tkinter variable

    #This Method will create a Text widget and display the conversion table
    #Between -30 degrees and 60 degrees
    def draw_table(self):
        self.mtext = Text(self.root, width=50, height=20)
        self.mtext.pack()
        self.mtext.insert(END, "Celsius  Fahrenheit  Kelvins  Rankine\n")
        for c in range(-30, 60, 10):
            str1 = "{:>7}".format(c)
            str1 += ("{:>12}".format("{:.2f}".format(32+c*9/5)))
            str1 += ("{:>9}".format("{:.2f}".format(c + 273.15)))
            str1 += ("{:>9}".format("{:.2f}".format(c*9/5 + 273.15*9/5)))
            str1 += '\n'
            self.mtext.insert(END, str1)

################################# Calculate Fahrenheit  ####################################################
            
#This Method is used to display the conversion table on the "console" and
#Prompt the user to enter a celsius value and it will display a fahrenheit value
#This will be run in a different thread to main
def temperature(list1 = []):
    print("Celsius  Fahrenheit  Kelvin  Rankine")
    for i in range(-30, 61, 10):
        print("{:>7}".format(i), "{:>11}".format("{:.2f}".format((32+i*9/5))), 
              "{:>7}".format("{:.2f}".format(i+273.15)),  "{:>8}".format("{:.2f}".format((273.15*(9/5)+i*9/5))))
    
    temp_phrases = ["Artic", "Baltic", "Freezing", "Chilly", "Not Bad", "Great"]
    temp_ranges = [-30, -20,-19, -10, -9, 2, 3, 10, 11, 20,]
    celsius = 0
    
    while celsius != 'q':
        celsius = (input("Enter a temperature in celsius or 'q' to quit: "))
        if celsius == 'q':
            pass #If user enter q then skip until the next loop iteration where the while loop will terminate
        else:
            celsius = float(celsius)
            fahrenheit = (32+celsius*9/5)
    
            if (celsius >= temp_ranges[0]) & (celsius <= temp_ranges[1]):
                print(fahrenheit, temp_phrases[0])
            elif (celsius >= temp_ranges[2]) & (celsius <= temp_ranges[3]):
                print(fahrenheit, temp_phrases[1])
            elif (celsius >= temp_ranges[4]) & (celsius <= temp_ranges[5]):
                print(fahrenheit, temp_phrases[2])
            elif (celsius >= temp_ranges[6]) & (celsius <= temp_ranges[7]):
                 print(fahrenheit, temp_phrases[3])
            elif (celsius >= temp_ranges[8]) & (celsius <= temp_ranges[9]):
                  print(fahrenheit, temp_phrases[4])
            elif (celsius > temp_ranges[9]):
                  print(fahrenheit, temp_phrases[5])
          
    print("Finished Thread 2\n")
        
    
#############################################    MAIN    ################################################
def main():

    mythread = Thread(target=temperature) #Create a new thread and give it the method temperature
    mythread.start() #Start the thread
    
    root=Tk() #Create root window
    root.geometry("400x400+100+100")
    root.title("Temperature Converter")
    tempconvert = TempConvert(root) #create object "tempconvert" from class TempConvert and pass the root window
    root.mainloop() #This keeps the GUI waiting for inputs and button presses


if __name__=='__main__':
    main()





    
