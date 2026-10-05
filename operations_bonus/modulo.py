def moduloer(nombre1: int,nombre2:int) -> int:
    """Donne le reste d'une division entière.

    Utilise l'opérateur modulo (`%`) pour calculer le reste
    de la division de deux nombres.

    Args:
        nombre1 (int): Le nombre à diviser.
        nombre2 (int): Le diviseur de l'opération.

    Returns:
        int: Le reste de la division de nombre1 par nombre2

    Raises:
        ValueError: En cas de division par 0
    """

    if nombre1 == 0:
        raise ValueError("Division par zéro impossible")

    return nombre1 % nombre2
