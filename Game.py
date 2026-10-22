import random as ra
value=ra.randint(1,50)
print("welcome to my guessing game🎮.guess the number")
hyy = int(input("enter number:"))
while hyy!=value:
    if hyy>value:
        print("value given is too high")
    else:
        print("value given is too low")
    hyy = int(input("try again"))
print("congrats!you got it right👏")