# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 4th, 2021

base = float((input("Enter number: ")))
exponent = float((input("To the power of: ")))

result = pow(base, exponent)

# Format result
formatted_result = "{:.0f}".format(result)
print("Result:", formatted_result)
