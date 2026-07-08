"""Utilidades de formateo — refactor sin cambio de comportamiento.

REFACTOR: se reordenaron helpers; la logica observable es la misma.
"""


def _formatear_moneda(valor: float) -> str:
    return f"${valor:,.2f}"


def _redondear(valor: float, decimales: int = 2) -> float:
    return round(valor, decimales)


def presentar_total(valor: float) -> str:
    """Formatea un total monetario para mostrar en UI."""
    return _formatear_moneda(_redondear(valor))
