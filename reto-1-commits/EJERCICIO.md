# Ejercicio: generador-commits

## Contexto de practica

Este reto esta disenado para construir una skill de VS Code llamada **`generador-commits`**.
La skill debe analizar cambios en el **stage area** de git y proponer mensajes
de commit con formato **Conventional Commits**.

## Como preparar el ejercicio

Antes de usar la skill, ejecuta el generador spec-driven:

```bash
python3 reto-1-commits/generar_stage_area.py
```

Esto crea archivos independientes en `reto-1-commits/staged/` y los deja en staged.
Esos archivos generados son la **entrada de evaluacion** para tu skill.

> No modifiques `spec_stage_area.json`, `templates/` ni `generar_stage_area.py`.
> Son la infraestructura fija del reto.

## Que debe hacer la skill

1. Leer los cambios staged (`git diff --staged` o equivalente).
2. Proponer un mensaje de commit en formato Conventional Commits **por cada cambio**.
3. Distinguir correctamente entre: `feat`, `fix`, `refactor`, `docs`, `chore`.
4. Si detecta multiples cambios no relacionados en una sola propuesta, **debe advertir/rechazar**
   en vez de generar un unico commit generico.

## Casos borde obligatorios

- Cinco cambios independientes staged simultaneamente (feat, fix, docs, refactor, chore).
- Cambio puramente documental (`docs`) sin logica de codigo.
- Cambio tecnico de mantenimiento (`chore`) sin impacto funcional.
- Cambio de reordenamiento interno (`refactor`) sin alterar comportamiento observable.
- Mezcla de archivos `.py`, `.md` y `.txt` con intenciones distintas.

## Entregable esperado de la skill

- Mensaje(s) de commit propuestos con estructura Conventional Commits.
- Justificacion breve del tipo elegido para cada archivo.
- Advertencia explicita cuando se intente agrupar cambios no relacionados en un solo commit.
