# This program calculates the average of three values

def calc_average(num1, num2, num3):
    average = int((num1 + num2 + num3)/3) #Convert result to an int to keep it clean
    return average

def main():
    num = [1,2,3] # Initialise list. N.B. There are better ways to do this 
    for i in range(3):
        num[i] = int(input("Enter value " + str(i+1) + ": "))
        
    average = calc_average(num[0], num[1], num[2])
    print("The average value is", average)

main()

#1. Inputting a float won't make a difference since the arithemtic operation will resolve to a float
#2. Inputtin an int will change to a float
#3. Print a float adds decminal points (only 1 if there is no remainder)
#4. Printing an int works as expected
