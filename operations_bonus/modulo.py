def moduloer(nombre1: int,nombre2:int) -> bool:
    """Vérifie si un nombre entier est pair.

    Utilise l'opérateur modulo (`%`) pour déterminer si le reste
    de la division par 2 est égal à zéro.

    Args:
        nombre1 (int): Le nombre entier à tester.
        nombre2 (int): Le diviseur de l'opération.

    Returns:
        bool: True si le nombre est pair, False s'il est impair.

    Raises:
        ValueError: En cas de division
    """

    if nombre1 == 0:
        raise ValueError("Division par zéro impossible")

    return nombre1 % nombre2 == 0
