import re
import json
from pathlib import Path


INPUT_PATH = Path(__file__).parent / "desastre_variables.py"


def detect_format(name: str) -> str:
    if "_" in name:
        return "snake_case"
    if "-" in name:
        return "kebab-case"
    if name[0].isupper():
        return "PascalCase"
    if any(c.isupper() for c in name[1:]):
        return "camelCase"
    return "lowercase"


def split_identifier(name: str) -> list[str]:
    # First split on common delimiters
    if "_" in name:
        return [p for p in name.split("_") if p]
    if "-" in name:
        return [p for p in name.split("-") if p]

    # Split camelCase / PascalCase and keep numeric groups and uppercase acronyms
    parts = re.findall(r"[A-Z]+(?=[A-Z][a-z]|$)|[A-Z]?[a-z]+|\d+", name)
    return parts


def to_snake(name: str) -> str:
    parts = split_identifier(name)
    # Lowercase everything for the chosen normalization
    parts = [p.lower() for p in parts]
    return "_".join(parts)


def extract_identifiers(text: str) -> list[str]:
    ids = set()
    for line in text.splitlines():
        # function defs
        m = re.match(r"^\s*def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", line)
        if m:
            ids.add(m.group(1))
            continue
        # class defs
        m = re.match(r"^\s*class\s+([A-Za-z_][A-Za-z0-9_]*)\s*[:(]", line)
        if m:
            ids.add(m.group(1))
            continue
        # simple assignments
        m = re.match(r"^\s*([A-Za-z_][A-Za-z0-9_\-]*)\s*=", line)
        if m:
            ids.add(m.group(1))
            continue
        # dict keys in double quotes used as snake/camel examples (best-effort)
        for km in re.findall(r'"([A-Za-z0-9_\-]+)"\s*:', line):
            ids.add(km)

    return sorted(ids)


def analyze_and_propose(text: str) -> dict:
    identifiers = extract_identifiers(text)
    mapping = []

    for name in identifiers:
        fmt = detect_format(name)
        notes = []

        if len(name) == 1:
            notes.append("single_char: revisar semántica; se sugiere prefijo 'var_'")
            proposed = f"var_{name}"
        else:
            proposed = to_snake(name)

        # Special handling for numeric-only or numbers in name: preserve position
        if re.fullmatch(r"\d+", name):
            notes.append("numeric_identifier")

        # Detect acronyms (consecutive uppercase letters) in original
        if re.search(r"[A-Z]{2,}", name):
            acr = re.findall(r"[A-Z]{2,}", name)
            notes.append(f"siglas_detectadas={acr}")

        mapping.append({
            "original": name,
            "detected_format": fmt,
            "proposed": proposed,
            "notes": notes,
        })

    result = {
        "normalization_rule": "snake_case_lowercase",
        "details": (
            "Regla: convertir todos los identificadores a snake_case en minúsculas. "
            "Siglas se detectan y se bajan a minúsculas (p.ej. API -> api). "
            "Variables de un solo carácter se marcan para revisión y se sugiere 'var_<x>'. "
            "Números se conservan en la posición original dentro del identificador."
        ),
        "mapping": mapping,
    }
    return result


def main():
    text = INPUT_PATH.read_text(encoding="utf-8")
    result = analyze_and_propose(text)

    out_json = INPUT_PATH.parent / "mapping.json"
    out_md = INPUT_PATH.parent / "resultado.md"
    out_json.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    # Write a readable markdown result
    lines = ["# Resultado de normalización", "", "**Regla aplicada:** snake_case_lowercase", "", "**Detalles:**", "", result["details"], "", "**Mapeo:**", ""]
    for m in result["mapping"]:
        notes = "; ".join(m["notes"]) if m["notes"] else ""
        lines.append(f"- {m['original']} -> {m['proposed']}  {('(' + notes + ')') if notes else ''}")

    out_md.write_text("\n".join(lines), encoding="utf-8")
    print(f"Mapping generado: {out_json}\nResumen: {out_md}")


if __name__ == "__main__":
    main()
