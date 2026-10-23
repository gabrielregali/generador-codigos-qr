from pathlib import Path


def pedir_nombre_archivo() -> str:
    """Solicita y valida el nombre del archivo de salida.

    Returns:
        str: El nombre válido del archivo PNG.

    Raises:
        ValueError: Si el nombre está vacío, contiene caracteres
            no permitidos o no tiene la extensión .png.
        EOFError: Si se interrumpe la entrada de datos.
        KeyboardInterrupt: Si el usuario cancela la ejecución.
    """
    nombre_archivo = input(
        "Ingresá el nombre del archivo (ejemplo: mi_qr.png): "
    ).strip()

    if not nombre_archivo:
        raise ValueError(
            "El nombre del archivo no puede estar vacío."
        )

    caracteres_invalidos = '<>:"/\\|?*'

    if any(
        caracter in nombre_archivo
        for caracter in caracteres_invalidos
    ):
        raise ValueError(
            "El nombre contiene caracteres no permitidos."
        )

    ruta = Path(nombre_archivo)

    if ruta.suffix.lower() != ".png":
        raise ValueError(
            "El archivo debe tener la extensión .png."
        )

    return nombre_archivo
