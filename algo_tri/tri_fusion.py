# Fonction de tri par fusion
def triFusion(tab):
    if len(tab) <= 1:
        return tab
    milieu = len(tab) // 2
    gauche = triFusion(tab[:milieu])  # partie gauche
    droite = triFusion(tab[milieu:])  # partiee droite
    return fusionner(gauche, droite)





# Fonction qui permet de fusionner
def fusionner(tab1, tab2):
    i, j = 0, 0
    resultat = []




    # Fusionner les deux tableaux
    while i < len(tab1) and j < len(tab2):
        if tab1[i] < tab2[j]:
            resultat.append(tab1[i])
            i += 1
        else:
            resultat.append(tab2[j])
            j += 1


#ajouter les resultats
    resultat.extend(tab1[i:])
    resultat.extend(tab2[j:]) 
    return resultat





# Test
tab = [4, 8, 2, 10, 1, 9, 7, 6, 3, 5]
print(f'tableau original : ', tab)
tab = triFusion(tab)
print(f'tableau trié : ', tab)
