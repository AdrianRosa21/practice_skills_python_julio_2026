# Ejercicio: traductor-nombres

## Contexto de práctica

Este reto está diseñado para construir una skill de VS Code llamada **`traductor-nombres`**.
La skill debe normalizar nombres entre estilos comunes sin depender de que el usuario declare el formato origen.

## Entrada de prueba fija

- `reto-2-nombres/desastre_variables.py`

> No modifiques este archivo como parte del ejercicio. Es la entrada fija de evaluación.

## Qué debe hacer la skill

1. Detectar automáticamente el formato de entrada por identificador.
2. Convertir entre:
   - `camelCase`
   - `snake_case`
   - `kebab-case`
   - `PascalCase`
3. Proponer una normalización consistente para un archivo con estilos mezclados.

## Casos borde obligatorios

- Siglas técnicas (por ejemplo, API, REST, JSON) en diferentes posiciones.
- Identificadores con números intercalados.
- Variables de un solo carácter (por ejemplo, `x`) con baja semántica.
- Entradas ambiguas donde no es obvio si una sigla debe preservarse en mayúsculas.

## Entregable esperado de la skill

- Mapeo claro: nombre original -> nombre propuesto.
- Regla de normalización elegida y aplicada de forma uniforme.
- Tratamiento explícito para siglas, números y casos ambiguos.
