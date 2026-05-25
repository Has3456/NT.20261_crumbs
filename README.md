# Proyecto Integrador NT 2026-1

**Integrantes:** Laura Patricia Torres Contreras · Habbleybdy Castrillón Calle

---

## Descripción

Pipeline de análisis de datos en Python que consume dos endpoints de un backend **Spring Boot**,
aplica limpieza, transformación y genera gráficos automáticamente.

---

## Estructura del proyecto

```
proyecto_adaptado/
│
├── main.py                        # Punto de entrada: orquesta todo el pipeline
│
├── notebook/                      # Módulos del pipeline (estilo proyecto muestra)
│   ├── consumo.py                 # Consume los endpoints reales de Spring Boot
│   ├── limpieza.py                # Limpieza de datos (gastos y usuarios)
│   ├── transformacion.py          # Agrupaciones y filtros analíticos
│   ├── descripcion.py             # Estadísticas descriptivas del dataset
│   └── graficacion.py             # Generación de gráficos (barras, torta, líneas, mapa de calor)
│
├── utils/                         # Utilidades de apoyo
│   ├── simulacion_gastos.py       # Generador local de datos de gastos (modo sin backend)
│   └── simulacion_usuarios.py     # Generador local de datos de usuarios (modo sin backend)
│
├── graficos/                      # Carpeta de salida de imágenes (se crea automáticamente)
│
├── requirements.txt
└── README.md
```

---

## Endpoints consumidos

| Endpoint Java (`@RequestMapping`) | URL en ejecución |
|---|---|
| `api/v1/gastos` | `http://localhost:8080/api/v1/gastos` |
| `api/v1/usuarios` | `http://localhost:8080/api/v1/usuarios` |

---

## Cómo ejecutar

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Con el backend Spring Boot activo
Asegúrate de que tu aplicación Java esté corriendo en el puerto 8080, luego:
```bash
python main.py
```

### 3. Sin el backend (modo simulación local)
Abre `main.py` y cambia la línea:
```python
USE_SIMULACION = False
```
por:
```python
USE_SIMULACION = True
```
Luego ejecuta normalmente con `python main.py`.

---

## Gráficos generados

Todos los gráficos se guardan en la carpeta `graficos/` automáticamente.

| Archivo | Descripción |
|---|---|
| `gastos_barras_tipo_necesidad.png` | Total de valor gastado por tipo de necesidad |
| `gastos_torta_frecuencia.png` | Distribución de gastos por frecuencia |
| `gastos_mapa_calor.png` | Cruce tipo de necesidad vs grado de necesidad |
| `usuarios_barras_ocupacion.png` | Conteo de usuarios por ocupación principal |
| `usuarios_torta_nivel.png` | Distribución por nivel socioeconómico |
| `usuarios_mapa_calor.png` | Cruce ubicación geográfica vs género |
