'''
Developed by: Calinescu Mihai
Date: 15 Mar, 2021

Github: https://github.com/CMihai99
'''

# CONVERTS: ml, l, oz, cubic ft, cubic in, cubic cm, cubic m


# Input
num1 = input('Enter the value: ')
unit1 = input('Convert from (ml, l, oz, cubic ft, cubic in, cubic cm, cubic m):  ')
unit2 = input('To (ml, l, oz, cubic ft, cubic in, cubic cm, cubic m): ')

# Calculations

# ml
if unit1 == "ml" and unit2 == "l":
    ans = float(num1)/1000
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "ml" and unit2 == "oz":
    ans = float(num1)/29.574
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "ml" and unit2 == "ml":
    ans = float(num1)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "ml" and unit2 == "cubic ft":
    ans = float(num1)/28317
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "ml" and unit2 == "cubic in":
    ans = float(num1)/16.387
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "ml" and unit2 == "cubic cm":
    ans = float(num1)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "ml" and unit2 == "cubic m":
    ans = float(num1)/1000000
    formatted_ans = "{:.6f}".format(ans)
    print(formatted_ans, unit2)

# l
elif unit1 == "l" and unit2 == "ml":
    ans = float(num1)*1000
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "l" and unit2 == "oz":
    ans = float(num1)*33.814
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "l" and unit2 == "l":
    ans = float(num1)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "l" and unit2 == "cubic ft":
    ans = float(num1)/28.317
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "l" and unit2 == "cubic in":
    ans = float(num1)*61.024
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "l" and unit2 == "cubic cm":
    ans = float(num1)*1000
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "l" and unit2 == "cubic m":
    ans = float(num1)/1000
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

# oz
elif unit1 == "oz" and unit2 == "ml":
    ans = float(num1)*29.574
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "oz" and unit2 == "l":
    ans = float(num1)/33.814
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "oz" and unit2 == "oz":
    ans = float(num1)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "oz" and unit2 == "cubic ft":
    ans = float(num1)/958
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "oz" and unit2 == "cubic in":
    ans = float(num1)*1.805
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "oz" and unit2 == "cubic cm":
    ans = float(num1)*29.574
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "oz" and unit2 == "cubic m":
    ans = float(num1)/33814
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

# cubic ft
elif unit1 == "cubic ft" and unit2 == "ml":
    ans = float(num1)*28317
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cubic ft" and unit2 == "l":
    ans = float(num1)*28.317
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cubic ft" and unit2 == "oz":
    ans = float(num1)*958
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cubic ft" and unit2 == "cubic ft":
    ans = float(num1)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cubic ft" and unit2 == "cubic in":
    ans = float(num1)*1728
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cubic ft" and unit2 == "cubic cm":
    ans = float(num1)*28317
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cubic ft" and unit2 == "cubic m":
    ans = float(num1)/35.315
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

# cubic in
elif unit1 == "cubic in" and unit2 == "ml":
    ans = float(num1)*16.387
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cubic in" and unit2 == "l":
    ans = float(num1)/61.024
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cubic in" and unit2 == "oz":
    ans = float(num1)/1.805
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cubic in" and unit2 == "cubic ft":
    ans = float(num1)/1728
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cubic in" and unit2 == "cubic in":
    ans = float(num1)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cubic in" and unit2 == "cubic cm":
    ans = float(num1)*16.387
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cubic in" and unit2 == "cubic m":
    ans = float(num1)/61024
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

# cubic cm
elif unit1 == "cubic cm" and unit2 == "ml":
    ans = float(num1)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cubic cm" and unit2 == "l":
    ans = float(num1)/1000
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cubic cm" and unit2 == "oz":
    ans = float(num1)/29.574
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cubic cm" and unit2 == "cubic ft":
    ans = float(num1)/28317
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cubic cm" and unit2 == "cubic in":
    ans = float(num1)/16.387
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cubic cm" and unit2 == "cubic cm":
    ans = float(num1)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cubic cm" and unit2 == "cubic m":
    ans = float(num1)/1000000
    formatted_ans = "{:.6f}".format(ans)
    print(formatted_ans, unit2)

# cubic m
elif unit1 == "cubic m" and unit2 == "ml":
    ans = float(num1)*1000000
    formatted_ans = "{:.6f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cubic m" and unit2 == "l":
    ans = float(num1)*1000
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cubic m" and unit2 == "oz":
    ans = float(num1)*33814
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cubic m" and unit2 == "cubic ft":
    ans = float(num1)*35.315
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cubic m" and unit2 == "cubic in":
    ans = float(num1)*61024
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cubic m" and unit2 == "cubic cm":
    ans = float(num1)*1000000
    formatted_ans = "{:.6f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cubic m" and unit2 == "cubic m":
    ans = float(num1)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)