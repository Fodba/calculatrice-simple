#### Script principal de Calculatrice-simple


import affichage


# Affiche l'en-tête calculatrice.
affichage.ouverture()


# Boucle les opérations tant que la fonction ne quitte pas avec un return False.
while affichage.affichage_calcul_terminal():
    continue


# Affiche la clôture de la calculatrice
affichage.fermeture()