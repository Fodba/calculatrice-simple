#### Module d'affichage


import operations_base.addition       as oaddi
import operations_base.soustraction   as osous
import operations_base.multiplication as omult
import operations_base.division       as odivi
import operations_bonus.modulo        as omodu



## Fonction de demande de saisie
def demande_de_saisie(le_type:type[int|float|str], texte:str=''):
    """
    Demande une saisie jusqu'à ce que le type corresponde avec celui choisi, puis renvoit la saisie.

    Args:
        le_type (`type[int|float|str]`) : Type vers lequel sera converti la saisie utilisateur.
        texte (`str`) : Texte affiché au moment de la saisie [optionnel]
    
    Returns:
        `int`|`float`|`str` : Saisie de l'utilisateur converti au type défini.
    """
    while True:

        la_saisie = input(f"{texte}").strip()

        try:
            if le_type in (int, float, str):
                le_retour = le_type(la_saisie)
                break
            else:
                continue

        except Exception:
            print("Valeur invalide saisie, essayez à nouveau.")
            continue

    return le_retour
            

def demande_deux_nombres(le_type:type[int|float]):
    """
    Demande la saisie de deux nombres un par un.
    
    Args:
        le_type (`type[int|float]`) : le type de la saisie demandé.

    Returns:
        `tuple[int|float, int|float]` : Tuple contenant les deux nombres saisies
    """
    print("Saisir un premier nombre : ")
    nombre_1 = demande_de_saisie(le_type, "Saisir un premier nombre : ")
    print("Saisir un deuxième nombre : ")
    nombre_2 = demande_de_saisie(le_type, "Saisir un deuxième nombre : ")

    return tuple(nombre_1, nombre_2)


## Fonction d'affichage des choix et résultat du calcul dans le terminal
def affichage_calcul_terminal():
    """
    Propose des opérations mathématiques, calcule le résultat d'après deux nombres rentrés, puis affiche le résultat.

    Returns:
        `bool`
    """
    print( "-"*50
    +"Quelle opération mathématique effectuer ?\n"
    +"\n"
    +"  A  ->  Addition\n"
    +"  S  ->  Soustraction\n"
    +"  M  ->  Multiplication\n"
    +"  D  ->  Division\n"
    +"\n"
    +"  Q  ->  Quitter\n"
    +"\n"
    )

    # Boucle les opération jusqu'à ce que l'option Quitter soit choisie.
    while True:
        choix = demande_de_saisie(str, "Choisir une opération : ").upper

        # On récupère un tuple
        nombres = demande_deux_nombres()

        try:
            if choix == 'A' :
                resultat = oaddi.additionner( *nombres )
                contexte = ("la somme", "+")
                print("'[ Addition ]' ")
                break

            elif choix == 'S' :
                resultat = osous.soustraire( *nombres )
                contexte = ("la différence", "-")
                print("'[ Soustraction ]' ")
                break

            elif choix == 'M' :
                resultat = omult.multiplier( *nombres )
                contexte = ("la multiplication", "*")
                print("'[ Multiplication ]' ")
                break

            elif choix == 'D' :
                resultat = odivi.diviser( *nombres )
                contexte = ("la division", "/")
                print("'[ Division ]' ")
                break

            elif choix == 'R' :
                resultat = omodu.moduloer( *nombres )
                contexte = ("la division", "/")
                print("'[ Division ]' ")
                break

            elif choix == 'Q' :
                print("\nFermeture de la calculatrice.")
                return False

            else:
                print(f"Aucune opération sur \"{choix}\", essayez à nouveau.")
                continue

        except Exception as erreur:
            print(f"\n{erreur}. Essayez à nouveau.")


    print(f"\n  Le résultat de {contexte[0]} {nombres[0]} {contexte[1]} {nombres[1]} est de {resultat}")


    return True


