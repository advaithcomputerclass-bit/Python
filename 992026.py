import random 
import string
def generate_pwd(length):
    characters = string.ascii_letters+string.digits+string.punctuation
    password = " "
    for i in range(length):
        password+=random.choice(characters)
    return password
length = int(input("enter pwd length:"))
print("Generated pwd",generate_pwd(length))