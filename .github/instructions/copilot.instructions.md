---
name: Sandbox Agent Skills — Reglas del taller
description: Reglas universales del repositorio sandbox. Protegen las entradas de prueba y evitan que el agente aplique convenciones globales que rompan los ejercicios.
applyTo: "**"
---

# Contexto del repositorio

Este workspace es un **sandbox pedagógico** para un taller de **Agent Skills en VS Code**.
Los estudiantes construyen skills que **leen, analizan y transforman** código existente; no se espera programar desde cero ni “arreglar” el repositorio.

Antes de actuar, identifica en qué reto estás trabajando y lee el archivo `EJERCICIO.md` de esa carpeta.

---

# Zonas del repositorio

| Zona | Rol | Regla |
| --- | --- | --- |
| `.github/skills/` | Donde el estudiante **construye sus skills** | Puedes crear y editar aquí libremente |
| `reto-N/` | Entradas fijas de evaluación | **Solo lectura por defecto** (ver excepciones) |
| `reto-1-commits/staged/` | Archivos generados por el spec para practicar commits | Solo lectura; se crean con `generar_stage_area.py` |
| `reto-1-commits/templates/`, `spec_stage_area.json`, `generar_stage_area.py` | Infraestructura del reto 1 | No modificar |

---

# Regla principal: no corromper las entradas de prueba

**No modifiques** los archivos de entrada fija dentro de `reto-N/`, salvo que el usuario lo pida de forma explícita y justificada.

Entradas protegidas:

- `reto-2-nombres/desastre_variables.py`
- `reto-3-mockdata/modelos_relacionales.py`
- `reto-4-docstring/funciones_analisis.py`
- `reto-5-readme/detalles_proyecto.txt`
- `reto-6-entorno/script_complejo.py`

Modo de trabajo por defecto sobre estas rutas: **leer → analizar → proponer salida** (en chat, archivo nuevo o carpeta de skill), **sin editar el fixture**.

---

# Lo que NO debes imponer de forma global

Estas convenciones son **específicas de cada ejercicio**. No las apliques automáticamente a todo el repo:

| Convención | Por qué NO es global | Ejercicio que la define |
| --- | --- | --- |
| Normalizar a `snake_case` (u otro estilo fijo) | El código de prueba tiene nomenclatura mezclada a propósito | Reto 2 — `traductor-nombres` |
| Proponer o ejecutar commits | Solo aplica al flujo de cambios staged del reto 1 | Reto 1 — `generador-commits` |
| Generar docstrings | Solo aplica a funciones del reto 4 | Reto 4 — `generador-docstring-python` |
| Generar README.md | Solo aplica a notas del reto 5 | Reto 5 — `generador-readme` |
| Generar `requirements.txt` o comandos de venv | Solo aplica al script del reto 6 | Reto 6 — `creador-entorno-python` |
| Generar mock data JSON | Solo aplica a modelos del reto 3 | Reto 3 — `generador-datos-prueba` |
| “Limpiar”, refactorizar o corregir el código sucio | Destruye el valor pedagógico del sandbox | Todos los retos |

**No refactorices, no corrijas estilo, no agregues docstrings ni “mejores prácticas”** en archivos de `reto-N/` a menos que el usuario lo solicite explícitamente para ese reto concreto.

---

# Comportamiento esperado por reto (referencia rápida)

| Reto | Skill objetivo | Qué hacer | Qué evitar |
| --- | --- | --- | --- |
| 1 | `generador-commits` | Analizar `git diff --staged` tras ejecutar el generador; proponer commits Conventional Commits **separados**; advertir si se mezclan cambios no relacionados | Un solo commit genérico; modificar templates o spec |
| 2 | `traductor-nombres` | Detectar formato de entrada automáticamente; proponer conversión entre camelCase, snake_case, kebab-case, PascalCase | Imponer un estilo global al repo; editar el fixture |
| 3 | `generador-datos-prueba` | Generar JSON con relaciones Usuario→Pedidos, emails válidos, fechas coherentes | Datos incoherentes o quemados en el fixture |
| 4 | `generador-docstring-python` | Documentar según firma real (Google o NumPy); omitir Args/Returns cuando no correspondan | Inventar secciones vacías; modificar el fixture |
| 5 | `generador-readme` | Adaptar README al tipo de proyecto (API, librería, app); evitar plantilla rígida | README genérico idéntico para todos los tipos |
| 6 | `creador-entorno-python` | Separar stdlib de externas; resolver import≠paquete (`cv2`, `yaml`, `PIL`) | Incluir stdlib en requirements; mapeo 1:1 ingenuo |

---

# Git

- **No hagas `git commit` ni `git push`** salvo petición explícita del usuario.
- En el reto 1, el generador (`python3 reto-1-commits/generar_stage_area.py`) deja archivos en staged; tu rol es **analizar**, no confirmar commits automáticamente.
- Puedes usar comandos de lectura (`git status`, `git diff`, `git diff --staged`) cuando el ejercicio lo requiera.

---

# Python y calidad mínima

- Compatibilidad: **Python 3.10+**.
- Si escribes o editas Python (por ejemplo en `.github/skills/`), el código debe ser **sintácticamente válido** (`ast.parse` no debe fallar).
- Mantén el alcance mínimo: no agregues funcionalidad, tests ni archivos no solicitados.

---

# Idioma y entregables

- Responde al usuario en **español**.
- Cuando una skill produzca resultados (commits propuestos, nombres normalizados, JSON, docstrings, README, requirements), entrégalos como:
  1. salida en el chat, o
  2. archivo nuevo en `.github/skills/<nombre-skill>/`, o
  3. ruta explícitamente indicada por el usuario.

Nunca sobrescribas las entradas fijas de `reto-N/` como entregable por defecto.

---

# Detección de contexto

Si el usuario no indica el reto:

1. Infiérelo por la ruta del archivo abierto o mencionado.
2. Lee `reto-N/EJERCICIO.md` correspondiente.
3. Aplica **solo** las reglas de ese ejercicio, sin arrastrar convenciones de otros retos.

Si hay ambigüedad, pregunta antes de modificar archivos.

---
# Skill: creador-entorno-python

**Propósito:** Detectar dependencias reales de un script Python, resolver mapeos no triviales (ej. `cv2`→`opencv-python`, `yaml`→`PyYAML`, `PIL`→`Pillow`, `dotenv`→`python-dotenv`) y generar un `requirements.txt` y los comandos para crear/activar un `venv`.

**Activación automática:** El agente invoca esta skill automáticamente cuando el usuario escribe en lenguaje natural frases como: "preparar entorno", "generar dependencias", "crear requirements", "crear venv", "instalar dependencias". No se requiere `/` ni `@`.

**Reglas de uso dentro del sandbox:**
- Seguir la regla principal: no modificar archivos de entrada fija dentro de `reto-N/` salvo petición explícita del usuario. La skill debe leer y analizar el script (por ejemplo `reto-6-entorno/script_complejo.py`) pero generar su salida en la raíz del workspace o en `.github/skills/` según el flujo del ejercicio.
- Excluir por completo módulos de la stdlib del `requirements.txt`.
- Evitar confirmaciones interactivas: la skill generará `requirements.txt` y mostrará/ejecutará los comandos de creación/activación del `venv` e instalación de dependencias tal como indica el ejercicio, dejando al usuario el control final sobre ejecuciones en su entorno.

