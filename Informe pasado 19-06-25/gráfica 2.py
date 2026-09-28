import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from datetime import datetime
import numpy as np

# Centro del disco solar en la imagen LASCO
x0, y0 = 512, 512
escala_C2 = 179  # px/R☉ (LASCO C2)

# === Datos del evento 2 (04/04/2024) - Solo LASCO C2 ===
c2_event2_data = [
    {"time": "2024-04-04 20:24:05", "col": 323.0, "row": 342.0, "angle": 322.6, "altura_rsun": 2.76},
    {"time": "2024-04-04 20:36:05", "col": 324.0, "row": 361.0, "angle": 327.4, "altura_rsun": 3.16},
    {"time": "2024-04-04 20:56:53", "col": 342.0, "row": 401.0, "angle": 329.5, "altura_rsun": 4.23},
]

# Procesar los datos
t_c2 = [datetime.strptime(d["time"], "%Y-%m-%d %H:%M:%S") for d in c2_event2_data]
h_c2 = [d["altura_rsun"] for d in c2_event2_data]
a_c2 = [d["angle"] for d in c2_event2_data]

# Graficar
plt.figure(figsize=(10, 6))
sc = plt.scatter(t_c2, h_c2, c=a_c2, cmap='plasma', s=100, marker='o', label="LASCO C2 (179 px/𝑅☉)")

# Barra de color
cbar = plt.colorbar(sc)
cbar.set_label("Ángulo de propagación (°)")

# Estética
plt.xlabel("Hora UTC")
plt.ylabel("Altura radial H (𝑅☉)")
plt.title("Evento CME – 04/04/2024 – Diagrama H vs t con ángulo de propagación")
plt.grid(True)
plt.legend()
plt.gca().xaxis.set_major_formatter(DateFormatter("%H:%M"))
plt.tight_layout()
plt.gcf().autofmt_xdate()

# Mostrar
plt.show()

