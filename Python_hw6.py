def type_of_number(nums):
    if nums > 0:
        print("this number positive thoughts",nums)
    elif nums < 0:
        print("this number has negative thoughts",nums)
    else:
        print("this number has zero thoughts",nums)
num10 = int(input("enter number:"))
type_of_number(num10)