

from tkinter import TRUE

import pandas as pd

from notebook.consumo import consumir_gastos, consumir_usuarios
from notebook.limpieza import limpiar_gastos, limpiar_usuarios
from notebook.transformacion import transformar_gastos, transformar_usuarios
from notebook.descripcion import describir_gastos, describir_usuarios
from notebook.graficacion import (
    graficar_barras,
    graficar_torta,
    graficar_lineas,
    graficar_mapa_calor,
)


USE_SIMULACION = True



def obtener_datos_gastos():
    if USE_SIMULACION:
        from utils.simulacion_gastos import generar_gasto
        return generar_gasto(100)
    return consumir_gastos()


def obtener_datos_usuarios():
    if USE_SIMULACION:
        from utils.simulacion_usuarios import generar_usuario
        return generar_usuario(100)
    return consumir_usuarios()


# ══════════════════════════════════════════════
#  PIPELINE DE GASTOS
# ══════════════════════════════════════════════

print("\n>>> Procesando GASTOS...")
datos_gastos = obtener_datos_gastos()
df_gastos = pd.DataFrame(datos_gastos)
df_gastos_limpio = limpiar_gastos(df_gastos)
describir_gastos(df_gastos_limpio)

agrupaciones_gastos = transformar_gastos(df_gastos_limpio)

# Gráfico de barras: total de valor por tipo de necesidad
graficar_barras(
    agrupaciones_gastos["agrupacion1"],
    columna_categorias="tipo_necesidad",
    columna_valores="total_valor",
    titulo="Total de valor gastado por tipo de necesidad",
    color_barras="#4CAF50",
    nombre_archivo="gastos_barras_tipo_necesidad.png",
)

# Gráfico de torta: distribución por frecuencia de gasto
graficar_torta(
    agrupaciones_gastos["agrupacion2"],
    columna_etiquetas="frecuencia_gasto",
    columna_valores="conteo",
    titulo="Distribución de gastos por frecuencia",
    nombre_archivo="gastos_torta_frecuencia.png",
)

# Mapa de calor: tipo de necesidad vs grado de necesidad
graficar_mapa_calor(
    agrupaciones_gastos["agrupacion3"],
    columna_filas="tipo_necesidad",
    columna_columnas="grado_necesidad",
    columna_valores="conteo",
    titulo="Cantidad de gastos: tipo vs grado de necesidad",
    paleta_color="YlOrRd",
    nombre_archivo="gastos_mapa_calor.png",
)



#  PIPELINE DE USUARIOS


print("\n>>> Procesando USUARIOS...")
datos_usuarios = obtener_datos_usuarios()
df_usuarios = pd.DataFrame(datos_usuarios)
df_usuarios_limpio = limpiar_usuarios(df_usuarios)
describir_usuarios(df_usuarios_limpio)

agrupaciones_usuarios = transformar_usuarios(df_usuarios_limpio)

# Gráfico de barras: conteo por ocupación principal
graficar_barras(
    agrupaciones_usuarios["agrupacion1"],
    columna_categorias="ocupacion_principal",
    columna_valores="conteo",
    titulo="Usuarios por ocupación principal",
    color_barras="#2196F3",
    nombre_archivo="usuarios_barras_ocupacion.png",
)

# Gráfico de torta: distribución por nivel socioeconómico
graficar_torta(
    agrupaciones_usuarios["agrupacion2"],
    columna_etiquetas="nivel_socioeconomico",
    columna_valores="conteo",
    titulo="Distribución por nivel socioeconómico",
    nombre_archivo="usuarios_torta_nivel.png",
)

# Mapa de calor: ubicación geográfica vs género
graficar_mapa_calor(
    agrupaciones_usuarios["agrupacion3"],
    columna_filas="ubicacion_geografica",
    columna_columnas="genero",
    columna_valores="conteo",
    titulo="Usuarios por ubicación geográfica y género",
    paleta_color="Blues",
    nombre_archivo="usuarios_mapa_calor.png",
)

print("\n✓ Pipeline completo. Revisa la carpeta 'graficos/' para ver las imágenes generadas.")
