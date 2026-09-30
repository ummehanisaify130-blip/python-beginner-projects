import random
import string
print("---PYTHON PASSWORD GENERATOR---")
length = int(input("enter password length(eg. 8, 12):"))
#character to use
chars = string.ascii_letters+string.digits+string.punctuation
#generate password
password = ""
for i in range(length):
    password+= random.choice(chars)

print("\nYour strong password is:",password)
print("\nkeep it safe")
