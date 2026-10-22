# # # # # FRUITS = ["APPLE","BANANA","GUAVA","papaya","mango"]
# # # # # length_of_fruits = len(FRUITS)
# # # # # print(length_of_fruits)
# # # # # newfruit=FRUITS.append("pineapple")
# # # # # print(FRUITS)
# # # # sports = ('hockey','cricket','football')
# # # # print(sports)
# # # # a=sports[2]
# # # # print(a)
# # # # b=sports.count("hockey")
# # # # print(b)
# # # # c= sports.index("cricket")
# # # # print(c)
# # # age = int(input("enter your age:"))
# # # if age >= 18:
# # #     print("more than 18")
# # # else:
# # #     print("less than 18")

# # while True:
# #     no = int(input("enter your number:"))
# #     if no%2 !=0:
# #         print("no is odd")
# #     else:
# #         print("no is even")
# n=int(input("enter n:"))
# sum=0
# for i in range(1,n+1):
#   sum+=i                          imp
# print("sum=",sum)
n=int(input("enter n:"))
sum=0
i=1
while i<=n:
   sum+=i
   i+=1
print("sum =",sum)