from __future__ import annotations

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE_PATH = ROOT / "reto-4-docstring" / "funciones_analisis.py"
OUTPUT_PATH = Path(__file__).resolve().parent / "funciones_analisis_docstring.py"


def build_docstring(function_name: str, node: ast.FunctionDef) -> list[str]:
    summaries = {
        "funcion_a": "Calcula un valor ajustado aplicando un factor y un desplazamiento.",
        "funcion_b": "Devuelve la fecha y hora actual en formato ISO 8601.",
        "funcion_c": "Registra un evento con su severidad y marca el momento de ocurrencia.",
        "funcion_d": "Construye un payload con los datos del usuario y los extras recibidos.",
    }

    args: list[str] = []
    positional = list(node.args.posonlyargs) + list(node.args.args)
    defaults = [None] * (len(positional) - len(node.args.defaults)) + list(node.args.defaults)

    for index, arg in enumerate(positional):
        default = ""
        if defaults[index] is not None:
            default = f" = {ast.unparse(defaults[index])}"
        args.append(f"{arg.arg} ({arg.annotation and ast.unparse(arg.annotation) or 'object'}): Parámetro de entrada{default}.")

    if node.args.vararg:
        args.append(f"*{node.args.vararg.arg} (object): Argumentos posicionales adicionales.")

    if node.args.kwarg:
        args.append(f"**{node.args.kwarg.arg} (object): Argumentos por nombre adicionales.")

    lines = [f'    """{summaries[function_name]}\n']
    if args:
        lines.extend(["\n", "    Args:\n"])
        for arg in args:
            lines.append(f"        {arg}\n")

    returns = None
    if isinstance(node.returns, ast.Constant) and node.returns.value is None:
        returns = None
    elif node.returns is not None:
        returns = f"{ast.unparse(node.returns)}: Valor devuelto por la función."

    if returns:
        lines.extend(["\n", "    Returns:\n"])
        lines.append(f"        {returns}\n")

    if function_name == "funcion_c":
        lines.extend(["\n", "    Note:\n"])
        lines.append("        Agrega el registro al almacenamiento global y lo imprime en consola.\n")

    lines.append('    """\n')
    return lines


def generate_docstrings() -> str:
    source = SOURCE_PATH.read_text(encoding="utf-8")
    tree = ast.parse(source)
    function_nodes = [node for node in tree.body if isinstance(node, ast.FunctionDef)]

    lines = source.splitlines(keepends=True)
    for node in reversed(function_nodes):
        insert_at = node.body[0].lineno - 1
        docstring_lines = build_docstring(node.name, node)
        lines[insert_at:insert_at] = docstring_lines

    return "".join(lines)


if __name__ == "__main__":
    output = generate_docstrings()
    OUTPUT_PATH.write_text(output, encoding="utf-8")
    print(f"Docstrings generados en {OUTPUT_PATH}")
