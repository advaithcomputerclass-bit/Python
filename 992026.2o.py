import random
import string
def generate_the_strongest_password(length):
   characters = string.ascii_letters+string.digits+string.punctuation
   password=" "
   for i in range(length):
     password+=random.choice(characters)
   return password
length = int(input("enter len of pwd:"))
print("generated password",generate_the_strongest_password(length))