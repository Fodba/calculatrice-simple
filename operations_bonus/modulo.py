def moduloer(nombre: int) -> bool:
    """Vérifie si un nombre entier est pair.

    Utilise l'opérateur modulo (`%`) pour déterminer si le reste
    de la division par 2 est égal à zéro.

    Args:
        nombre (int): Le nombre entier à tester.

    Returns:
        bool: True si le nombre est pair, False s'il est impair.

    Raises:
        ValueError: En cas de division
    """
    if nombre == 0:
        raise ValueError("Division par zéro impossible")

    return nombre % 2 == 0
