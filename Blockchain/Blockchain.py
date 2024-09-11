with open('Blockchain/input1.txt', 'r') as fichier:
    # un entier P correspondant au nombre de personnes stockant le livre
    P = int(fichier.readline().strip())

    # un entier N correspondant au nombre de demandes d'écriture
    N = int(fichier.readline().strip())

    livre = ""

    for _ in range(N):
        ligne = fichier.readline().strip().split()
    #  une lettre de l’alphabet C et un entier Q séparés par un espace où C est la demande d’écriture et Q le nombre de personne ayant validé cette demande.
        C, Q = ligne[0], int(ligne[1])
        
        if Q > P // 2:
            livre += C

# Sortie
print(livre)