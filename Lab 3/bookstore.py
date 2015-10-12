#Calculate the wholesale cost of a number of books
#Based on the cover price, discount and shipping costs

def calculate_cost(cover_price, discount, number_books):
    discount_price = cover_price * (1 - (discount/100))
    shipping_cost = 3 + 0.75*(number_books-1)
    wholesale_cost = (number_books * discount_price) + shipping_cost
    return wholesale_cost

def main():
    cover_price = float(input("Enter the cover price of the book: "))
    discount = float(input("Enter the percentage discount: "))
    number_books = int(input("Enter the number of books: "))

    wholesale_cost = calculate_cost(cover_price, discount, number_books)

    print("The wholesale cost is \u20AC", "{:.2f}".format(wholesale_cost), sep='')
    

main()
