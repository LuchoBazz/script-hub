import random
import string

ALPHA = string.ascii_letters + string.digits + string.punctuation

def generate_password(n):
    password = ''.join(random.choice(ALPHA) for _ in range(n))
    return password

n = 32
password = generate_password(n)
print(password)
