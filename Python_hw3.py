def largest(num1 , num2 , num3):
    if num1 > num2:
        num = num1
    else:
        num = num2
    
    if num3 > num:
        print("the largest number is",num3)
    else:
        print("the largest number is",num)
 
def smallest(num1 , num2 , num3):
     if num1 > num2:
          num = num2
     else:
          num = num1
          
     if num3 > num:
          print("the smallest number is",num)
     else:
          print("the smallest number is",num3)    
num = 0
num1 = int(input("enter number1:"))
num2 = int(input("enter number2:"))
num3 = int(input("enter number3:"))
largest(num1 , num2 , num3)
smallest(num1 , num2 , num3)