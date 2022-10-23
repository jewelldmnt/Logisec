# This is a random password generator
from pwd_gen import all_characters, easy_to_memorize

pwd_len = int(input("Enter the length of password: (6, 8, 12): "))
pwd_type = int(input("\n1. All characters \n2. Easy to remember \nEnter the type of password: "))

password = all_characters(pwd_len) if pwd_type == 1 else easy_to_memorize(pwd_len)
print(f"\nYour password is: {password}")
