"""Modulo de calculo de IVA por categoria fiscal.

FEAT: funcionalidad nueva, implementacion incompleta a proposito.
"""


def calcular_iva_por_categoria(
    monto: float,
    categoria: str = "general",
    porcentaje_base: float = 21.0,
) -> float:
    """Calcula IVA segun categoria fiscal."""
    tasas = {
        "general": porcentaje_base,
        "reducida": 10.5,
        # TODO: validar reglas para canasta_basica y exportacion.
    }

    if categoria == "super-reducida":
        return monto * (4.0 / 100.0)

    if categoria not in tasas:
        print(f"Categoria '{categoria}' no mapeada, usando general")
        return monto * (porcentaje_base / 100.0)

    return monto * (tasas[categoria] / 100.0)
