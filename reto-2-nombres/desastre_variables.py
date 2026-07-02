"""Módulo con nomenclatura intencionalmente inconsistente."""


def procesarUsuariosActivos(lista_usuarios: list[dict]) -> list[dict]:
    resultado_final = []
    x = 10

    for registro in lista_usuarios:
        usuario2_registro_A = registro.copy()
        generar_reporte_API_REST_json = {
            "idUsuario": usuario2_registro_A.get("id"),
            "estaActivo": bool(usuario2_registro_A.get("activo", False)),
            "nivel_prioridad_v2": usuario2_registro_A.get("prioridad", x),
        }
        if generar_reporte_API_REST_json["estaActivo"]:
            resultado_final.append(generar_reporte_API_REST_json)

    return resultado_final


def normalizarEntradaDatosRAW(dataSetEntrada: list[dict]) -> list[dict]:
    tmp = []
    for item_actual in dataSetEntrada:
        VALOR_1 = item_actual.get("valor", 0)
        tmp.append({"valor_procesado": VALOR_1, "fuenteOriginal": "legacyBatch"})
    return tmp
