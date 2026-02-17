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
```text
OCR/
│
├── .venv/               # Entorno virtual del proyecto (no se versiona)
├── examples/            # Ejemplos adicionales o pruebas del sistema
├── images/              # Imágenes de entrada para el OCR
├── results/             # Archivos generados con los resultados del OCR
│
├── src/
│   ├── inferencia.py    # Script principal para ejecutar el sistema
│   ├── ocr_pipeline.py  # Implementación del pipeline OCR
│   └── utils.py         # Funciones auxiliares y preprocesamiento
│
├── .gitignore           # Archivos y carpetas excluidos del control de versiones
├── README.md            # Documentación del proyecto
└── requirements.txt     # Lista de dependencias del proyecto
```

# Descripción de archivos principales

1. .venv/: entorno virtual local donde se instalan las dependencias del proyecto. No debe subirse al repositorio.

2. examples/: carpeta destinada a pruebas o ejemplos adicionales del sistema.

3. images/: contiene las imágenes utilizadas como entrada para el proceso OCR.

4. results/: almacena los archivos de salida generados por el sistema (por ejemplo, output.txt).

5. src/: contiene el código fuente del proyecto.

6. utils.py: funciones de preprocesamiento de imágenes.

7. ocr_pipeline.py: implementación del flujo principal del OCR.

8. inferencia.py: punto de entrada para ejecutar el sistema completo.

9. requirements.txt: archivo que permite instalar todas las dependencias del proyecto mediante pip install -r requirements.txt.

# 5. Instrucciones de uso del script de inferencia

1. Colocar una imagen con texto dentro de la carpeta:

images/


2. Verificar o modificar en src/inferencia.py la ruta de la imagen:

image_path = "images/test_image.png"


3. Ejecutar el script desde la raíz del proyecto:

python src/inferencia.py


4. El sistema imprimirá el texto detectado en consola y generará un archivo con el resultado en:

results/output.txt

# 6. Ejemplo de entrada y salida
# Ejemplo de entrada

Archivo:

(examples/inputs/j04-080.png)

![Ejemplo de entrada OCR](examples/inputs/j04-080.png)

Contenido visual aproximado de la imagen:

"Sentence a Database

During the first few hours the curve will be distorted if activity other than bismuth-210 is present. These bismuth niclides may include: together with their lead parents. All but lead-212 will decay completely within six hours. The decay of lead-212 will distort the pbserved activity for four and a half days if it is present."

# Ejemplo de salida (results/output.txt)
```text
Texto reconocido: Sentence Database J04-080 During the first few hours the curve will be distorted if activity other than bismuth- 210 is present. These bismuth nuclides may include: together with their lead parents_ All but lead-212 will decay completely within six hours. The decay of lead-212 will distort the observed activity for four and a half if it is present.
```
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