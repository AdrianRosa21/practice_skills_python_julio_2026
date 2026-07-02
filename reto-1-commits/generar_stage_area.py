"""Generador spec-driven de artefactos staged para reto de commits.

Uso rapido:
    python3 reto-1-commits/generar_stage_area.py
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def _ejecutar_git(args: list[str], repo_root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo_root,
        text=True,
        capture_output=True,
        check=False,
    )


def _repo_root_desde_git(inicio: Path) -> Path:
    resultado = _ejecutar_git(["rev-parse", "--show-toplevel"], inicio)
    if resultado.returncode != 0:
        raise RuntimeError("No se pudo resolver la raiz git. Ejecuta dentro de un repositorio.")
    return Path(resultado.stdout.strip())


def _cargar_spec(path_spec: Path) -> dict:
    if not path_spec.exists():
        raise FileNotFoundError(f"Spec no encontrado: {path_spec}")
    contenido = path_spec.read_text(encoding="utf-8")
    data = json.loads(contenido)

    if "output_dir" not in data or "artifacts" not in data:
        raise ValueError("El spec debe definir 'output_dir' y 'artifacts'.")
    if not isinstance(data["artifacts"], list) or not data["artifacts"]:
        raise ValueError("El campo 'artifacts' debe ser una lista no vacia.")
    return data


def _renderizar_markdown(artifact: dict, spec_version: str) -> str:
    ahora = datetime.now(timezone.utc).isoformat()
    checks = artifact.get("acceptance_checks", [])
    touched_files = artifact.get("touched_files", [])

    lineas = [
        f"# {artifact['title']}",
        "",
        f"- Tipo de cambio: `{artifact['change_type']}`",
        f"- Spec version: `{spec_version}`",
        f"- Generado en UTC: `{ahora}`",
        "",
        "## Resumen",
        artifact["summary"],
        "",
        "## Archivos afectados",
    ]

    for item in touched_files:
        lineas.append(f"- `{item}`")

    lineas.extend(["", "## Acceptance checks"])
    for check in checks:
        lineas.append(f"- [ ] {check}")

    lineas.extend(
        [
            "",
            "## Nota didactica",
            "Este artefacto existe para entrenar una skill que separe cambios no relacionados en commits independientes.",
            "",
        ]
    )
    return "\n".join(lineas)


def generar_artefactos(spec_path: Path, dry_run: bool) -> list[Path]:
    repo_root = _repo_root_desde_git(spec_path.parent)
    data = _cargar_spec(spec_path)
    output_dir = repo_root / data["output_dir"]
    output_dir.mkdir(parents=True, exist_ok=True)

    spec_version = str(data.get("version", "sin-version"))
    generados: list[Path] = []

    for artifact in data["artifacts"]:
        requeridos = {"filename", "change_type", "title", "summary"}
        faltantes = requeridos.difference(artifact)
        if faltantes:
            faltan = ", ".join(sorted(faltantes))
            raise ValueError(f"Artifact incompleto, faltan campos: {faltan}")

        destino = output_dir / artifact["filename"]
        contenido = _renderizar_markdown(artifact, spec_version=spec_version)
        destino.write_text(contenido, encoding="utf-8")
        generados.append(destino)

    if not dry_run and generados:
        rutas_relativas = [str(path.relative_to(repo_root)) for path in generados]
        add = _ejecutar_git(["add", *rutas_relativas], repo_root)
        if add.returncode != 0:
            raise RuntimeError(f"Fallo 'git add': {add.stderr.strip()}")

    return generados


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Genera y stagea archivos a partir de un spec JSON para el reto 1."
    )
    parser.add_argument(
        "--spec",
        type=Path,
        default=Path(__file__).with_name("spec_stage_area.json"),
        help="Ruta al archivo spec JSON.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Genera archivos, pero no ejecuta git add.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    try:
        generados = generar_artefactos(spec_path=args.spec.resolve(), dry_run=args.dry_run)
    except Exception as exc:  # pragma: no cover - salida CLI
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print("Artefactos generados:")
    for path in generados:
        print(f"- {path}")
    if args.dry_run:
        print("Dry run activo: no se agregaron archivos al stage area.")
    else:
        print("Listo: archivos agregados al stage area con git add.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
