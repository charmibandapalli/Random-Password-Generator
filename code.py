import random
import string

def generate_password(length=12):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

print("Generated Password:", generate_password())
