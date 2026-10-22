from pathlib import Path

import qrcode


def generar_qr(
    contenido: str,
    nombre_archivo: str,
    color: str
) -> None:
    """Genera el código QR con el color elegido y guarda la imagen."""
    codigo_qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )

    codigo_qr.add_data(contenido)
    codigo_qr.make(fit=True)

    imagen_qr = codigo_qr.make_image(
        fill_color=color,
        back_color="white",
    )

    ruta = Path(nombre_archivo)
    imagen_qr.save(ruta)

    print("¡Código QR generado correctamente!")
    print(f"Ruta del archivo: {ruta.resolve()}")