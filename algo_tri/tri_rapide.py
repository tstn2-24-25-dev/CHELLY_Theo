#fonction tri
def tri(tab, debut, fin):
    pivot = tab[fin -1]
    curseur = debut

    for i in range(debut, fin -1):
        if tab[i] <= pivot:
           tab[i], tab[curseur] = tab[curseur], tab[i]
           curseur += 1 
    tab[curseur], tab[fin -1] = tab[fin -1], tab[curseur]
    return curseur




#tri
def triRapide(tab, debut, fin):
     if debut < fin:
            pivot_index = tri(tab, debut, fin)
            triRapide(tab , debut, pivot_index)
            triRapide(tab , pivot_index + 1, fin)




#test
tab =[4,8,2,10,1,9,7,6,3,5]
print (f'tableau original : ', tab)
triRapide(tab, 0, len(tab))
print (f'tableau trié : ', tab)
