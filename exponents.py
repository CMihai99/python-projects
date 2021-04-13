'''
Developed by: Calinescu Mihai
Date: 16 Mar, 2021

Github: https://github.com/CMihai99
'''


base = float((input("Base number: ")))
exponent = float((input("Exponent: ")))

ans = pow(base, exponent) # Declare variable

formatted_ans = "{:.4f}".format(ans) # Format answer

print("Exponential Value:", formatted_ans)