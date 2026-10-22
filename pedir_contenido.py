def pedir_contenido() -> str:
    """Solicita el texto que se guardará en el código QR."""
    contenido = input("Ingresá un texto o una URL: ").strip()

    if not contenido:
        raise ValueError("El texto no puede estar vacío.")

    return contenido