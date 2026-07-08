# Generador de docstrings para Python

Esta carpeta contiene una propuesta de solución para el reto 4.

## Qué hace

- Lee [reto-4-docstring/funciones_analisis.py](../../reto-4-docstring/funciones_analisis.py).
- Analiza cada función con `ast`.
- Inserta un docstring estilo Google con secciones solo cuando corresponden.

## Archivos

- [generar_docstrings.py](generar_docstrings.py): script que genera el resultado.
- [funciones_analisis_docstring.py](funciones_analisis_docstring.py): versión con los docstrings aplicados.

## Justificación de secciones

- `funcion_a`: incluye `Args` y `Returns` porque recibe parámetros y devuelve un valor.
- `funcion_b`: incluye `Returns` porque devuelve una cadena, pero no `Args` porque no recibe ninguno.
- `funcion_c`: incluye `Args` y un bloque `Note` porque tiene efectos laterales y no devuelve nada.
- `funcion_d`: incluye `Args` con `*args` y `**kwargs`, además de `Returns` porque arma un `dict`.
