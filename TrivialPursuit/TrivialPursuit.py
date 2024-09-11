import random
#Entree
# une série de ligne contenant chacune un chiffre compris entre 1 et 6
with open('TrivialPursuit/serie.txt', 'r') as fichier:
    serie = fichier.readlines()
#la liste des couleurs avec la position initial
couleurs = ["orange", "jaune", "vert", "rose", "bleu", "violet"]
position = 0
#calcul de la position en fonction des lancés dans le fichier txt
for lancer in serie:
    position = (position + int(lancer.strip())) % 48
    couleurJoueur = couleurs[position // 8]

trivial = couleurJoueur

#Sortie
# une couleur parmi orange, jaune, vert, rose, bleu, violet.
print(couleurJoueur)