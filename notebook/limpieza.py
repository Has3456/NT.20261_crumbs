import pandas as pd


# ─────────────────────────────────────────────
#  LIMPIEZA DE GASTOS
# ─────────────────────────────────────────────

def limpiar_gastos(data_frame_sucio):
    gasto_limpio = data_frame_sucio.copy()

    # 1. Columnas de texto: quitar espacios y pasar a minúsculas
    columnas_texto = [
        "grado_necesidad", "descripcion", "fecha",
        "tipo_necesidad", "lugar_consumo",
        "frecuencia_gasto", "medio_verificacion",
    ]
    for columna in columnas_texto:
        if columna in gasto_limpio.columns:
            gasto_limpio[columna] = (
                gasto_limpio[columna].astype("string").str.strip().str.lower()
            )

    # 2. Valores esperados por columna categórica
    medios_esperados = [
        "efectivo", "tarjeta de crédito",
        "transferencia bancaria", "pago móvil", "cheque",
    ]
    gasto_limpio["medio_verificacion"] = gasto_limpio["medio_verificacion"].where(
        gasto_limpio["medio_verificacion"].isin(medios_esperados), pd.NA
    )

    grados_esperados = ["alta", "media", "baja"]
    gasto_limpio["grado_necesidad"] = gasto_limpio["grado_necesidad"].where(
        gasto_limpio["grado_necesidad"].isin(grados_esperados), pd.NA
    )

    frecuencias_esperadas = ["diaria", "semanal", "mensual", "anual"]
    gasto_limpio["frecuencia_gasto"] = gasto_limpio["frecuencia_gasto"].where(
        gasto_limpio["frecuencia_gasto"].isin(frecuencias_esperadas), pd.NA
    )

    # 3. Numéricos
    gasto_limpio["id"] = pd.to_numeric(gasto_limpio["id"], errors="coerce")
    gasto_limpio["valor"] = pd.to_numeric(gasto_limpio["valor"], errors="coerce")

    gasto_limpio = gasto_limpio[gasto_limpio["id"] > 0]
    gasto_limpio = gasto_limpio[gasto_limpio["valor"] > 50000]

    # 4. Fechas
    gasto_limpio["fecha"] = pd.to_datetime(gasto_limpio["fecha"], errors="coerce")
    fecha_default = pd.to_datetime("2026-01-01")
    gasto_limpio["fecha"] = gasto_limpio["fecha"].fillna(fecha_default)

    # 5. Eliminar filas con campos obligatorios vacíos y duplicados
    columnas_obligatorias = [
        "id", "fecha", "valor", "tipo_necesidad",
        "frecuencia_gasto", "lugar_consumo",
        "medio_verificacion", "grado_necesidad", "descripcion",
    ]
    columnas_obligatorias = [c for c in columnas_obligatorias if c in gasto_limpio.columns]
    gasto_limpio = gasto_limpio.dropna(subset=columnas_obligatorias)
    gasto_limpio = gasto_limpio.drop_duplicates()

    return gasto_limpio


# ─────────────────────────────────────────────
#  LIMPIEZA DE USUARIOS
# ─────────────────────────────────────────────

def limpiar_usuarios(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    # 1. Columnas de texto: quitar espacios y pasar a minúsculas
    columnas_textos = [
        "nombre", "tipo_documento", "documento",
        "ocupacion_principal", "nivel_socioeconomico",
        "rango_ingresos_mensuales", "ubicacion_geografica", "genero",
    ]
    for columna in columnas_textos:
        if columna in data_frame_limpio.columns:
            data_frame_limpio[columna] = (
                data_frame_limpio[columna].astype("string").str.strip().str.lower()
            )

    # 2. Valores esperados por columna categórica
    nombre_esperado = [
        "juan fernando gallego", "maria jose perez",
        "carlos mario sanchez", "ana gomez", "luis rodriguez",
    ]
    data_frame_limpio["nombre"] = data_frame_limpio["nombre"].where(
        data_frame_limpio["nombre"].isin(nombre_esperado), pd.NA
    )

    tipo_documento_esperado = ["cc", "ti", "ce", "pp"]
    data_frame_limpio["tipo_documento"] = data_frame_limpio["tipo_documento"].where(
        data_frame_limpio["tipo_documento"].isin(tipo_documento_esperado), pd.NA
    )

    documento_esperado = ["123456789", "987654321", "456789123", "321654987", "654321789"]
    data_frame_limpio["documento"] = data_frame_limpio["documento"].where(
        data_frame_limpio["documento"].isin(documento_esperado), pd.NA
    )

    ocupacion_esperada = ["estudiante", "empleado", "desempleado", "independiente", "jubilado"]
    data_frame_limpio["ocupacion_principal"] = data_frame_limpio["ocupacion_principal"].where(
        data_frame_limpio["ocupacion_principal"].isin(ocupacion_esperada), pd.NA
    )

    nivel_esperado = ["bajo", "medio", "alto", "muy alto"]
    data_frame_limpio["nivel_socioeconomico"] = data_frame_limpio["nivel_socioeconomico"].where(
        data_frame_limpio["nivel_socioeconomico"].isin(nivel_esperado), pd.NA
    )

    rango_esperado = ["1700000", "2600000", "2100000", "3800000", "2500000"]
    data_frame_limpio["rango_ingresos_mensuales"] = data_frame_limpio["rango_ingresos_mensuales"].where(
        data_frame_limpio["rango_ingresos_mensuales"].isin(rango_esperado), pd.NA
    )

    ubicacion_esperada = ["girardot", "medellin", "la doctora", "sabaneta", "san antonio de prado"]
    data_frame_limpio["ubicacion_geografica"] = data_frame_limpio["ubicacion_geografica"].where(
        data_frame_limpio["ubicacion_geografica"].isin(ubicacion_esperada), pd.NA
    )

    genero_esperado = ["masculino", "femenino"]
    data_frame_limpio["genero"] = data_frame_limpio["genero"].where(
        data_frame_limpio["genero"].isin(genero_esperado), pd.NA
    )

    # 3. Numéricos
    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"], errors="coerce")
    data_frame_limpio["edad"] = pd.to_numeric(data_frame_limpio["edad"], errors="coerce")
    if "id_gastos" in data_frame_limpio.columns:
        data_frame_limpio["id_gastos"] = pd.to_numeric(data_frame_limpio["id_gastos"], errors="coerce")

    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"] > 0]
    data_frame_limpio["edad"] = data_frame_limpio["edad"].apply(
        lambda x: int(x) if pd.notna(x) and x > 0 else pd.NA
    )
    if "id_gastos" in data_frame_limpio.columns:
        data_frame_limpio = data_frame_limpio[data_frame_limpio["id_gastos"] > 0]

    # 4. Eliminar filas con campos obligatorios vacíos y duplicados
    columnas_obligatorias = [
        "id", "nombre", "tipo_documento", "documento",
        "ocupacion_principal", "nivel_socioeconomico",
        "rango_ingresos_mensuales", "ubicacion_geografica",
        "genero", "edad",
    ]
    columnas_obligatorias = [c for c in columnas_obligatorias if c in data_frame_limpio.columns]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio
