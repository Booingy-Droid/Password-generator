import string
import random
print("""

█▀█ ▄▀█ █▀ █▀ █░█░█ █▀█ █▀█ █▀▄   █▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█
█▀▀ █▀█ ▄█ ▄█ ▀▄▀▄▀ █▄█ █▀▄ █▄▀   █▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄""")


length = int(input("Inter how long you need the password: "))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
spec = string.punctuation

combined = lower + upper + num + spec

temp = random.sample(combined,length)
code = "".join(temp)
print(code)
