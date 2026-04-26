import pandas as pd

# 1. Importar tal cual la estructura de carpetas
from utils.simulacion_gasto import generar_gasto
from utils.simulacion_usuario import generar_ususario

# 2. Generar la data de usuarios (lo que Lau hizo con probabilidades)
# Usamos 100 para que el DataFrame tenga buen volumen
usuarios = generar_ususario(100)

# 3. Convertir a DataFrame (Estructura de la imagen)
usuarios_ordenados = pd.DataFrame(usuarios)

# 4. Mostrar el resultado
print(usuarios_ordenados)