#fonction tri
def triSelection(l):
    for i in range(len(l) - 1):
# Trouver l'indice du minimum à partir de la position i
        indiceMin = i
        for j in range(i + 1, len(l)):
            if l[j] < l[indiceMin]:
                indiceMin = j
# Échange l'élément à la position i avec l'élément minimum trouvé
        l[i], l[indiceMin] = l[indiceMin], l[i]
def indiceMin(tab, j):
    indice_minimum = j
#trouver l'indice de la plus petite valeur à partir de l'indice j
    for i in range(j, len(tab)):
        if tab[i] < tab[indice_minimum]:
            indice_minimum = i
    return indice_minimum

tableau = [4,8,2,10,1,9,7,6,3,5]
print("Tableau original:", tableau)
triSelection(tableau)
print("Tableau trié:", tableau)