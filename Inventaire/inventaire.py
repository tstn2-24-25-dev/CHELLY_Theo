import random
import string


N = random.randint(10, 1000)
print(N)
for i in range(N):
    longueur = random.randint(4, 8)
    caractere = ''.join(random.choice(string.ascii_lowercase) for _ in range(longueur))
    numero = random.randint(1, 100)
    print(f"{caractere} {numero}")
    