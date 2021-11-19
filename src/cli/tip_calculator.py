# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 10th, 2021

meal = float(input("Enter meal price: "))
tip = 0.15

total_tip = meal * tip
total_price = meal + meal * tip

print("Meal: %.2f" % meal)
print("Tip: %.2f" % total_tip)
print("Total: %.2f" % total_price)
