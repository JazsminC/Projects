##
# This program simulates a coin machine that receives a certain amount of coins and then
# dispenses smallest combination of coins.
# Note: You can only enter in coin amounts. Its the machines job to breakdown what coins we will be using Ex: (2.00 = 200 coins)
#
# Define the price of a quarter, dime, nickel and penny
Quarter_price = 25
Dime_price = 10
Nickel_price = 5
Penny_price = 1

# Obtain the number of cents.
centStr = input("Enter the number of cents: ")
cents = int(centStr)

# Compute and print the coin combination dispensed
quarters = cents // 25
dimes = (cents - (quarters * Quarter_price)) // Dime_price
nickels = (cents - (quarters * Quarter_price) - (dimes * Dime_price)) // Nickel_price
pennies = (cents - (quarters * Quarter_price) - (dimes * Dime_price) - (nickels * Nickel_price)) // Penny_price

print("Pennies:   %6d" % pennies)
print("Nickels:   %6d" % nickels)
print("Dimes:     %6d" % dimes)
print("Quarters:  %6d" % quarters)
