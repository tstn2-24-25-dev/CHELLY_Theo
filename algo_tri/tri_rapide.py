#fonction tri
def tri_rapide(tableau, debut, fin):
    pivot = tableau [fin -1]
    curseur = debut

    for i in range(debut, fin -1):
        if tableau[i] <= pivot:
           tableau[i], tableau[curseur] = tableau[curseur], tableau[i]
           curseur += 1 
    tableau[curseur], tableau[fin -1] = tableau[fin -1], tableau[curseur]
    return curseur





#test
tableau =[4,8,2,10,1,9,7,6,3,5]
print (f'tableau original : ', tableau)
tri_rapide(tableau)
print (f'tableau trié : ', tableau)
