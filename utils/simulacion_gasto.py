import random

def generar_gasto(numeroGastos):

    # Listas de datos para generar gastos aleatorios
    
    fecha=["2026-01-15", "2026-02-20", "2026-03-10", "2026-04-05", "2026-05-05"]
           
    valor=[50000, 100000, 200000, 500000, 100000, 150000, 250000, 300000, 400000]

    tipoNecesidad=["Alimentación", "Transporte", "Vivienda", "Salud", "Educación", 
                   "Entretenimiento", "Ropa", "Tecnología", "Viajes"]


    frecuenciaGasto=["Diario", "Semanal", "Mensual", "Anual"]


    lugarConsumo=["Supermercado", "Restaurante", "Gasolinera", "Tienda de ropa", "Farmacia", 
                  "Cine", "Librería", "Centro comercial", "Agencia de viajes" ]
    

    medioVerificacion=["Efectivo", "Tarjeta de crédito", "Transferencia bancaria", 
                       "Pago móvil", "Cheque"]
    
    
    gradoNecesidad=["Alta", "Media", "Baja"]

    
    Descripcion=["Compra de alimentos", "Pago de transporte público", "Alquiler mensual", 
                 "Consulta médica", "Matrícula escolar", "Entrada de cine",
                 "Compra de ropa", "Compra de gadgets", "Reserva de hotel"]
    
    
 

    # Generar gastos aleatorios

    gastos = []

    for i in range (numeroGastos):
        gasto = {
            "id": random.randint(1, 1000),
            "Fecha": random.choice(fecha),
            "Valor": random.choice(valor),
            "Tipo de Necesidad": random.choice(tipoNecesidad),
            "Frecuencia del Gasto": random.choice(frecuenciaGasto),
            "Lugar de Consumo": random.choice(lugarConsumo),
            "Medio de Verificación": random.choice(medioVerificacion),
            "Grado de Necesidad": random.choice(gradoNecesidad),
            "Descripción": random.choice(Descripcion),
<<<<<<< HEAD:utils/simulacion_gasto.py
            "id_cliente": random.randint(1, 10)
=======
            "id_cliente": random.choice(id_cliente)
            
>>>>>>> a0bf210ff7591bb13efc65b46fc1e12ec5cd5759:simulacion_gasto.py
        }

# Agregar el gasto generado a la lista de gastos
        gastos.append(gasto)

    return gastos
    
    
   


