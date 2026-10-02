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
