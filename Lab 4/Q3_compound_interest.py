

def simple_interest(principle, rate, periods):
    balance = principle*(1 + (rate/100)*periods)
    return balance

def compound_interest(principle, rate, periods, compounds):
    
    for i in range(1, periods*compounds):
        balance = principle * pow((1 + ((rate/100/12))),  (i))
        print("Quarter: ", i, "Balance: ", "%.2f" % balance)

    return balance

def main():
    principle = float(input("Enter the principle amount: "))
    rate = float(input("Enter the percentage interest rate: "))
    periods = int(input("Enter the number of years: "))
    compounds = int(input("Enter the number of periods per year: "))
    #balance1 = simple_interest(principle, rate, periods)
    balance2 = compound_interest(principle, rate, periods, compounds)
   # print("The balance is: ", "%.2f" % balance1)
    print("The compound interest is: ", "%.2f" % balance2)
    #print("The difference is: ", "%.2f" % (balance2-balance1))

main()
