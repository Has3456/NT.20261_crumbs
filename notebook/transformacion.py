import pandas as pd


def transformar_gastos(df_limpio):


    # Agrupación 1: suma del valor por tipo de necesidad
    agrupacion1 = (
        df_limpio.groupby("tipo_necesidad")["valor"]
        .sum()
        .reset_index(name="total_valor")
    )

    # Agrupación 2: conteo de registros por frecuencia de gasto
    agrupacion2 = (
        df_limpio.groupby("frecuencia_gasto")["id"]
        .count()
        .reset_index(name="conteo")
    )

    # Agrupación 3: conteo cruzado tipo_necesidad vs grado_necesidad
    agrupacion3 = (
        df_limpio.groupby(["tipo_necesidad", "grado_necesidad"])["id"]
        .count()
        .reset_index(name="conteo")
    )

    return {
        "agrupacion1": agrupacion1,
        "agrupacion2": agrupacion2,
        "agrupacion3": agrupacion3,
    }


def transformar_usuarios(df_limpio):
    """
    Genera tres agrupaciones analíticas sobre los datos de usuarios.

    Retorna un diccionario con tres DataFrames:
      - agrupacion1: conteo de usuarios por ocupacion_principal
      - agrupacion2: conteo de usuarios por nivel_socioeconomico
      - agrupacion3: tabla cruzada ubicacion_geografica vs genero (para mapa de calor)
    """

    # Agrupación 1: conteo por ocupación principal
    agrupacion1 = (
        df_limpio.groupby("ocupacion_principal")["id"]
        .count()
        .reset_index(name="conteo")
    )

    # Agrupación 2: conteo por nivel socioeconómico
    agrupacion2 = (
        df_limpio.groupby("nivel_socioeconomico")["id"]
        .count()
        .reset_index(name="conteo")
    )

    # Agrupación 3: conteo cruzado ubicacion_geografica vs genero
    agrupacion3 = (
        df_limpio.groupby(["ubicacion_geografica", "genero"])["id"]
        .count()
        .reset_index(name="conteo")
    )

    return {
        "agrupacion1": agrupacion1,
        "agrupacion2": agrupacion2,
        "agrupacion3": agrupacion3,
    }
