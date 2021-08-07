# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 7th, 2021

base = float((input("Enter number: ")))
exponent = float((input("To the power of: ")))

result = pow(base, exponent)

formatted_result = "{:.0f}".format(result)

print(f"Result: {formatted_result}")
