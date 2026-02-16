# OCR Pipeline
import easyocr
import numpy as np

# Nativas python
import json
from datetime import datetime


class OCRJob():
    '''
        Clase para realizar OCR en una imagen utilizando EasyOCR y guardar los resultados en archivos de texto y JSON.

        Atributos:
        - image_path: Ruta de la imagen a procesar.
        - output_path: Ruta del directorio donde se guardarán los archivos de salida.
        - image_name: Nombre del archivo de imagen (opcional).

        Metodos:
        - OCR_image: Realiza OCR en la imagen y almacena el texto reconocido y las probabilidades de confianza.
        - save_results: Guarda los resultados del OCR en archivos de texto y JSON.
        - excetute: Ejecuta el proceso completo de OCR y guardado de resultados.
    '''

    def __init__(self
                 , image_path : str , output_path : str = None
                 ,image_name : str = None, language : str = 'en') -> None:

        self.language = language

        self.text = None
        self.probs = None

        self.image_name = image_name
        self.output_path = output_path

        if not image_name is None:
            self.image_path = f'{image_path}/{image_name}'
        else:
            self.image_path = image_path
        try :   
            self.reader = easyocr.Reader([self.language]) 
        except Exception as e:
            print(f"Error al cargar el modelo de OCR. Verifique que el idioma sea correcto y que el modelo esté disponible. Error: {e}")

    def OCR_image(self)  -> None:

        '''
        Funcion para realizar OCR en una imagen utilizando EasyOCR.
        Parametros:
        - image_path: Ruta de la imagen a procesar.
        - language: Idioma del modelo de OCR a utilizar (por defecto 'en').

        Retorna:
        - text: Texto reconocido en la imagen.
        - results: Array con el texto reconocido y su probabilidad de confianza.    
        '''
        
        try:
            result = self.reader.readtext(self.image_path)
        except Exception as e:
            print(f"Error al leer la imagen. Error: {e}")
            return None, None
        
        # Procesar resultados
        results = np.array([])
        for (bbox, text, prob) in result:
            results = np.append(results, np.array([text, prob]))
        results = results.reshape(-1, 2)
        text = " ".join(results[:,0])
        
        self.text = text
        self.probs = results
        print(f"Texto reconocido: {self.text}")

    def save_results(self)  -> None:

        '''
        Funcion para guardar los resultados del OCR en archivos de texto y JSON.
        
        Parametros:
        - text: Texto reconocido en la imagen.
        - probs: Array con el texto reconocido y su probabilidad de confianza.
        - file_name: Nombre del archivo de entrada (sin extensión).
        - output_path: Ruta del directorio donde se guardarán los archivos de salida.
        
        Retorna:
        - None
        '''

        current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if self.image_name is None:
            results_name = "inference_results"
        else:
            results_name = self.image_name.split('.')[0]

        if self.output_path is None:
            self.output_path = './'
        # Rutas de salida para los archivos de texto y JSON
        txt_path = f'{self.output_path}/{results_name}_{current_datetime}.txt'
        json_path = f'{self.output_path}/{results_name}_{current_datetime}.json'

        # Guardar resultados en archivos de texto y JSON
        try:
            with open(txt_path, 'w') as f:
                f.write(f"Texto reconocido: {self.text}\n")
            with open(json_path, 'w') as f:
                json.dump(self.probs.tolist(), f, indent = 4)
            print(f"Resultados guardados en: {txt_path} y {json_path}")
        except Exception as e:
            print(f"Error al guardar los resultados. Verifique que la ruta de salida sea correcta y que tenga permisos de escritura. Error: {e}")

    def excetute(self) -> None:
        self.OCR_image()
        self.save_results()