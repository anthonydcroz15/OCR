import cv2


# Mejoras a futuro
def preprocess_image(image_path):
    """
    Preprocesamiento de imagen:
    - Escala de grises
    - Suavizado
    - Umbralización adaptativa
    """
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError("No se pudo cargar la imagen.")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    thresh = cv2.adaptiveThreshold(
        blurred,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    return thresh

