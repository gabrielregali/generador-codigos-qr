def pedir_color() -> str:
    """Solicita y valida el color del código QR.

    Returns:
        str: El nombre del color seleccionado en inglés.

    Raises:
        ValueError: Si el color ingresado no está permitido.
        EOFError: Si se interrumpe la entrada de datos.
        KeyboardInterrupt: Si el usuario cancela la ejecución.
    """
    print("Colores disponibles: black, blue, red, green, purple")

    color = input("Elegí un color: ").strip().lower()

    colores_validos = ["black", "blue", "red", "green", "purple"]

    if color not in colores_validos:
        raise ValueError("El color ingresado no es válido.")

    return color
