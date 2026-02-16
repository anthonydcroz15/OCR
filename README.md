# Proyecto OCR – Extracción Automática de Texto desde Imágenes

# 1.Descripción general del proyecto

Este proyecto implementa un sistema de Reconocimiento Óptico de Caracteres (OCR) capaz de extraer texto desde imágenes digitales utilizando técnicas de preprocesamiento y modelos de visión por computadora.

El sistema sigue una arquitectura modular que incluye:


1. Aplicación de un modelo OCR para reconocimiento de texto.

2. Generación de archivo de salida con el texto detectado.

Las imágenes utilizadas para pruebas fueron obtenidas de la plataforma Kaggle, reconocida internacionalmente por alojar datasets para proyectos de ciencia de datos y aprendizaje automático.

El modelo está diseñado para funcionar con texto digital impreso o generado por computadora, no para reconocimiento de escritura manuscrita.

# 2.Requisitos del sistema

# Software requerido:

1. Python 3.10 o superior

2. Git (para clonar el repositorio)

3. Sistema operativo: Windows, macOS o Linux

# Librerías necesarias

1. easyocr

2. numpy

# 3.Instrucciones de instalación
1. Clonar el repositorio
git clone <URL_DEL_REPOSITORIO>
cd OCR

2. Crear entorno virtual
python -m venv .venv

3. Activar entorno virtual

En Windows:

.venv\Scripts\activate


En macOS / Linux:

source .venv/bin/activate

4. Instalar dependencias
pip install easyocr -python numpy

# 4. Descripción de la estructura del repositorio
OCR/
│
├── images/              # Imágenes de entrada para OCR
├── results/             # Resultados generados por el sistema
├── src/
│   ├── utils.py         # Funciones auxiliares y preprocesamiento
│   ├── ocr_pipeline.py  # Implementación del pipeline OCR
│   └── inferencia.py    # Script principal de ejecución
│
├── .gitignore
└── README.md

# Descripción de archivos principales

utils.py contiene el inicio de la mejora que queremos hacer.

ocr_pipeline.py: ejecuta el flujo completo del sistema OCR.

inferencia.py: script principal que permite ejecutar el sistema y generar resultados (texto y la probabilidad)

# 5. Instrucciones de uso del script de inferencia

Colocar una imagen con texto dentro de la carpeta:

images/


Verificar o modificar en src/inferencia.py la ruta de la imagen:

image_path = "images/test_image.png"


Ejecutar el script desde la raíz del proyecto:

python src/inferencia.py


El sistema imprimirá el texto detectado en consola y generará un archivo con el resultado en:

results/output.txt

# 6. Ejemplo de entrada y salida
# Ejemplo de entrada

Archivo:

images/test_image.png


Contenido visual aproximado de la imagen:

Hola mundo
Este es un ejemplo OCR

# Ejemplo de salida (results/output.txt)
Hola mundo
Este es un ejemplo OCR


El texto también se muestra en la terminal tras ejecutar el script.

# 7. Limitaciones y posibles mejoras
# Limitaciones actuales

1. El modelo funciona correctamente con texto digital impreso.

2. No está optimizado para reconocimiento de texto manuscrito (a mano alzada).

3. El rendimiento depende de la calidad y resolución de la imagen.

4. No se implementan métricas automáticas de evaluación de precisión.

5. Puede disminuir la exactitud en imágenes con ruido, baja iluminación o distorsión.

# Posibles mejoras

1. Implementar modelos especializados en reconocimiento de escritura manuscrita.

2. Incorporar métricas como CER (Character Error Rate).

3. Integrar corrección ortográfica automática.

4. Implementar procesamiento por lotes.

5. Incorporar aceleración por GPU.

6. Desarrollar una interfaz gráfica o versión web.