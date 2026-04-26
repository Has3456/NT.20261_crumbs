#simulacion de datos de ususrio

import random

def generar_ususario(numero_usuarios):

    listaNombres = ["juan Fernando Gallego", "Maria JosePerez", "Carlos Mario Sanchez", "Ana Gomez", "Luis Rodriguez"]

    listaTipoDocumento = ["CC", "TI", "CE", "PP"]

    listaDocumento = ["123456789", "987654321", "456789123", "321654987", "654321789"]

    listaOcupacionPrincipal = ["Estudiante", "Empleado", "Desempleado", "Independiente", "Jubilado"]

    nivelSocioeconomico = ["Bajo", "Medio", "Alto", "Muy Alto","medio"]

    rangoIngresosMensuales = ["1700000", "2600000", "2100000", "3800000", "2500000"]   

    ubicacionGeografica = ["Girardot", "Medellin", "la doctora","Sabaneta", "San Antonio de prado"] 

    listaGenero = ["Masculino", "Femenino", "masculino", "femenino", "masculino"]  
    
    idGastos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



    usuarios = []
    for i in range(numero_usuarios):
        usuario = {
            "id": random.randint(1, 1000),
            "nombre": random.choice(listaNombres),
            "tipo_documento": random.choice(listaTipoDocumento),
            "documento": random.choice(listaDocumento),
            "ocupacion_principal": random.choice(listaOcupacionPrincipal),
            "nivel_socioeconomico": random.choice(nivelSocioeconomico),
            "rango_ingresos_mensuales": random.choice(rangoIngresosMensuales),
            "ubicacion_geografica": random.choice(ubicacionGeografica),
            "genero": random.choice(listaGenero),
            "edad": random.randint(15, 80),
            "id_gastos": random.choice(idGastos)
  
        }

        #Inyectar errores controlados 
        probabilidadError = random.random()

        if probabilidadError < 0.1: 
            usuario["id"] = random.choice([])  # ID fuera del rango esperado
        elif probabilidadError < 0.3:
            pass
        elif probabilidadError < 0.6:
            pass
        elif probabilidadError < 0.9:
            pass
            # 10% de probabilidad de error
        
        usuarios.append(usuario)   
    return usuarios 
        