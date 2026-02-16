import easyocr
from src.utils import preprocess_image

# Inicializamos el lector una sola vez (buena práctica)
reader = easyocr.Reader(['es', 'en'])

def run_ocr(image_path):
    """
    Ejecuta el pipeline completo:
    1. Preprocesa la imagen
    2. Aplica OCR con EasyOCR
    3. Devuelve el texto extraído
    """

    # 1️⃣ Preprocesamiento
    processed_image = preprocess_image(image_path)

    # 2️⃣ OCR
    results = reader.readtext(processed_image)

    extracted_text = ""

    # 3️⃣ Extraer solo el texto detectado
    for (bbox, text, probability) in results:
        extracted_text += text + "\n"

    return extracted_text
