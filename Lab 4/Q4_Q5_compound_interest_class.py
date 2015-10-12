#Calculate the average of three numbers
#Create a class to encapsulate the banking functions

class Banking():
    """ Calculates simple and compound interest """
    def __init__(self, principle=0, rate=0, years=0, periods=0):
        #Create instance variables
        self.principle = principle
        self.rate = rate
        self.periods = periods
        self.years = years
        self.balance = 0

    def calculate_rate(self):
    #Check if a percentage character was entered and if so strip it away
    #If the user entered a rate lower than 1 assume
        if isinstance(self.rate, str): # If rate is a string convert to float
            self.rate = float(self.rate.strip('%')) #Strip out the percentage sign
            
        if self.rate > 1:
           self.rate /= 100
        return self.rate

    ################### Setter Methods ########################
    
    def set_variables(self, var_list): # Set all variables from a list
        self.principle = var_list[0]
        self.rate = var_list[1]
        self.years = var_list[2]
        self.periods = var_list[3]
        
    def set_principle(self, principle): # Set principle directly
        self.principle = principle

    def set_rate(self, rate): # Set rate directly
        self.rate = rate

    def set_periods(self, periods): # Set number of periods directly
        self.periods = periods

    def set_years(self, years): # Set number of years directly
        self.years = years

    ########################## Getter Methods #######################
    def get_variables(self, compound): # Get each value from the user and put them in a list
        print("\nEnter the principle, rate, years & compound if applicable\n"
              "For Rate enter a percentage value (1 - 100)\n"
              "Values from 0 - 1 will be treated as (0 - 100%)\n")
        
        principle = float(input("Enter the principle amount: "))
        rate = input("Enter the percentage interest rate: ")
        years = float(input("Enter the number of years the interest is over: "))
        if compound: # if compound is through ask for periods per year
            periods = float(input("Enter the number of times per year the interest is compounded: "))

        var_list = [principle, rate, years, periods]
        return var_list

    #########################  Interest Methods  ####################
    def simple_interest(self): # Calculate the simple interest 
        self.rate = self.calculate_rate() # Check that rate is not a string
        self.balance = self.principle + (self.principle * self.rate * self.years)
        return self.balance

    def compound_interest(self): # Calculate the compound interest
        self.rate = self.calculate_rate()
        compound = pow((1+self.rate/self.periods), (self.periods*self.years))
        self.balance = self.principle * compound
        return self.balance

    #Calculate the compound interest and print the balance at each period
    def compound_interest_verbose(self): 
        self.rate = self.calculate_rate()
        #Create a string that will output a summary of the how the end balance was determined
        output_string = "\n{:.2f}".format(self.principle) + " at " + "{:.1f}".format((self.rate*100))
        output_string += "% compounded " + "{:.0f}".format(self.periods) + " times per year for " 
        output_string += "{:.0f}".format(self.years) + " years yields " + "{:.2f}".format(self.compound_interest())
        print(output_string)

        #Print the balance at each compound period
        for i in range(1, (int(self.periods * self.years))+1):
            balance=self.principle*(pow((1+self.rate/self.periods), i))
            print("Quarter:{:>3}".format(i), "<>", "Balance:{:>10}".format("{:,.2f}".format(balance)))
        print("\n")

##################################  Main  ##############################################
            
# Define main function
def main():

    #Create 3 Banking objects: 
    simple_bank = Banking(1000, 2, 6) # Create object to calculate simple interest
    compound_bank = Banking() #Create object to calculate compound interest
    compound_bank2 = Banking() #Create object to calculate compound interest and print compounds

    # Get variables from user; a list is used to hold the variables
    bank_variables = compound_bank.get_variables(True)
    #bank_variables2 = compound_bank.get_variables(True)

    # Set the variables of the objects
    compound_bank.set_variables(bank_variables) 
    #compound_bank2.set_variables(bank_variables2)

    # Calculate simple interest and compound interest
    #simple_balance = simple_bank.simple_interest()
    #compound_balance = compound_bank.compound_interest()
    compound_balance2 = compound_bank.compound_interest_verbose()

    # Print simple interest, compound interest and compare the difference
    #print("The balance from simple interest is", "{:,.2f}".format(simple_balance))
    #print("The balance compound interest is", "{:,.2f}".format(compound_balance))
    #print("The difference between the interest rates is", "{:,.2f}".format(compound_balance-simple_balance))


#Call main program
if __name__=='__main__': 
    main() 



    
