
# Creating a shopping programme that will  continuosly ask the user for a food product and the price of the product
# Have an exist clause  if the user wishes to stop additing more things to their cart
# At the end of the food items and the total cost to the  user

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or press q to quit")
    if food == 'q':
        break
    else:
        price = float (input(f"Enter the price of the{food}:R"))
        foods.append(food)
        prices.append(price)

print ("-----YOUR CART-----")

for food in foods:
    price(food)

for price in prices:
    total = total + price

    price(f"Your total is: R{total}")