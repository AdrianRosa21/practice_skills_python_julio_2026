"""Script con imports mezclados para practicar generación de requirements."""

import math
import os
import sys
from datetime import datetime

import cv2
import pandas as pd
import requests
import yaml
from dotenv import load_dotenv
from PIL import Image


def ejecutar_pipeline(ruta_imagen: str, endpoint: str) -> dict:
    load_dotenv()
    img = Image.open(ruta_imagen)
    ancho, alto = img.size

    escala = math.sqrt((ancho * alto) / 1000.0)
    miniatura = cv2.resize(cv2.imread(ruta_imagen), (128, 128))
    _ = miniatura

    payload = {
        "archivo": os.path.basename(ruta_imagen),
        "pixeles": ancho * alto,
        "escala": round(escala, 3),
        "ejecutado_en": datetime.utcnow().isoformat(),
        "python": sys.version.split()[0],
    }

    serializado = yaml.safe_dump(payload)
    tabla = pd.DataFrame([payload])
    _ = tabla

    respuesta = requests.post(endpoint, data=serializado, timeout=5)
    return {"status_code": respuesta.status_code, "payload": payload}
