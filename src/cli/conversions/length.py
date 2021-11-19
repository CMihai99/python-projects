# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: November 19th, 2021

# Converts: mm, cm, m, km, ft, in

num1 = input('Enter the value: ')
unit1 = input('Convert from (mm, cm, m, km, ft, in):  ')
unit2 = input('To (m, cm, mm, km, ft, in): ')

# mm
if unit1 == "mm" and unit2 == "mm":
    ans = float(num1)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "mm" and unit2 == "cm":
    ans = float(num1)/10
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "mm" and unit2 == "m":
    ans = float(num1)/1000
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "mm" and unit2 == "km":
    ans = float(num1)/1000000
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "mm" and unit2 == "ft":
    ans = float(num1)/305
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "mm" and unit2 == "in":
    ans = float(num1)/25.4
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

# cm
if unit1 == "cm" and unit2 == "mm":
    ans = float(num1)*10
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cm" and unit2 == "cm":
    ans = float(num1)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cm" and unit2 == "m":
    ans = float(num1)/100
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cm" and unit2 == "km":
    ans = float(num1)/1000
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cm" and unit2 == "ft":
    ans = float(num1)/30.48
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "cm" and unit2 == "in":
    ans = float(num1)/2.54
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

# m
if unit1 == "m" and unit2 == "mm":
    ans = float(num1)*1000
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "m" and unit2 == "cm":
    ans = float(num1)*100
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "m" and unit2 == "m":
    ans = float(num1)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "m" and unit2 == "km":
    ans = float(num1)/1000
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "m" and unit2 == "ft":
    ans = float(num1)*3.281
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "m" and unit2 == "in":
    ans = float(num1)*39.37
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

# km
if unit1 == "km" and unit2 == "mm":
    ans = float(num1)*1000000
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "km" and unit2 == "cm":
    ans = float(num1)*100000
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "km" and unit2 == "m":
    ans = float(num1)/1000
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "km" and unit2 == "km":
    ans = float(num1)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "km" and unit2 == "ft":
    ans = float(num1)*3281
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "km" and unit2 == "in":
    ans = float(num1)*39370
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

# ft
if unit1 == "ft" and unit2 == "mm":
    ans = float(num1)*305
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "ft" and unit2 == "cm":
    ans = float(num1)*30.48
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "ft" and unit2 == "m":
    ans = float(num1)/3.281
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "ft" and unit2 == "km":
    ans = float(num1)/3281
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "ft" and unit2 == "ft":
    ans = float(num1)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "ft" and unit2 == "in":
    ans = float(num1)*12
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

# in
if unit1 == "in" and unit2 == "mm":
    ans = float(num1)*25.4
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "in" and unit2 == "cm":
    ans = float(num1)*2.54
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "in" and unit2 == "m":
    ans = float(num1)/39.37
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "in" and unit2 == "km":
    ans = float(num1)/39370
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "in" and unit2 == "ft":
    ans = float(num1)/12
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "in" and unit2 == "in":
    ans = float(num1)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)
