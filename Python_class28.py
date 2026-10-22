def factorial(nums):
    if nums == 0 or nums == 1:
        return 1
    else:
        return nums*factorial(nums-1) 
num1 = int(input("enter number:"))
print("factorial =",factorial(num1))