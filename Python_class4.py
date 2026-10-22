num1 = int(input("enter number"))
num2 = int(input("enter number"))
opi = input("Enter operator(+,-,*,/) ")
if opi == '+':
    print(num1 + num2)
elif opi == '-':
    print(num1- num2)
elif opi == '*':
    print(num1 * num2)
elif opi == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print("undefined")
else:
    print("invalid operator")        