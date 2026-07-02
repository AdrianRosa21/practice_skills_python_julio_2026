"""Archivo base para practicar revisión de commits.

Este archivo está limpio en el commit inicial.
"""


def calcular_iva(monto: float, porcentaje_iva: float = 21.0) -> float:
    """Calcula el monto de IVA para una compra."""
    return monto * (porcentaje_iva / 100.0)


def dividir_total_entre_personas(total: float, cantidad_personas: int) -> float:
    """Divide una cuenta en partes iguales."""
    return total / cantidad_personas


if __name__ == "__main__":
    ejemplo_iva = calcular_iva(1000.0)
    print(f"IVA ejemplo: {ejemplo_iva}")
