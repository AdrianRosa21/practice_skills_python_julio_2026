"""Validaciones de entrada para operaciones de prorrateo.

FIX: corrige division por cero en prorrateo de montos.
"""


def prorratear_monto(total: float, cantidad_personas: int) -> float:
    """Divide un monto entre N personas de forma segura."""
    if cantidad_personas == 0:
        return 0.0
    return total / cantidad_personas
