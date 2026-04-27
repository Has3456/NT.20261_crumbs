import pandas as pd

def limpia_simulacion(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    #rutina para evaluar textos
    #seleccionar todas las columnas de tipo texto y poner todo en minuscula 
    columnas_textos =["nombre","tipo_documento","documento","ocupacion_principal","nivel_socioeconomico","rango_ingresos_mensuales","ubicacion_geografica","genero"]
    for columna in columnas_textos:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip().str.lower()

    # Limpiar los textos solo con valores esperados
    nombre_esperado = ["juan fernando gallego", "maria jose perez", "carlos mario sanchez", "ana gomez", "luis rodriguez"]
    data_frame_limpio["nombre"]=data_frame_limpio["nombre"].where(
         data_frame_limpio["nombre"].isin(nombre_esperado),
         pd.NA
      )
    
    tipo_documento_esperado = ["cc", "ti", "ce", "pp"]
    data_frame_limpio["tipo_documento"]=data_frame_limpio["tipo_documento"].where(
        data_frame_limpio["tipo_documento"].isin(tipo_documento_esperado),
        pd.NA
    )

    documento_esperado= ["123456789", "987654321", "456789123", "321654987", "654321789"]
    data_frame_limpio["documento"]=data_frame_limpio["documento"].where(
        data_frame_limpio["documento"].isin(documento_esperado),
        pd.NA
     )
    
    ocupacion_principal_esperada = ["estudiante", "empleado", "desempleado", "independiente", "jubilado"]
    data_frame_limpio["ocupacion_principal"]=data_frame_limpio["ocupacion_principal"].where(
        data_frame_limpio["ocupacion_principal"].isin(ocupacion_principal_esperada),
        pd.NA   
        )
    nivel_socioeconomico_esperado = ["bajo", "medio", "alto", "muy alto"]
    data_frame_limpio["nivel_socioeconomico"]=data_frame_limpio["nivel_socioeconomico"].where(
        data_frame_limpio["nivel_socioeconomico"].isin(nivel_socioeconomico_esperado),
        pd.NA
    )
    rango_ingresos_mensuales_esperado = ["1700000", "2600000", "2100000", "3800000", "2500000"]
    data_frame_limpio["rango_ingresos_mensuales"]=data_frame_limpio["rango_ingresos_mensuales"].where(
        data_frame_limpio["rango_ingresos_mensuales"].isin(rango_ingresos_mensuales_esperado),
        pd.NA
    )
    ubicacion_geografica_esperada = ["girardot", "medellin", "la doctora", "sabaneta", "san antonio de prado"]
    data_frame_limpio["ubicacion_geografica"]=data_frame_limpio["ubicacion_geografica"].where(
        data_frame_limpio["ubicacion_geografica"].isin(ubicacion_geografica_esperada),
        pd.NA           
    )
    genero_esperado = ["masculino", "femenino"]
    data_frame_limpio["genero"]=data_frame_limpio["genero"].where(
        data_frame_limpio["genero"].isin(genero_esperado),              
        pd.NA
    )



    #Rutina para evaluar numeros 
    #evaluar  que la columna  numerica si son numeros 
    data_frame_limpio["id"]=pd.to_numeric(data_frame_limpio["id"])
    data_frame_limpio["edad"]=pd.to_numeric(data_frame_limpio["edad"])  
    data_frame_limpio["id_gastos"]=pd.to_numeric(data_frame_limpio["id_gastos"])    

   
    #evaluar solo valores numericos permitidos
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"] > 0]
    data_frame_limpio["edad"] = data_frame_limpio["edad"].astype(int)
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id_gastos"] > 0]


    #rutina para evaluar novedades 
    #rutina  para evaluara campos obligatorios  que vienen vacios 
    columna_obligatoria=["id","nombre","tipo_documento","documento","ocupacion_principal","nivel_socioeconomico","rango_ingresos_mensuales","ubicacion_geografica","genero","edad"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columna_obligatoria)

    data_frame_limpio=data_frame_limpio.drop_duplicates()

    return data_frame_limpio