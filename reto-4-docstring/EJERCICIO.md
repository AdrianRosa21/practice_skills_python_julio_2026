# Ejercicio: generador-docstring-python

## Contexto de práctica

Este reto está diseñado para construir una skill de VS Code llamada **`generador-docstring-python`**.
La skill debe documentar funciones Python en estilo **Google** o **NumPy** (a elección del equipo).

## Entrada de prueba fija

- `reto-4-docstring/funciones_analisis.py`

> No modifiques este archivo como parte del ejercicio. Es la entrada fija de evaluación.

## Qué debe hacer la skill

1. Analizar firma y comportamiento de cada función.
2. Generar docstring estructurado y coherente.
3. Adaptar secciones según el caso real de la función.

## Casos borde obligatorios

- Si la función no recibe parámetros, no inventar sección `Args`/`Parameters`.
- Si la función no retorna valor, no inventar sección `Returns`.
- Manejo correcto de firmas no triviales con valores por defecto, `*args` y `**kwargs`.
- Redacción alineada con el comportamiento real, no con suposiciones arbitrarias.

## Entregable esperado de la skill

- Docstrings completos por función en un solo estilo consistente.
- Justificación de por qué se incluyen o excluyen secciones.
- Sin secciones vacías o inventadas.
