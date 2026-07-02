# Ejercicio: generador-datos-prueba

## Contexto de práctica

Este reto está diseñado para construir una skill de VS Code llamada **`generador-datos-prueba`**.
La skill debe producir mock data JSON válida a partir de entidades relacionales.

## Entrada de prueba fija

- `reto-3-mockdata/modelos_relacionales.py`

> No modifiques este archivo como parte del ejercicio. Es la entrada fija de evaluación.

## Qué debe hacer la skill

1. Leer la estructura de entidades (`Usuario`, `Pedido`, `Producto`).
2. Generar JSON de prueba respetando relaciones:
   - Usuario -> lista de Pedidos
   - Pedido -> lista de Productos
3. Mantener coherencia de tipos y consistencia entre IDs referenciados.

## Casos borde obligatorios

- Correos electrónicos con formato válido.
- Fechas coherentes: un pedido no puede ser anterior al nacimiento del usuario.
- Totales de pedido razonables según precios/cantidades simuladas.
- Múltiples usuarios con diferente cantidad de pedidos.

## Entregable esperado de la skill

- Archivo o bloque JSON con datos de ejemplo consistentes.
- Evidencia de validaciones de coherencia mínima (emails y fechas).
- Datos suficientemente variados para pruebas funcionales.
