import string
import random

print("welcome to password generator")

length = int(input("enter the length of password (number): "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits

all = lower + upper + num

temp = random.sample(all, length)
password = "".join(temp)
print(password)

input("press enter to exit")
