def can_vote(age):
    if age >= 18:
        print("You are eligible to vote")
    else:
        print("Get out of here!Come back to vote when eighteen years of age")
your_age = int(input("Enter age:"))
can_vote(your_age)        