---
name: creador-entorno-python
description: Detecta dependencias externas en un script Python, resuelve mapeos no triviales y genera `requirements.txt` y comandos reproducibles para crear/activar un `venv` dentro de la carpeta del script.
applyTo: "**/*.py"
---

Objetivo
-
Proveer una skill reutilizable que, al activarse por frases naturales (por ejemplo: "preparar entorno", "generar dependencias", "crear requirements"), analice un script Python, extraiga imports externos, excluya la stdlib, resuelva mapeos de paquetes y genere un `requirements.txt` exactamente en el mismo directorio donde se encuentra el script. Además, debe proveer los comandos para crear y activar un entorno virtual y ejecutar la instalación en esa misma ruta.

Activación automática
-
Palabras clave (detonadores): preparar entorno, generar dependencias, crear requirements, preparar entorno virtual, instalar dependencias, crear venv

Flujo principal
-
1. Detección: cuando el usuario escribe una de las frases de activación en lenguaje natural, el agente invoca esta skill automáticamente.
2. Análisis: parsear el archivo objetivo y extraer todos los imports `import X` y `from X import Y`.
3. Filtrado stdlib: excluir módulos pertenecientes a la librería estándar de Python (uso de lista blanca/stdlib lookup).
4. Resolución de mapeos: transformar nombres de imports a paquetes PyPI cuando difieren. Ejemplos: `cv2` → `opencv-python`, `yaml` → `PyYAML`, `PIL`/`from PIL import Image` → `Pillow`, `dotenv`/`from dotenv import load_dotenv` → `python-dotenv`.
5. Salida: generar y guardar el archivo `requirements.txt` **dentro del mismo directorio donde se encuentra el script analizado**. Mostrar lista limpia de dependencias y un mapeo explícito de imports↔paquetes.
6. Entorno reproducible: preparar los comandos para navegar a la carpeta del script, crear/activar el `venv` e instalar las dependencias desde el `requirements.txt` recién creado. Antes de ejecutar estas acciones, la skill preguntará al usuario y sólo procederá si el usuario confirma.

Casos borde y reglas
-
- Excluir por completo cualquier módulo perteneciente a la stdlib (no deben aparecer en `requirements.txt`).
- Resolver mapeos comunes: `cv2` -> `opencv-python`, `yaml` -> `PyYAML`, `PIL` -> `Pillow`, `dotenv` -> `python-dotenv`.
- Si un import es ambiguo (por ejemplo paquetes con mismo nombre que stdlib y tercero), priorizar una heurística y mostrar la decisión junto al resultado para revisión.

Entregables
-
- `requirements.txt` generado **en la misma carpeta del archivo script analizado**.
- Resumen en chat con:
  - Lista de dependencias externas (una por línea).
  - Mapeo imports→paquetes para los casos no triviales.
  - Comandos a ejecutar (incluyendo el cambio de directorio) para crear/activar `venv` e instalar dependencias — la skill preguntará antes de ejecutar.

Comandos sugeridos
-
*Nota para el agente: Asegúrate de navegar al directorio correcto antes de ejecutar los comandos.*

Crear venv (Windows PowerShell):

```powershell
cd <ruta_al_directorio_del_script>
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

```

Crear venv (Unix/macOS):

```bash
cd <ruta_al_directorio_del_script>
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

```

## Integración con VS Code

* Recomendación: añadir una `task` que ejecute la creación del `venv` y la instalación desde `requirements.txt` en la carpeta activa.
* Palabras clave para la Command Palette: "Crear entorno (creador-entorno-python)", "Instalar dependencias (creador-entorno-python)".

## Ejemplos de prompts para el usuario

* "preparar entorno"
* "generar dependencias para reto-6-entorno/script_complejo.py"
* "crear requirements para este archivo"

## Notas de seguridad y alcance

* No modificar archivos de entrada fija del reto sin petición explícita del usuario (seguir reglas del sandbox).
* La skill generará automáticamente el `requirements.txt` en la carpeta del script. Para acciones que ejecutan cambios en el sistema (por ejemplo creación/activación del `venv` e instalación de paquetes), la skill preguntará al usuario antes de ejecutar y sólo procederá con su confirmación.

```