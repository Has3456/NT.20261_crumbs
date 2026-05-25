import pandas as pd


def describir_gastos(df_limpio):
    print("\n" + "=" * 50)
    print("*** DESCRIPCIÓN DEL DATASET: GASTOS ***")
    print("=" * 50)
    print(f"Número de filas  : {df_limpio.shape[0]}")
    print(f"Número de columnas: {df_limpio.shape[1]}")
    print(f"Columnas disponibles: {list(df_limpio.columns)}")
    print(f"\nTipos de dato:\n{df_limpio.dtypes}")

    print("\n*** ESTADÍSTICAS NUMÉRICAS ***")
    columnas_numericas = [c for c in ["id", "valor"] if c in df_limpio.columns]
    if columnas_numericas:
        print(df_limpio[columnas_numericas].describe())

    print("\n*** CONTEOS ***")
    for col in ["tipo_necesidad", "grado_necesidad", "frecuencia_gasto", "medio_verificacion"]:
        if col in df_limpio.columns:
            print(f"\n{col}:\n{df_limpio[col].value_counts()}")

    if "fecha" in df_limpio.columns:
        print("\n*** RANGO DE FECHAS ***")
        print(f"Fecha más antigua: {df_limpio['fecha'].min()}")
        print(f"Fecha más reciente: {df_limpio['fecha'].max()}")


def describir_usuarios(df_limpio):
    print("\n" + "=" * 50)
    print("*** DESCRIPCIÓN DEL DATASET: USUARIOS ***")
    print("=" * 50)
    print(f"Número de filas  : {df_limpio.shape[0]}")
    print(f"Número de columnas: {df_limpio.shape[1]}")
    print(f"Columnas disponibles: {list(df_limpio.columns)}")
    print(f"\nTipos de dato:\n{df_limpio.dtypes}")

    print("\n*** ESTADÍSTICAS NUMÉRICAS ***")
    columnas_numericas = [c for c in ["id", "edad"] if c in df_limpio.columns]
    if columnas_numericas:
        print(df_limpio[columnas_numericas].describe())

    print("\n*** CONTEOS ***")
    for col in ["genero", "nivel_socioeconomico", "ocupacion_principal", "ubicacion_geografica"]:
        if col in df_limpio.columns:
            print(f"\n{col}:\n{df_limpio[col].value_counts()}")
