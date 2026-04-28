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
            "fecha": random.choice(fecha),
            "valor": random.choice(valor),
            "tipo_necesidad": random.choice(tipoNecesidad),
            "frecuencia_gasto": random.choice(frecuenciaGasto),
            "lugar_consumo": random.choice(lugarConsumo),
            "medio_verificación": random.choice(medioVerificacion),
            "grado_necesidad": random.choice(gradoNecesidad),
            "descripción": random.choice(Descripcion),
            "id_cliente": random.randint(1, 10)
        }


        #inyectando errores 
        probabilidadError = random.random()

        if probabilidadError < 0.10:
            gasto["id"] = random.choice([None, -1, 0])
            gasto["valor"]= None
            gasto["valor"] = random.randint(-5000, -1)  

        elif probabilidadError < 0.3:  
           gasto["grado_necesidad"] = "Inexistente"
           gasto["descripción"] = " " + gasto["descripción"] + " "
           gasto["medio_verificación"] = random.choice([None, "", "Pago en especie", "Trueque", "Intercambio de bienes", "monedas de oro" ])
           gasto["grado_necesidad"] = random.choice([None, "", "superflua", "esencial", "innecesaria", "prescindible"])

        elif probabilidadError < 0.6:  
           gasto["fecha"] = "2020-02-31" 
           gasto["tipo_necesidad"] = None
           gasto["lugar_consumo"] = gasto["lugar_consumo"].upper()
           gasto["frecuencia_gasto"] = random.choice([None, "", "cada minuto", "cada hora", "cada segundo"])

        elif probabilidadError < 0.9:  
            pass


    # Agregar el gasto generado a la lista de gastos
        gastos.append(gasto)

    return gastos
    
    
   


