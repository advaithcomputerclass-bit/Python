def find_numbers(a,b,c):
    largest = max(a,b,c)
    smallest = min(a,b,c)
    print("largest number",largest)
    print("smallest number",smallest)
a = int(input("enter number a:"))
b = int(input("enter number b:"))
c = int(input("enter number c:"))
find_numbers(a,b,c)