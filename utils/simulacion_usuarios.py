import random


def generar_usuario(numero_usuarios):
    """
    Genera una lista de usuarios simulados con errores controlados,
    compatible con el endpoint real http://localhost:8080/api/v1/usuarios.
    """
    nombres = [
        "juan Fernando Gallego", "Maria Jose Perez",
        "Carlos Mario Sanchez", "Ana Gomez", "Luis Rodriguez",
    ]
    tipos_documento = ["CC", "TI", "CE", "PP"]
    documentos = ["123456789", "987654321", "456789123", "321654987", "654321789"]
    ocupaciones = ["Estudiante", "Empleado", "Desempleado", "Independiente", "Jubilado"]
    niveles = ["Bajo", "Medio", "Alto", "Muy Alto", "medio"]
    rangos_ingresos = ["1700000", "2600000", "2100000", "3800000", "2500000"]
    ubicaciones = ["Girardot", "Medellin", "la doctora", "Sabaneta", "San Antonio de prado"]
    generos = ["Masculino", "Femenino", "masculino", "femenino"]
    ids_gastos = list(range(1, 11))

    usuarios = []
    for _ in range(numero_usuarios):
        usuario = {
            "id": random.randint(1, 1000),
            "nombre": random.choice(nombres),
            "tipo_documento": random.choice(tipos_documento),
            "documento": random.choice(documentos),
            "ocupacion_principal": random.choice(ocupaciones),
            "nivel_socioeconomico": random.choice(niveles),
            "rango_ingresos_mensuales": random.choice(rangos_ingresos),
            "ubicacion_geografica": random.choice(ubicaciones),
            "genero": random.choice(generos),
            "edad": random.randint(15, 80),
            "id_gastos": random.choice(ids_gastos),
        }

        # Inyección de errores controlados
        probabilidad = random.random()
        if probabilidad < 0.1:
            usuario["id"] = random.choice([None, -1, 0])
            usuario["edad"] = random.choice([None, -5, -30])
        elif probabilidad < 0.3:
            usuario["nombre"] = usuario["nombre"].upper()
            usuario["tipo_documento"] = random.choice([None, "", "   "])
        elif probabilidad < 0.6:
            usuario["documento"] = random.choice([None, "", "   "])
            usuario["ocupacion_principal"] = random.choice([None, "", "   "])
        elif probabilidad < 0.9:
            usuario["nivel_socioeconomico"] = random.choice([None, "", "   "])
            usuario["rango_ingresos_mensuales"] = random.choice([None, 0, ""])

        usuarios.append(usuario)

    return usuarios
