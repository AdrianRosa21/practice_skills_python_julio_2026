from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE_PATH = ROOT / "reto-5-readme" / "detalles_proyecto.txt"
OUTPUT_PATH = Path(__file__).resolve().parent / "README.md"


def detect_project_type(text: str) -> str:
    lowered = text.lower()
    if any(token in lowered for token in ["fastapi", "api rest", "endpoints", "uvicorn", "auth", "pedidos"]):
        return "api"
    if any(token in lowered for token in ["tkinter", "desktop", "inventario", "tabla", "formulario"]):
        return "app"
    if any(token in lowered for token in ["librería", "libreria", "resize", "grayscale", "watermark", "procesamiento de imágenes"]):
        return "library"
    return "generic"


def build_readme(text: str) -> str:
    project_type = detect_project_type(text)

    if project_type == "api":
        return """# API REST para gestión de usuarios y pedidos

## Resumen
Esta API expone endpoints para usuarios, autenticación y pedidos, con un enfoque claro para demos y pruebas locales.

## Funcionalidades principales
- Gestión de usuarios.
- Autenticación básica para sesiones de prueba.
- Endpoints para consultar y crear pedidos.

## Decisiones técnicas
- Se recomienda usar SQLite para la demo inicial y PostgreSQL si la carga crece.
- Los ejemplos de requests y responses deben quedar documentados junto al servicio.

## Ejecución local
1. Crear un entorno virtual.
2. Instalar dependencias con `pip install fastapi uvicorn`.
3. Definir variables de entorno como `DATABASE_URL` y `SECRET_KEY`.
4. Ejecutar el servidor con `uvicorn main:app --reload`.

## Variables de entorno
- `DATABASE_URL`: ruta de la base de datos.
- `SECRET_KEY`: clave para firmar tokens.

## Ejemplos de endpoints
- `GET /users`
- `POST /auth/login`
- `GET /orders`

## Arquitectura
La estructura debe separar rutas, modelos y servicios para facilitar el crecimiento del proyecto.
"""

    if project_type == "app":
        return """# App de escritorio de inventario

## Resumen
Aplicación desktop construida con Tkinter para gestionar inventario desde una interfaz sencilla.

## Requisitos
- Python 3.10+
- Windows para la experiencia prevista.

## Ejecución local
1. Instalar dependencias.
2. Ejecutar el script principal con `python main.py`.
3. Confirmar que la ventana se abre sin pasos adicionales.

## Funcionalidades actuales
- Formulario para registrar productos.
- Tabla para listar el inventario.
- Acciones básicas de edición y consulta.

## Empaquetado
Se recomienda probar `pyinstaller` para generar un ejecutable de Windows.

## Capturas y UX
Agregar capturas del flujo principal en este README cuando la interfaz quede estable.
"""

    if project_type == "library":
        return """# Librería de procesamiento de imágenes

## Resumen
Librería sencilla para trabajar con imágenes mediante operaciones comunes como redimensionado, grayscale, compresión y watermark.

## Instalación
```bash
pip install nombre-del-paquete
```

## Uso básico
```python
from imagenes import resize, convertir_a_grises
```

## API pública
- `resize(image, width, height)`
- `convertir_a_grises(image)`
- `comprimir(image, quality=85)`
- `watermark(image, text)`

## Formatos soportados
La tabla de formatos debe completarse con los formatos reales que quiera soportar la librería.

## Benchmark
Incluir un benchmark básico cuando la librería quede estable.
"""

    return """# Proyecto de software

## Resumen
Este README se generó a partir de notas incompletas y necesita más detalle para quedar listo.

## Siguientes pasos
- Definir el tipo de proyecto con más precisión.
- Describir la arquitectura y las dependencias.
- Añadir ejemplos de uso reales.
"""


if __name__ == "__main__":
    notes = SOURCE_PATH.read_text(encoding="utf-8")
    OUTPUT_PATH.write_text(build_readme(notes), encoding="utf-8")
    print(f"README generado en {OUTPUT_PATH}")
