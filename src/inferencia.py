import ocr_pipeline as ocr
import argparse

# Configuración de argumentos de entrada para la inferencia OCR
def build_argparser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="OCR inference con EasyOCR. Genera .txt y .json."
    )
    p.add_argument(
        
        "image_path",
        type=str,
        help="Ruta a la imagen (ej: ../examples/inputs/n06-092.png)",
    )
    p.add_argument(
        "--image_name",
        type=str,
        default=None,
        help = "Nombre de la imagen dentro del directorio. Si no se especifica, se asume que image_path es la ruta completa a la imagen."
    )
    p.add_argument(
        "--lang",
        type=str,
        default="en",
        help="Idioma de OCR (default: en). Ej: en, es, pt...",
    )
    p.add_argument(
        "--out",
        type=str,
        default=None,
        help=(
            "Directorio de salida. Si no se especifica, se usa la carpeta de inferencia.py."
        ),
    )
    return p

# 
def main() -> int:
    args = build_argparser().parse_args()


    job = ocr.OCRJob(
        image_path=args.image_path,
        image_name=args.image_name,
        output_path=args.out,
        language=args.lang,
    )

    job.excetute()
    return 0

main()