import numpy as np
import matplotlib.pyplot as plt
import sunpy.map

# Cargar las imágenes LASCO
my_maps = sunpy.map.Map("c:/walter_asesoria/steve_nina/lascoc2")

# Hacer diferencia
data_diff = my_maps[1].data - my_maps[0].data
diff_map = sunpy.map.Map(data_diff, my_maps[0].meta)

# --------- Parámetros para extracción del sector ---------
theta_min, theta_max = 270, 275
num_r = 1024
num_theta = 179

# Crear malla polar para extracción
r = np.linspace(0, diff_map.data.shape[0] // 2, num_r)
theta = np.linspace(np.radians(theta_min), np.radians(theta_max), num_theta)

# Convertir polar -> cartesiano
X = (r[:, None] * np.cos(theta)).astype(int) + diff_map.data.shape[1] // 2
Y = (r[:, None] * np.sin(theta)).astype(int) + diff_map.data.shape[0] // 2

# Extraer datos
sector_data = np.full((num_r, num_theta), np.nan)
valid_mask = (X >= 0) & (X < diff_map.data.shape[1]) & (Y >= 0) & (Y < diff_map.data.shape[0])
sector_data[valid_mask] = data_diff[Y[valid_mask], X[valid_mask]]

# --------- Visualización ---------
plt.figure(figsize=(6, 12))  # Ajuste para que el alto sea más notorio
plt.imshow(sector_data, cmap='gray', origin='lower', aspect='equal')
plt.axis('off')
plt.title("Imagen transformada (1024x179)")
plt.show()