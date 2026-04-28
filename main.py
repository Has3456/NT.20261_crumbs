import pandas as pd


from notebooks.limpiezaUsuario import limpia_simulacion
from utils.simulacion_usuario import generar_ususario
usuarios = generar_ususario(100)
usuarios_ordenados = pd.DataFrame(usuarios)
usuarios_limpio = limpia_simulacion(usuarios_ordenados)
print(usuarios_limpio)


from utils.simulacion_gasto import generar_gasto
from notebooks.limpiezaGasto import limpiar_gasto
gastos = generar_gasto(10)
gastos_ordenados = pd.DataFrame(gastos)
gastos_limpio = limpiar_gasto(gastos_ordenados)
print(gastos_limpio)