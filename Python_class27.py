def largest(a,b,c):
    if a == b == c:
        print("all numbers are equal",a)
    elif a == b and a > c:
        print("a,b are largest numbers",a)
    elif b == c and b > a:
        print("b,c are largest numbers",b)
    elif c == a and c > b:
        print("c,a are the largest numbers",c)
    elif a > b and a > c:
        print("a is the largest number",a)
    elif b > a and b > c:
        print("b is the largest number",b)
    else:
        print("c is the largest number",c) 
def smallest(a,b,c):
    if a == b == c:
        print("all numbers are equal",a)
    elif a == b and a < c:
        print("a,b are smallest numbers",a)
    elif b == c and b < a:
        print("b,c are smallest numbers",b)
    elif c == a and c < b:
        print("c,a are the smallest numbers",c)
    elif a < b and a < c:
        print("a is the smallest number",a)
    elif b < a and b < c:
        print("b is the smallest number",b)
    else:
        print("c is the smallest number",c)
a = int(input("enter a:"))
b = int(input("enter b:"))
c = int(input("enter c:"))
largest(a,b,c)
smallest(a,b,c)  