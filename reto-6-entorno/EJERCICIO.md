# Ejercicio: creador-entorno-python

## Contexto de práctica

Este reto está diseñado para construir una skill de VS Code llamada **`creador-entorno-python`**.
La skill debe detectar dependencias reales de un script y ayudar a preparar el entorno.

## Entrada de prueba fija

- `reto-6-entorno/script_complejo.py`

> No modifiques este archivo como parte del ejercicio. Es la entrada fija de evaluación.

## Qué debe hacer la skill

1. Analizar imports `import ...` y `from ... import ...`.
2. Diferenciar librería estándar de dependencias externas.
3. Generar:
   - `requirements.txt`, o
   - comandos para crear/activar `venv` e instalar dependencias.
4. Resolver correctamente casos donde nombre de import != nombre de paquete.

## Casos borde obligatorios

- No incluir módulos de librería estándar en `requirements.txt`.
- Resolver mapeos no triviales, por ejemplo:
  - `cv2` -> `opencv-python`
  - `yaml` -> `pyyaml`
  - `from PIL import Image` -> `Pillow`
- Mantener salida reproducible y clara para instalación.

## Entregable esperado de la skill

- Lista final de dependencias externas sin ruido.
- Mapeo explícito para imports con nombre de paquete distinto.
- Instrucciones mínimas de entorno (venv) cuando aplique.
