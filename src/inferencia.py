import os
from src.ocr_pipeline import run_ocr

def main():
    # Ruta de la imagen de prueba
    image_path = "images/test_image.png"

    if not os.path.exists(image_path):
        print("⚠ No se encontró la imagen en la carpeta images.")
        return

    # Ejecutar OCR
    text = run_ocr(image_path)

    # Crear carpeta results si no existe
    os.makedirs("results", exist_ok=True)

    # Guardar resultado en archivo
    output_path = "results/output.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    print("✅ Texto extraído correctamente.")
    print("\n--- TEXTO DETECTADO ---\n")
    print(text)
    print(f"\n📁 Resultado guardado en: {output_path}")

if __name__ == "__main__":
    main()

