#fonction tri
def tri_rapide(tab, debut, fin):
    pivot = tab[fin -1]
    curseur = debut

    for i in range(debut, fin -1):
        if tab[i] <= pivot:
           tab[i], tab[curseur] = tab[curseur], tab[i]
           curseur += 1 
    tab[curseur], tab[fin -1] = tab[fin -1], tab[curseur]
    return curseur




#tri
def tri(tab, debut, fin):
     if debut < fin:
            pivot_index = tri_rapide(tab, debut, fin)
            tri(tab , debut, pivot_index)
            tri(tab , pivot_index + 1, fin)




#test
tab =[4,8,2,10,1,9,7,6,3,5]
print (f'tableau original : ', tab)
tri(tab, 0, len(tab))
print (f'tableau trié : ', tab)
