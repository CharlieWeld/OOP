#bookstore.py
#calculate the wholesale price of books

#get the cover price from the user
cover_price = float(input("Enter cover price of book: "))
discount = int(input("Enter the percentage discount on books: "))

#divide the discount by 100 to get it in decimal form
discount /= 100

number_books = int(input("Enter the number of books: "))

shipping_cost = 3 + (0.75 * (number_books-1))

wholesale_cost = number_books*(cover_price*(1-discount)) + shipping_cost

print("The wholesale cost of the books are", "%.2f" % wholesale_cost)
