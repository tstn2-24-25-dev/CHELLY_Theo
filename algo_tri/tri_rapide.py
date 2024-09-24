# fonction tri
def triPivot(tab, debut, fin):
    pivot = tab[fin - 1]
    curseur = debut

    for i in range(debut, fin - 1):
        if tab[i] <= pivot:
            tab[i], tab[curseur] = tab[curseur], tab[i]
            curseur += 1
    tab[curseur], tab[fin - 1] = tab[fin - 1], tab[curseur]
    return curseur


# fonction triRapide avec indices
def triRapide_interne(tab, debut, fin):
    if debut < fin:
        pivot_index = triPivot(tab, debut, fin)
        triRapide_interne(tab, debut, pivot_index)
        triRapide_interne(tab, pivot_index + 1, fin)


# triRapide sans indices
def triRapid(tab):
    triRapide_interne(tab, 0, len(tab))
    return tab


# test
tab = [4, 8, 2, 10, 1, 9, 7, 6, 3, 5]
print(f'Tableau original : {tab}')
triRapide(tab)
print(f'Tableau trié : {tab}')
