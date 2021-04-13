'''
Developed by: Calinescu Mihai
Date: 14 Mar, 2021

Github: https://github.com/CMihai99
'''


# Assign values to the variables
meal = int(input("Input meal price: "))
tax = 0.0675
tip = 0.15

# Calculate total values
total_meal = meal + meal * tax
total_tip = meal * tip
total_tipnotax = meal + meal * tip
total_tipwithtax = total_meal + meal * tip

# Print result
print("Meal: %.2f" % meal)
print("Tip: %.2f" % total_tip)
print("Total without tax: %.2f" % total_tipnotax)
print("Total with tax: %.2f" % total_tipwithtax)
