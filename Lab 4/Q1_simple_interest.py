
def simple_interest(principle, rate, periods):
    balance = principle + (periods*(principle * (rate/100)))
    return balance

def main():
    principle = float(input("Enter the principle amount: "))
    rate = float(input("Enter the percentage interest rate: "))
    periods = float(input("Enter the number of years: "))
    balance = simple_interest(principle, rate, periods)
    print("The balance is: ", "%.2f" % balance)

main()
