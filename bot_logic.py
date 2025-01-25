import random
import string

def gen_pass(pass_length):
    # Combinar letras, números y símbolos
    elements = string.ascii_letters + string.digits + "+-/*!&$#?=@<>"
    password = ""

    for _ in range(pass_length):
        password += random.choice(elements)

    return password
print( gen_pass(10))


    