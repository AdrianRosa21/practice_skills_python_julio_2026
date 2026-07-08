# API REST para gestión de usuarios y pedidos

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
