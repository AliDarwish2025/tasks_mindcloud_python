import random
import string

def generate_password(length):
    if length < 5:
        return

    upper = string.ascii_uppercase  
    lower = string.ascii_lowercase   
    digits = string.digits           
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/"

    pass_char = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(symbols)
    ]
    all_chars = upper + lower + digits + symbols
    pass_char += random.choices(all_chars, k=length - 4)

    return "".join(pass_char)

while True:
    user_length = int(input("enter the len of number: "))
    if user_length < 5:
        print("unvalid number")
        continue
    print("the password is :", generate_password(user_length))
    if user_length >= 5:
        break
