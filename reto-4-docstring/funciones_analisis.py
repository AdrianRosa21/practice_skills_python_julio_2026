"""Funciones de análisis para documentar con docstrings."""

from __future__ import annotations

from datetime import datetime, timezone

REGISTRO_GLOBAL: list[dict] = []


def funcion_a(valor_base: float, factor: float, desplazamiento: float) -> float:
    resultado = (valor_base * factor) + desplazamiento
    return round(resultado, 4)


def funcion_b() -> str:
    ahora = datetime.now(timezone.utc)
    return ahora.isoformat()


def funcion_c(evento: str, severidad: str) -> None:
    registro = {
        "evento": evento,
        "severidad": severidad,
        "momento": funcion_b(),
    }
    REGISTRO_GLOBAL.append(registro)
    print(f"[{severidad}] {evento}")


def funcion_d(
    nombre: str,
    activo: bool = True,
    *args: object,
    **kwargs: object,
) -> dict:
    payload = {"nombre": nombre, "activo": activo, "extras": list(args)}
    payload.update(kwargs)
    return payload
