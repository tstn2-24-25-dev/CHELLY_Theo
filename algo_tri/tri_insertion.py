#fonction tri
def tri_insertion(tab):
    for i in range(1, len(tab)):
 #stocker l'élément à insérer
        element_a_inserer = tab[i]
        k = i - 1
        while k >= 0 and tab[k] > element_a_inserer:
#insérer l'élément à la ponne position
            tab[k + 1] = tab[k]  
            k -= 1
        tab[k + 1] = element_a_inserer
    return tab  
    
if __name__ == "__main__":
    print("tableau original: ")
    tab = [4,8,2,10,1,9,7,6,3,5]
    print ((tab))
    print("tableau trié :")
    print(tri_insertion(tab))