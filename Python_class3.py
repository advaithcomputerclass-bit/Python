a1 = int(input("enter number 1 "))
a2 = int(input("enter number 2 "))
a3 = int(input("enter number 3 "))
if a1 >= a2 and a1 >= a3:
    print("a1 is the greatest number",a1)
elif a2 >= a1 and a2 >= a3:
    print("a2 is the greatest number",a2)
else:
    print("a3 is the greatest number",a3)