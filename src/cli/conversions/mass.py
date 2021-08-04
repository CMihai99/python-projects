'''
Developed by: Calinescu Mihai
Date: 16 Mar, 2021

Github: https://github.com/CMihai99
'''

# CONVERTS: mg, g, kg, tonne, oz, lbs


# Input
num1 = input('Enter the value: ')
unit1 = input('Convert from (mg, g, kg, tonne, oz, lbs):  ')
unit2 = input('To (mg, g, kg, tonne, oz, lbs): ')

# Calculations

# mg
if unit1 == "mg" and unit2 == "mg":
    ans = float(num1)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "mg" and unit2 == "g":
    ans = float(num1)/1000
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "mg" and unit2 == "kg":
    ans = float(num1)/1000000
    formatted_ans = "{:.6f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "mg" and unit2 == "tonne":
    ans = float(num1)/1000000000
    formatted_ans = "{:.9f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "mg" and unit2 == "oz":
    ans = float(num1)/28350
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "mg" and unit2 == "lbs":
    ans = float(num1)/453592
    formatted_ans = "{:.6f}".format(ans)
    print(formatted_ans, unit2)

# g
if unit1 == "g" and unit2 == "mg":
    ans = float(num1)*1000
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "g" and unit2 == "g":
    ans = float(num1)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "g" and unit2 == "kg":
    ans = float(num1)/1000
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "g" and unit2 == "tonne":
    ans = float(num1)/1000000
    formatted_ans = "{:.6f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "g" and unit2 == "oz":
    ans = float(num1)/28.35
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "g" and unit2 == "lbs":
    ans = float(num1)/454
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

# kg
if unit1 == "kg" and unit2 == "mg":
    ans = float(num1)*1000000
    formatted_ans = "{:.6f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "kg" and unit2 == "g":
    ans = float(num1)*1000
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "kg" and unit2 == "kg":
    ans = float(num1)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "kg" and unit2 == "tonne":
    ans = float(num1)/1000
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "kg" and unit2 == "oz":
    ans = float(num1)*35.274
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "kg" and unit2 == "lbs":
    ans = float(num1)*2.205
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

# tonne
if unit1 == "tonne" and unit2 == "mg":
    ans = float(num1)*1000000000
    formatted_ans = "{:.9f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "tonne" and unit2 == "g":
    ans = float(num1)*1000000
    formatted_ans = "{:.6f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "tonne" and unit2 == "kg":
    ans = float(num1)*1000
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "tonne" and unit2 == "tonne":
    ans = float(num1)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "tonne" and unit2 == "oz":
    ans = float(num1)/35274
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "tonne" and unit2 == "lbs":
    ans = float(num1)*2205
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

# oz
if unit1 == "oz" and unit2 == "mg":
    ans = float(num1)*28350
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "oz" and unit2 == "g":
    ans = float(num1)*28.35
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "oz" and unit2 == "kg":
    ans = float(num1)/35.274
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "oz" and unit2 == "tonne":
    ans = float(num1)/35274
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "oz" and unit2 == "oz":
    ans = float(num1)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "oz" and unit2 == "lbs":
    ans = float(num1)/16
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

# lbs
if unit1 == "lbs" and unit2 == "mg":
    ans = float(num1)*453592
    formatted_ans = "{:.6f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "lbs" and unit2 == "g":
    ans = float(num1)*454
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "lbs" and unit2 == "kg":
    ans = float(num1)/2.205
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "lbs" and unit2 == "tonne":
    ans = float(num1)/2205
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "lbs" and unit2 == "oz":
    ans = float(num1)*16
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "lbs" and unit2 == "lbs":
    ans = float(num1)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)