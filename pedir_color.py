
def pedir_color() -> str:
    """Solicita al usuario el color del código QR."""
    print("Colores disponibles: black, blue, red, green, purple")

    color = input("Elegí un color: ").strip().lower()

    colores_validos = ["black", "blue", "red", "green", "purple"]

    if color not in colores_validos:
        raise ValueError("El color ingresado no es válido.")

    return color
