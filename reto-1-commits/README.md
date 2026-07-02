# Reto 1 — generador-commits

Este reto usa un flujo **spec-driven**: un spec JSON define varios cambios
independientes y un script los genera en el **stage area** de git.

## Paso 1: generar los archivos de ejercicio

```bash
python3 reto-1-commits/generar_stage_area.py
```

Esto crea 5 archivos en `reto-1-commits/staged/` (uno por tipo de cambio)
y los deja en staged con `git add`:

| Archivo generado | Tipo Conventional Commit |
| --- | --- |
| `feat_calculo_iva.py` | `feat` |
| `fix_validacion_entrada.py` | `fix` |
| `docs_guia_api.md` | `docs` |
| `refactor_utilidades.py` | `refactor` |
| `chore_config_editor.txt` | `chore` |

## Paso 2: analizar con tu skill

Tu skill **`generador-commits`** debe leer los cambios staged:

```bash
git diff --staged
git status
```

Y proponer mensajes de commit separados, **advertiendo** si alguien intenta
un unico commit generico para todos los cambios.

## Dry run

```bash
python3 reto-1-commits/generar_stage_area.py --dry-run
```

Genera archivos sin ejecutar `git add`.

## Archivos del reto (no modificar)

- `spec_stage_area.json` — definicion spec-driven de los cambios
- `templates/` — plantillas fuente de cada cambio
- `generar_stage_area.py` — script invocable
- `EJERCICIO.md` — enunciado completo del ejercicio
