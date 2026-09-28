import numpy as np
import matplotlib.pyplot as plt
import sunpy.map

# Cargar las imágenes LASCO
my_maps = sunpy.map.Map("c:/walter_asesoria/steve_nina/lascoc2")

# Hacer diferencia
data_diff = my_maps[1].data - my_maps[0].data
diff_map = sunpy.map.Map(data_diff, my_maps[0].meta)

# --------- Parámetros para extracción del sector ---------
theta_min, theta_max = 270, 275  # 270° a 275°
num_r = 1024  # Radial
num_theta = 179  # Angular divisiones

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

# --------- Visualización comparativa ---------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Imagen rectangular transpuesta
c1 = ax1.imshow(sector_data, cmap='gray', aspect='auto')
ax1.set_title('Imagen rectangular')
ax1.axis('off')
plt.colorbar(c1, ax=ax1, orientation='horizontal')

# Imagen polar
ax2 = plt.subplot(122, projection='polar')
theta_polar = np.linspace(np.radians(theta_min), np.radians(theta_max), num_theta)
r_polar = np.arange(num_r)
theta_grid_polar, r_grid_polar = np.meshgrid(theta_polar, r_polar)
c2 = ax2.pcolormesh(theta_grid_polar, r_grid_polar, sector_data, cmap='gray', shading='auto')
ax2.set_title('Imagen en coordenadas polares')
ax2.set_xticks([])
ax2.set_yticks([])
ax2.grid(False)
plt.colorbar(c2, ax=ax2, orientation='horizontal')

plt.tight_layout()
plt.show()