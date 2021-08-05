# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 5th, 2021

num = int(input("Enter number: "))

factorial = 1

# Check if the number is negative
if num < 0:
   print("Factorial only works for positive integers")

# Check if the number is 0
elif num == 0:
   print("Factorial of 0 is 1")

else:
   for i in range(1, num + 1):
      factorial = factorial * i

   print("Factorial of", num, "is", factorial)
