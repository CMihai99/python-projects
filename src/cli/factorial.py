# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 7th, 2021

num = int(input("Enter number: "))

factorial = 1

if num < 0:
   print("Factorial only works for positive integers")

elif num == 0:
   print("Factorial of 0 is 1")

else:
   for i in range(1, num + 1):
      factorial = factorial * i

   print(f"Factorial of {num} is {factorial}")
