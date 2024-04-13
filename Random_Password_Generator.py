import random
import string
pass_len = 10
char_values = string.ascii_letters + string.punctuation + string.digits
password = ""
for i in range(pass_len):
    password += random.choice(char_values)
print(password)