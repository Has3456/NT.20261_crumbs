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
    
    edad = [19, 25, 28, 38, 50]

    idGastos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



    usuarios = []
    for i in range(numero_usuarios):
        usuario = {
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
        usuarios.append(usuario)   
    return usuarios 
        