def pedir_contenido() -> str:
    """Solicita y valida el contenido del código QR.

    Returns:
        str: El texto o la URL ingresados por el usuario.

    Raises:
        ValueError: Si el contenido está vacío.
        EOFError: Si se interrumpe la entrada de datos.
        KeyboardInterrupt: Si el usuario cancela la ejecución.
    """
    contenido = input(
        "Ingresá un texto o una URL: "
    ).strip()

    if not contenido:
        raise ValueError("El texto no puede estar vacío.")

    return contenido
