import pandas as pd

# 1. Cambia 'generar_gastos' por 'generar_gasto' (quítale la s)
from utils.simulacion_gasto import generar_gasto

# 2. Úsala también en singular
gastos = generar_gasto(100)

# 3. Convierte a DataFrame y muestra
gastos_ordenados = pd.DataFrame(gastos)
print(gastos_ordenados)