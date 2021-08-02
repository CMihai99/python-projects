'''
Developed by: Calinescu Mihai
Date: 8 Apr, 2021

Github: https://github.com/CMihai99
'''


num = int(input("Enter a number: "))
factorial = 1

# Check if the number is negative, positive or zero
if num < 0:
   print("Factorial only works for positive integers")

elif num == 0:
   print("The factorial of 0 is 1")

else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
