import random
import string
import operator

N = random.randint(10, 1001)
print(N)
caractere_numero = {}


for i in range(N):
    longueur = random.randint(4, 8)
    caractere = ''.join(random.choice(string.ascii_lowercase) for _ in range(longueur))
    if caractere not in caractere_numero:
        caractere_numero[caractere] = random.randint(1, 100)  
    numero = caractere_numero[caractere]
    print(f"{caractere} {numero}")


article = {}
for caractere, numero in caractere_numero.items():
    if caractere in article:
        article[caractere] += numero
    else:
        article[caractere] = numero

caractere_max = max(article, key=article.get)
print(f"{caractere_max}")
