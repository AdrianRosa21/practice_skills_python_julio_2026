# Reto 1 - Commits mezclados

Este reto incluye dos senales mezcladas en el mismo archivo:

- un cambio de tipo `feat` (IVA por categoria, incompleto),
- un cambio de tipo `fix` (division por cero corregida).

La skill del alumno debe detectar que no corresponde un solo commit generico.

## Modo spec-driven (invocable)

Para generar artefactos auxiliares y dejarlos en el **stage area** automaticamente:

```bash
python3 reto-1-commits/generar_stage_area.py
```

Esto lee `spec_stage_area.json`, crea archivos en `reto-1-commits/staged/` y ejecuta `git add` solo para esos artefactos.

### Dry run

```bash
python3 reto-1-commits/generar_stage_area.py --dry-run
```

## Criterio didactico

Los archivos generados en staged sirven para practicar prompts de analisis de commits y separacion de cambios por intencion.
