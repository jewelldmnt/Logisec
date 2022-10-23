from random import choice
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation
all_char = lowercase + uppercase + numbers + symbols


# composed of all ascii characters
def all_characters(pw_len):
    password = ''
    for i in range(pw_len):
        password += ''.join(choice(all_char))
    return password


# composed of (1 symbol)(2 numbers)(2 uppercase)(lowercase)
def easy_to_memorize(pw_len):
    symbol = choice(symbols)
    upper = ''
    num = ''
    lower = ''

    for i in range(2):
        num += ''.join(choice(numbers))
    for j in range(2):
        upper += ''.join(choice(uppercase))
    for k in range(pw_len-5):
        lower += ''.join(choice(lowercase))

    password = symbol + num + upper + lower
    return password
