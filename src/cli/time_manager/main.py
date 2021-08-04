'''
Developed by: Calinescu Mihai
Date: 30th Mar, 2021

Github: https://github.com/CMihai99
'''


'''
TASKS:
- Convert minutes to hours
- Create database of things you can do in the remaining time
    - Web scrape activities
    - Link file to main.py
'''

# Import Required Packages
import time

# 1. Greet the user
print("Welcome to Time Manager!")
time.sleep(2)
print("Please enter how much time you spend on each of the preselected activities.")
time.sleep(2.5)
print("If you dont practice some of these activites, type '0'.")
time.sleep(2.5)
print("Reminder: Time Manager only accepts hours at the moment.")
time.sleep(2.5)

# 2. Enter how many hours you spend on sleeping
sleeping = int(input("How many hours do you sleep? "))

# 3. Enter how many hours you spend on traveling
traveling = int(input("How many hours do you travel? "))

# 4. Print an approximation of how many hours you spend on eating
eating = int(input("How many hours do you spend on eating? "))

# 5. Print an approximation of how many hours you spend on going to the bathroom
bathroom = int(input("How many hours do you spend on going to the bathroom? "))

# 6. Enter how many hours you spend on morning routines
morning_routine = int(input("How many hours do you spend on your morning routine? "))

# 7. Enter how many hours you spend on evening routines
evening_routine = int(input("How many hours do you spend on your evening routine? "))

# 8. Enter how many hours you spend on exercising
exercising = int(input("How many hours do you exercise? "))

# 9. Print total amount of hours spent
total_hours_spent = sleeping + traveling + eating + bathroom + morning_routine + evening_routine + exercising
print("Total hours spent:", total_hours_spent)

# 10. Print hours remaining
remaining_hours = 24 - total_hours_spent
time.sleep(1)
print("Hours remaining:", remaining_hours)

# 11. Things you can do in the remaining time
time.sleep(1.5)
print("Activities you can do in the remaining time:")
time.sleep(1.5)
print("Have a Costume Night")
time.sleep(1.5)
print("Throw an Indoor Picnic")
time.sleep(1.5)
print("Have a Christmas Party (*In the Summer)")
time.sleep(1.5)
print("Host an International Dinner Night")
time.sleep(2)
print("Film a “Newscast“")
time.sleep(1.5)
print("And more")

# 12. Finish program
time.sleep(3)
print("Have a great day!")