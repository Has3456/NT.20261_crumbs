import random


def generar_gasto(numero_gastos):
    """
    Genera una lista de gastos simulados con errores controlados,
    compatible con el endpoint real http://localhost:8080/api/v1/gastos.
    """
    fechas = ["2026-01-15", "2026-02-20", "2026-03-10", "2026-04-05", "2026-05-05"]
    valores = [50000, 100000, 200000, 500000, 100000, 150000, 250000, 300000, 400000]
    tipos_necesidad = [
        "Alimentación", "Transporte", "Vivienda", "Salud", "Educación",
        "Entretenimiento", "Ropa", "Tecnología", "Viajes",
    ]
    frecuencias = ["Diaria", "Semanal", "Mensual", "Anual"]
    lugares = [
        "Supermercado", "Restaurante", "Gasolinera", "Tienda de ropa",
        "Farmacia", "Cine", "Librería", "Centro comercial", "Agencia de viajes",
    ]
    medios = [
        "Efectivo", "Tarjeta de crédito",
        "Transferencia bancaria", "Pago móvil", "Cheque",
    ]
    grados = ["Alta", "Media", "Baja"]
    descripciones = [
        "Compra de alimentos", "Pago de transporte público", "Alquiler mensual",
        "Consulta médica", "Matrícula escolar", "Entrada de cine",
        "Compra de ropa", "Compra de gadgets", "Reserva de hotel",
    ]

    gastos = []
    for _ in range(numero_gastos):
        gasto = {
            "id": random.randint(1, 1000),
            "fecha": random.choice(fechas),
            "valor": random.choice(valores),
            "tipo_necesidad": random.choice(tipos_necesidad),
            "frecuencia_gasto": random.choice(frecuencias),
            "lugar_consumo": random.choice(lugares),
            "medio_verificacion": random.choice(medios),
            "grado_necesidad": random.choice(grados),
            "descripcion": random.choice(descripciones),
            "id_cliente": random.randint(1, 10),
        }

        # Inyección de errores controlados
        probabilidad = random.random()
        if probabilidad < 0.10:
            gasto["id"] = random.choice([None, -1, 0])
            gasto["valor"] = random.randint(-5000, -1)
        elif probabilidad < 0.3:
            gasto["grado_necesidad"] = random.choice(
                [None, "", "superflua", "esencial", "innecesaria"]
            )
            gasto["descripcion"] = " " + gasto["descripcion"] + " "
            gasto["medio_verificacion"] = random.choice(
                [None, "", "Pago en especie", "Trueque"]
            )
        elif probabilidad < 0.6:
            gasto["fecha"] = "2020-02-31"
            gasto["tipo_necesidad"] = None
            gasto["lugar_consumo"] = gasto["lugar_consumo"].upper()
            gasto["frecuencia_gasto"] = random.choice(
                [None, "", "cada minuto", "cada hora"]
            )

        gastos.append(gasto)

    return gastos
