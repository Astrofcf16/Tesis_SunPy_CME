import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from datetime import datetime
import numpy as np

# Centro del disco solar en la imagen LASCO
x0, y0 = 512, 512

# Escalas de conversión (píxeles por radio solar)
escala_C2 = 179
escala_C3 = 56

# === Datos de LASCO C2 (ya incluyen altura en R☉) ===
c2_data = [
    {"time": "2024-12-17 16:00:05", "col": 258.0, "row": 131.0, "angle": 181.4, "altura_rsun": 2.97},
    {"time": "2024-12-17 16:12:05", "col": 226.0, "row": 14.0,   "angle": 173.1, "altura_rsun": 5.83},
]

# === Datos de LASCO C3 (requieren conversión a R☉) ===
c3_data = [
    {"time": "2024-12-17 16:18:06", "col": 261.0, "row": 204.0, "angle": 181.7},
    {"time": "2024-12-17 16:30:05", "col": 260.0, "row": 185.0, "angle": 180.6},
    {"time": "2024-12-17 16:42:05", "col": 258.0, "row": 164.0, "angle": 179.4},
    {"time": "2024-12-17 16:54:05", "col": 255.0, "row": 147.0, "angle": 178.0},
    {"time": "2024-12-17 17:06:05", "col": 249.0, "row": 131.0, "angle": 175.7},
    {"time": "2024-12-17 17:18:05", "col": 250.0, "row": 116.0, "angle": 176.5},
    {"time": "2024-12-17 17:30:06", "col": 251.0, "row": 100.0, "angle": 177.2},
    {"time": "2024-12-17 17:42:05", "col": 249.0, "row": 88.0,  "angle": 176.8},
    {"time": "2024-12-17 17:54:05", "col": 246.0, "row": 72.0,  "angle": 176.1},
    {"time": "2024-12-17 18:06:05", "col": 243.0, "row": 58.0,  "angle": 175.6},
    {"time": "2024-12-17 18:18:06", "col": 239.0, "row": 42.0,  "angle": 174.9},
    {"time": "2024-12-17 18:30:05", "col": 238.0, "row": 30.0,  "angle": 174.9},
]

# === Procesar datos de C2 ===
t_c2 = [datetime.strptime(d["time"], "%Y-%m-%d %H:%M:%S") for d in c2_data]
h_c2 = [d["altura_rsun"] for d in c2_data]
a_c2 = [d["angle"] for d in c2_data]

# === Procesar datos de C3 (convertir a radios solares) ===
t_c3, h_c3, a_c3 = [], [], []
for d in c3_data:
    t = datetime.strptime(d["time"], "%Y-%m-%d %H:%M:%S")
    dx = d["col"] - x0
    dy = d["row"] - y0
    altura = np.sqrt(dx**2 + dy**2) / escala_C3
    t_c3.append(t)
    h_c3.append(altura)
    a_c3.append(d["angle"])

# === Crear la figura ===
plt.figure(figsize=(10, 6))

# Graficar LASCO C2 con color según ángulo
sc1 = plt.scatter(t_c2, h_c2, c=a_c2, cmap='plasma', s=100, marker='o', label="LASCO C2 (179 px/𝑅☉)")

# Graficar LASCO C3 con color según ángulo
sc2 = plt.scatter(t_c3, h_c3, c=a_c3, cmap='plasma', s=100, marker='s', label="LASCO C3 (56 px/𝑅☉)")

# Barra de color (ángulo)
cbar = plt.colorbar(sc2)
cbar.set_label("Ángulo de propagación (°)")

# Estética de la gráfica
plt.xlabel("Hora UTC")
plt.ylabel("Altura radial H (𝑅☉)")
plt.title("Evento CME – 17/12/2024 – Diagrama H vs t con ángulo de propagación")
plt.grid(True)
plt.legend()
plt.gca().xaxis.set_major_formatter(DateFormatter("%H:%M"))
plt.tight_layout()
plt.gcf().autofmt_xdate()

# Mostrar
plt.show()

