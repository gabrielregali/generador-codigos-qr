
# Generador de Códigos QR

## AUTORES

### **Lucas Ariel Holës**

### **Kevin Alejandro Medina**

### **Luciano Oscar Morales**

### **Gabriel Alfredo Regali**

## Descripción

Este proyecto es una aplicación de consola desarrollada en Python que permite generar códigos QR a partir de un texto o una dirección URL.

El usuario puede ingresar el contenido que desea codificar, elegir el nombre del archivo de salida y seleccionar el color del código QR.

La imagen generada se guarda en formato PNG y el programa informa dónde quedó almacenada.

## Funcionalidades

- Solicitar un texto o una URL.
- Solicitar y validar el nombre del archivo de salida.
- Elegir el color del código QR.
- Generar y guardar la imagen en formato PNG.
- Informar la ubicación del archivo generado.
- Manejar errores relacionados con los datos ingresados y el guardado de archivos.

## Tecnologías utilizadas

- Python 3
- qrcode
- Pillow
- pathlib
- venv

## Estructura del proyecto

```text
generador_qr/
├── main.py
├── pedir_contenido.py
├── pedir_nombre_archivo.py
├── pedir_color.py
├── generar_qr.py
├── requirements.txt
├── README.md
└── .venv/
```

La carpeta `.venv/` corresponde al entorno virtual local y no es necesario incluirla en el repositorio de GitHub.

## Requisitos previos

- Tener Python 3 instalado.
- Tener pip disponible.
- Contar con una terminal, como la terminal integrada de Visual Studio Code.

## Instalación

### 1. Clonar o descargar el proyecto

Si el proyecto está publicado en GitHub, clonar el repositorio y entrar en su carpeta:

```bash
git clone URL_DEL_REPOSITORIO
cd generador_qr
```

Si ya se tiene el proyecto descargado, abrir una terminal dentro de la carpeta.

### 2. Crear el entorno virtual

```bash
python -m venv .venv
```

El entorno virtual permite instalar las dependencias del proyecto de forma aislada.

### 3. Activar el entorno virtual

En Windows, utilizando PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

En Windows, utilizando el símbolo del sistema (CMD):

```bat
.venv\Scripts\activate.bat
```

En Linux o macOS:

```bash
source .venv/bin/activate
```

### 4. Instalar las dependencias

Con el entorno virtual activado, ejecutar:

```bash
python -m pip install -r requirements.txt
```

Este comando instala las librerías necesarias para ejecutar el proyecto.

## Ejecución

Desde la carpeta principal del proyecto, ejecutar:

```bash
python main.py
```

El programa solicitará:

1. El texto o la URL que se desea codificar.
2. El nombre del archivo de salida, con extensión `.png`.
3. El color del código QR.

Colores disponibles:

- `black`
- `blue`
- `red`
- `green`
- `purple`

Al finalizar, se mostrará un mensaje indicando que el código QR se generó correctamente y se informará la ubicación del archivo.

## Manejo de errores

El programa utiliza excepciones para contemplar situaciones como:

- Ingreso de texto vacío.
- Nombre de archivo inválido.
- Extensión de archivo no admitida.
- Selección de un color no permitido.
- Errores de acceso o guardado del archivo.
- Interrupción de la ejecución.



