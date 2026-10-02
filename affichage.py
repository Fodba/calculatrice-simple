#### Module d'affichage


import operations_base.addition       as oaddi
import operations_base.soustraction   as osous
import operations_base.multiplication as omult
import operations_base.division       as odivi
import operations_bonus.modulo        as omodu


def ouverture():
    """
    Affiche l'en-tête de la calculatrice.
    """
    print(
        f"{"\n"*10}"
        f"+{"-"*34}+\n"
        f"|{"C A L C U L A T R I C E":^34}|\n"
        f"+{"-"*34}+\n"
    )


def fermeture():
    """
    Affiche la clôture du script.
    """
    print(
         "\n"
        f"+{"-"*34}+\n"
        f"|{"Fermeture de la calculatrice":^34}|\n"
        f"+{"-"*34}+\n"
    )


def continuer_ou_quitter(question:str):
    """
    Retourne True ou False suivant le choix utilisateur de continuer ou non, demande à nouveau sur mauvaise saisie.

    Args:
        question (`str`) : Question posé sur le choix 

    Returns:
        return (`bool`) : 
    """
    # Boucle infinie jusqu'à sorti de la fonction
    while 1:
        match demande_de_saisie(str, f"{question}  [O]ui  ou  [N]on  : ").upper():
            case "O"|"OUI"|"Y"|"YES" : return True
            case "N"|"NON"|"NO"      : return False
            case _                   : continue


## Fonction de demande de saisie
def demande_de_saisie(le_type:type[int|float|str], texte:str=''):
    """
    Demande une saisie jusqu'à ce que le type corresponde avec celui choisi, puis renvoit la saisie typée au besoin.\n
    Les types acceptés sont : nombre entier, nombre décimal, ou chaîne de caractères.\n

    Args:
        le_type (`type[int|float|str]`) : Type vers lequel sera converti la saisie utilisateur.
        texte (`str`) : Texte affiché au moment de la saisie [optionnel]
    
    Returns:
        `int`|`float`|`str` : Saisie de l'utilisateur converti au type défini.
    """
    # Bouclage jusqu'à retour d'une saisie valide
    while True:

        la_saisie = input(f"{texte}").strip()

        try:
            match le_type:
                 
                # Si le type demandé est un nombre, remplace la virgule française en point et supprime les espaces diviseurs de milliers.
                case t if t in (int, float) :
                    le_retour = le_type(la_saisie.replace(',','.').replace(' ',''))

                    # Renvoie quand même comme un nombre entier si c'en est un.
                    if le_type is float and le_retour %1==0:
                        le_retour = int(le_retour)

                    break
                
                # Ne rien changer pour un type chaine de caractères.
                case t if t is str :
                    le_retour = la_saisie
                    break
                
                # Pour tout autre type demandé (incompatible), considère comme type chaine de caractères.
                case _:
                    le_retour = la_saisie
                    break

        # Si un erreur survient, demande une nouvelle saisie.
        except Exception:
            print("Valeur invalide saisie, essayer à nouveau.\n")
            continue

    # On retourne une valeur correct et typé.
    return le_retour
            

## Fonction de demande de deux nombres.
def demande_deux_nombres(le_type:type[int|float]):
    """
    Demande la saisie de deux nombres un par un.
    
    Args:
        le_type (`type[int|float]`) : le type de la saisie demandé.

    Returns:
        `list[int|float, int|float]` : Liste contenant les deux nombres saisies
    """
    nombre_1 = demande_de_saisie(le_type, "Saisir un premier nombre : ")
    nombre_2 = demande_de_saisie(le_type, "\nSaisir un deuxième nombre : ")
    
    return [nombre_1, nombre_2]


## Fonction d'affichage des choix et résultat du calcul dans le terminal
def affichage_calcul_terminal():
    """
    Propose des opérations mathématiques, calcule le résultat d'après deux nombres rentrés, puis affiche le résultat.

    Returns:
        `bool`
    """
    print("\n" + "-"*41 + "\n\n"
        "Quelle opération mathématique effectuer ?\n\n"
        "  [A]  ->  Addition       \n"
        "  [S]  ->  Soustraction   \n"
        "  [M]  ->  Multiplication \n"
        "  [D]  ->  Division       \n"
        "  [R]  ->  Modulo (Reste) \n\n"
        "  [Q]  --->  Quitter      \n"
    )

    # Boucle les opération jusqu'à ce que l'option Quitter soit choisie.
    while True:
        choix = demande_de_saisie(str, "Choisir une opération : ").upper()
        try:
            # Choix d'opération
            match choix:
                 
                case 'A' :
                        print("\n[ Addition ]\n")
                        nombres = demande_deux_nombres(float)
                        resultat = oaddi.additionner( *nombres )
                        contexte = ("de la somme", "+")
                        break

                case 'S' :
                        print("\n[ Soustraction ]\n")
                        nombres = demande_deux_nombres(float)   # On récupère une liste, modifiable
                        resultat = osous.soustraire( *nombres )
                        contexte = ("de la soustraction", "-")
                        if nombres[1] < 0 : nombres[1] = f"( {nombres[1]} )"  # Parenthèses pour l'affichage de la soustraction par un négatif
                        break

                case 'M' :
                        print("\n[ Multiplication ]\n")
                        nombres = demande_deux_nombres(float)
                        resultat = omult.multiplier( *nombres )
                        contexte = ("de la multiplication", "*")
                        break

                case 'D' :
                        print("\n[ Division ]\n")
                        nombres = demande_deux_nombres(float)
                        resultat = odivi.diviser( *nombres )
                        contexte = ("de la division", "/")
                        break

                case 'R' :
                        print("\n[ Modulo ]\n")
                        nombres = demande_deux_nombres(float)
                        resultat = omodu.moduloer( *nombres )
                        contexte = ("du modulo de", "//")
                        break

                case 'Q' :
                        # Fermeture calculatrice
                        return False

                case _:
                        print(f"Aucune opération sur \"{choix}\", essayer à nouveau.\n")
                        continue

        except Exception as erreur:
            print(f"\n{erreur}. Essayer à nouveau.")


    print(f"\n  Le résultat {contexte[0]}  ( {nombres[0]} {contexte[1]} {nombres[1]} )  est :   {round(resultat,10)}")
    print("\n" + "-"*41 + "\n")


    # Demande pour relancer une opération.
    return continuer_ou_quitter("Faire une nouvelle opération ?")

