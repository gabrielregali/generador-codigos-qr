from pathlib import Path


def pedir_nombre_archivo() -> str:
    """Solicita y valida el nombre del archivo de salida."""
    nombre_archivo = input(
        "Ingresá el nombre del archivo (ejemplo: mi_qr.png): "
    ).strip()

    if not nombre_archivo:
        raise ValueError("El nombre no puede estar vacío.")

    ruta = Path(nombre_archivo)

    if ruta.suffix.lower() != ".png":
        raise ValueError("El archivo debe tener la extensión .png.")

    return nombre_archivo