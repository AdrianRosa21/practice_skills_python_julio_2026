# Sandbox Repository — Taller de Agent Skills en VS Code

## ¿Qué es este sandbox?

Este repositorio es un **terreno de juego controlado** para un taller práctico de Agent Skills.
Está diseñado para estudiantes de 3.º año de ingeniería que practicarán cómo redactar prompts para agentes
que analizan, transforman o documentan código existente.

En este entorno:

- No se espera que programes desde cero.
- Sí se espera que diseñes prompts precisos para que un agente resuelva tareas reales sobre código ambiguo, incompleto o desordenado.
- Los retos incluyen casos borde para evaluar si tu skill detecta contexto y evita soluciones genéricas.

## Regla crítica del taller

> **No modifiques los archivos dentro de `reto-N/`.**
> Esos archivos son la **entrada fija de prueba**.
> Tu skill debe **leerlos e inferir**, no alterarlos manualmente.

## Mapa de retos y skills (a construir por el estudiante)

Completa la columna **Skill objetivo** durante el taller.

| Reto | Carpeta | Qué debe lograr la skill | Skill objetivo (completar) |
| --- | --- | --- | --- |
| 1 | `reto-1-commits/` | Analizar cambios staged generados por spec y proponer commits Conventional Commits separados; advertir si se mezclan cambios no relacionados | `generador-commits` |
| 2 | `reto-2-nombres/` | Inferir estilo de nombres original y normalizar nomenclatura de forma consistente | `traductor-nombres` |
| 3 | `reto-3-mockdata/` | Generar mock data JSON relacional válida (Usuario → Pedidos), con correos válidos y fechas coherentes | `generador-datos-prueba` |
| 4 | `reto-4-docstring/` | Crear docstrings correctos según firma real, sin inventar secciones Args/Returns cuando no aplican | `generador-docstring-python` |
| 5 | `reto-5-readme/` | Convertir notas desordenadas en README estructurado según tipo de proyecto elegido | `generador-readme` |
| 6 | `reto-6-entorno/` | Generar `requirements.txt` correcto distinguiendo stdlib/externas y resolviendo import ≠ paquete | `creador-entorno-python` |

## Estructura esperada

```text
.github/skills/
reto-1-commits/
reto-2-nombres/
reto-3-mockdata/
reto-4-docstring/
reto-5-readme/
reto-6-entorno/
```

## Recomendación de uso en clase

1. Lee el enunciado de cada reto.
2. Diseña prompts iterativos para tu skill.
3. Evalúa la salida contra los casos borde.
4. Refina instrucciones hasta lograr comportamiento robusto y específico.

## Reto 1: flujo spec-driven (obligatorio antes de practicar)

Antes de usar la skill `generador-commits`, ejecuta:

```bash
python3 reto-1-commits/generar_stage_area.py
```

Este comando:

1. Lee el spec `reto-1-commits/spec_stage_area.json`.
2. Copia plantillas desde `reto-1-commits/templates/` a `reto-1-commits/staged/`.
3. Deja esos archivos en staged con `git add`, sin confirmar commit.
4. Genera 5 cambios independientes (feat, fix, docs, refactor, chore) para analizar.
