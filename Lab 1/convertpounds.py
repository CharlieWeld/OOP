#convert pounds sterling to euros

pounds = float(input("Enter the number of pounds sterling: "))

conversion_rate = 1.37001
euros = pounds * conversion_rate
print("The equivalent euros are", format(euros, ".2f"))
