# Project 1 : Printing Receipt 

# Define store information
store_name = "Coding Temple, Inc."
store_address = "283 Franklin St."
store_city = "Boston, MA"

# Define product names and prices
product_1 = "Books"
price_1 = 49.95

product_2 = "Computer"
price_2 = 579.99

product_3 = "Monitor"
price_3 = 124.89

# Calculate total price
total_price = price_1 + price_2 + price_3

# Print the receipt
print("*" * 50)
print(f"{store_name.center(50)}")
print(f"{store_address.center(50)}")
print(f"{store_city.center(50)}")
print("-" * 50)
print(f"{'Product Name':<20}{'Product Price':>20}")
print(f"{product_1:<20}${price_1:>19.2f}")
print(f"{product_2:<20}${price_2:>19.2f}")
print(f"{product_3:<20}${price_3:>19.2f}")
print("-" * 50)
print(f"{'Total':<20}${total_price:>19.2f}")
print("-" * 50)
print("Thanks for shopping with us today!".center(50))
print("*" * 50)