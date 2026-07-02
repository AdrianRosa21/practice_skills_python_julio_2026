# Ejercicio: generador-commits

## Contexto de práctica

Este reto está diseñado para construir una skill de VS Code llamada **`generador-commits`**.
La skill debe analizar cambios y proponer mensajes de commit con formato **Conventional Commits**.

## Entrada de prueba fija

- `reto-1-commits/cambios_mezclados.py`

> No modifiques este archivo como parte del ejercicio. Es la entrada fija de evaluación.

## Qué debe hacer la skill

1. Leer los cambios descritos (o detectados en diff).
2. Proponer un mensaje de commit en formato Conventional Commits.
3. Distinguir correctamente entre: `feat`, `fix`, `refactor`, `docs`, `chore`.
4. Si detecta dos cambios no relacionados en una sola propuesta, **debe advertir/rechazar** en vez de generar un único commit genérico.

## Casos borde obligatorios

- Cambio mixto `feat + fix` en el mismo archivo (caso principal de este reto).
- Cambio puramente documental (`docs`) sin lógica de código.
- Cambio técnico de mantenimiento (`chore`) sin impacto funcional.
- Cambio de reordenamiento interno (`refactor`) sin alterar comportamiento observable.

## Entregable esperado de la skill

- Mensaje(s) de commit propuestos con estructura Conventional Commits.
- Justificación breve del tipo elegido.
- Advertencia explícita cuando haya mezcla de cambios no relacionados.
