#Lab 3 - Q1 tempconvert
#Convert Celsius to Fahrenheit

def TempConvert(celsius):
    fahrenheit = 32 + (celsius * (9/5))
    return fahrenheit

def main():

    #Could put a loop here, but we will let the user start the program each time
    celsius = float(input("Enter the temperature in celsius: "))
    fahrenheit = TempConvert(celsius)

    #Need to create a string because print buts a space between strings and there should
    #not be a space between the temperature value and the sign
    tempstring = "Temperature in fahrenheit is {:0.2f}".format(fahrenheit)+ '\u00b0'
    print(tempstring)

main()

