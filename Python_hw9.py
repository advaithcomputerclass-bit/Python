nums = [2,4,6,8,1,3,5,7,9,656,5,4534,34545,3,352,34324,42424,23421431233,3]
even_count = 0
odd_count = 0
for i in nums:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers =",even_count)
print("Odd numbers =",odd_count)