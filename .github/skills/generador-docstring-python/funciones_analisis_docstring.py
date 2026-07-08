"""Funciones de análisis para documentar con docstrings."""

from __future__ import annotations

from datetime import datetime, timezone

REGISTRO_GLOBAL: list[dict] = []


def funcion_a(valor_base: float, factor: float, desplazamiento: float) -> float:
    """Calcula un valor ajustado aplicando un factor y un desplazamiento.

    Args:
        valor_base (float): Parámetro de entrada.
        factor (float): Parámetro de entrada.
        desplazamiento (float): Parámetro de entrada.

    Returns:
        float: Valor devuelto por la función.
    """
    resultado = (valor_base * factor) + desplazamiento
    return round(resultado, 4)


def funcion_b() -> str:
    """Devuelve la fecha y hora actual en formato ISO 8601.

    Returns:
        str: Valor devuelto por la función.
    """
    ahora = datetime.now(timezone.utc)
    return ahora.isoformat()


def funcion_c(evento: str, severidad: str) -> None:
    """Registra un evento con su severidad y marca el momento de ocurrencia.

    Args:
        evento (str): Parámetro de entrada.
        severidad (str): Parámetro de entrada.

    Note:
        Agrega el registro al almacenamiento global y lo imprime en consola.
    """
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
    """Construye un payload con los datos del usuario y los extras recibidos.

    Args:
        nombre (str): Parámetro de entrada.
        activo (bool): Parámetro de entrada = True.
        *args (object): Argumentos posicionales adicionales.
        **kwargs (object): Argumentos por nombre adicionales.

    Returns:
        dict: Valor devuelto por la función.
    """
    payload = {"nombre": nombre, "activo": activo, "extras": list(args)}
    payload.update(kwargs)
    return payload
