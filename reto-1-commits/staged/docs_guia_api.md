# Guia de API de Facturacion

## Endpoints disponibles

| Metodo | Ruta | Descripcion |
| --- | --- | --- |
| GET | `/api/v1/facturas` | Lista facturas del usuario autenticado |
| POST | `/api/v1/facturas` | Crea una nueva factura |
| GET | `/api/v1/iva/categorias` | Devuelve categorias fiscales soportadas |

## Autenticacion

Todas las rutas requieren token Bearer en el header `Authorization`.

## Ejemplo de request

```bash
curl -H "Authorization: Bearer <token>" http://localhost:8000/api/v1/facturas
```
