# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 6th, 2021

year = int(input("Enter year: "))

# Check if the year is a leap year
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("The year", year, "is a leap year")

       else:
           print("The year", year, "is not a leap year") 

   else:
       print("The year", year, "is a leap year")

else:
   print("The year", year, "is not a leap year")
