'''
Developed by: Calinescu Mihai
Date: 8 Apr, 2021

Github: https://github.com/CMihai99
'''


year = int(input("Enter a year: "))

if (year % 4) == 0: # Check if the year is a leap year
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))   
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
