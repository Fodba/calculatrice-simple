
def division(nombre1: int | float, nombre2: int | float):
    """Calcule le quotient entre deux nombres.

    Args:
        nombre1 (int | float): Le nombre de base.
        nombre2 (int | float): Le diviseur.

    Returns:
        int | float: Le quotient entre nombre1 et nombre2.

    Raises:
        ValueError: En cas de division
    """

    if nombre2 == 0:
        raise ValueError("Division par zéro impossible")

    return nombre1 / nombre2



def multiplication(nombre1: int|float, nombre2: int|float):
    """Calcule le produit entre deux nombres.

    Args:
        nombre1 (int | float): Le nombre de base.
        nombre2 (int | float): Le mutiplicateur.

    Returns:
        int | float: Le produit entre nombre1 et nombre2.
    """
    return nombre1 * nombre2

def addition(nombre1: int|float, nombre2:int|float)->int|float:
    """Permet d'additionner deux nombre

    Args:
        nombre1 (int | float): premier terme de l'addition
        nombre2 (int | float): deuxième terme de l'addition

    Returns:
        int|float: la somme de nombre1 et nombre2
    """
    return nombre1 + nombre2
  
def soustraction(nombre1: int|float, nombre2:int|float):
    """Calcule la différence entre deux nombres.

    Args:
        nombre1 (int | float): Le nombre duquel on soustrait (le minued).
        nombre2 (int | float): Le nombre à soustraire (le soustrahend).

    Returns:
        int | float: La différence entre nombre1 et nombre2.
    """
    return nombre1 - nombre2



    


