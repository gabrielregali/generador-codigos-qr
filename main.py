# 📚 Ejercicio Avanzado 2: "Generador de Códigos QR"
#
# 🎯 Objetivo:
# Construir un pequeño proyecto que genere imágenes de códigos QR a partir de
# un texto o enlace, aplicando entorno virtual, librerías de terceros, manejo
# de errores y buenas prácticas de código.
#
# 📄 Enunciado:
# Desarrollá un programa de consola que:
#   1. Le pida al usuario un texto o una URL.
#   2. Le pida el nombre del archivo de salida (ej: "mi_qr.png").
#   3. Genere el código QR correspondiente.
#   4. Guarde la imagen en disco y avise al usuario la ruta donde quedó.
#   5. (Opcional) Permita elegir el color del QR.
#
# 🧩 Librerías de terceros a usar (mínimo 2, instalar con pip):
#   - qrcode       → para generar el código QR.
#   - pillow (PIL) → para manejar y guardar la imagen resultante.
#
# 🛠️ Pasos obligatorios del proyecto:
#   1. Crear una carpeta para el proyecto (ej: "generador_qr/").
#   2. Crear el entorno virtual:        python -m venv .venv
#   3. Activarlo:
#         Linux/Mac:   source .venv/bin/activate
#         Windows:     .venv\Scripts\activate
#   4. Instalar las librerías:          pip install qrcode pillow
#   5. Congelar las dependencias:       pip freeze > requirements.txt
#   6. Escribir un README.md que explique qué hace el proyecto, cómo crear
#      el entorno virtual, cómo instalar las dependencias y cómo ejecutarlo.
#
# ✅ Requerimientos técnicos:
#   - Manejar TODOS los errores posibles con try / except
#     (texto vacío, nombre de archivo inválido, error al guardar la imagen,
#     etc.).
#   - Cada función debe tener su docstring explicando qué hace.
#   - Usar anotación de tipos en parámetros y valores de retorno.
#   - Respetar PEP8 (nombres, espacios, longitud de línea, sangría).
#   - Entregar la carpeta del proyecto con: el .py, requirements.txt y
#     README.md.

from pedir_contenido import pedir_contenido
from pedir_nombre_archivo import pedir_nombre_archivo
from generar_qr import generar_qr
from pedir_color import pedir_color


def main() -> None:
    """Coordina la ejecución del generador de códigos QR."""
    print("=== GENERADOR DE CÓDIGOS QR ===")

    try:
        contenido = pedir_contenido()
        nombre_archivo = pedir_nombre_archivo()
        color = pedir_color()
        generar_qr(contenido, nombre_archivo, color)

    except ValueError as error:
        print(f"Error en los datos ingresados: {error}")

    except OSError as error:
        print(f"Error al guardar o acceder al archivo: {error}")

    except (EOFError, KeyboardInterrupt):
        print("\nEjecución cancelada por el usuario.")

    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")


if __name__ == "__main__":
    main()