import pandas as pd

def limpiar_gasto(gastos_sucio):
    gasto_limpio = gastos_sucio.copy()

    columnas_gasto = ["valor", "grado_necesidad", "descripción", "fecha", "tipo_necesidad", "lugar_consumo", 
                    "frecuencia_gasto", "medio_verificación", "descripción"]
    
    #Rutina para evaluar textos
    #limpiar textos de las columnas de tipo string, eliminando espacios y convirtiendo a minúsculas
    
    for columna in columnas_gasto:
         gasto_limpio[columna] = gasto_limpio[columna].astype("string").str.strip().str.lower()



    #limpiar textos solo con valores esperados en medio de verificacion
    medios_esperados = ["efectivo", "tarjeta de crédito", "transferencia bancaria", 
                       "pago móvil", "cheque"]
    
    gasto_limpio["medio_verificación"] = gasto_limpio ["medio_verificación"].where(
        gasto_limpio["medio_verificación"].isin(medios_esperados), 
        pd.NA
    )

    #limpiar textos solo con valores esperados en grado de necesidad
    grados_esperados = ["alta", "media", "baja"]

    gasto_limpio["grado_necesidad"] = gasto_limpio["grado_necesidad"].where(
        gasto_limpio["grado_necesidad"].isin(grados_esperados),
        pd.NA
    )

    #limpiar textos solo con valores esperados en frecuencia del gasto
    frecuencias_esperadas = ["diaria", "semanal", "mensual", "anual"]

    gasto_limpio["frecuencia_gasto"] = gasto_limpio["frecuencia_gasto"].where(
        gasto_limpio["frecuencia_gasto"].isin(frecuencias_esperadas),
        pd.NA
    )

    #rutina para evaluar numeros 
    gasto_limpio["id"] = pd.to_numeric(gasto_limpio["id"])
    gasto_limpio["valor"] = pd.to_numeric(gasto_limpio["valor"])

    #evaluar solo valores numericos permitidos 
    gasto_limpio["id"] = gasto_limpio["id"] [gasto_limpio["id"] > 0]
    gasto_limpio["valor"] = gasto_limpio["valor"] [gasto_limpio["valor"] > 50000]
   
    #rutina para evaluar fechas
    #evaluemos que una fecha si es una fecha 

    fecha_default = pd.to_datetime("2026-01-01")
    gasto_limpio["fecha"] = gasto_limpio["fecha"].fillna(fecha_default)

    #rutina para evaluar novedades
    #evaluamos campos obligatorios, si estan vacios los llenamos con un valor por defecto o los eliminamos
    columnas_obligatorias = ["id", "fecha", "valor", "tipo_necesidad", "frecuencia_gasto", "lugar_consumo",
                            "medio_verificación", "grado_necesidad", "descripción"]
    
    gasto_limpio = gasto_limpio.dropna(subset=columnas_obligatorias)
    gasto_limpio = gasto_limpio.drop_duplicates() 

    return gasto_limpio