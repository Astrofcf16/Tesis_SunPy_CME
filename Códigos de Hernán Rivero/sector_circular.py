import numpy as np
import matplotlib.pyplot as plt
import sunpy.map
from sunpy.data.sample import AIA_171_IMAGE
from scipy.ndimage import map_coordinates

# Cargar imagen de ejemplo del Sol
aia_map = sunpy.map.Map(AIA_171_IMAGE)

# Convertir datos a escala logarítmica para mejor contraste
data = np.log10(aia_map.data - np.min(aia_map.data) + 1)

# Definir el sector angular a extraer (en grados)
theta_min, theta_max = 0, 5  # Ángulo del sector
num_r = data.shape[0] // 2  # Radio máximo
num_theta = 100  # Resolución angular

# Crear malla en coordenadas polares
r = np.linspace(0, num_r, num_r)
theta = np.linspace(np.radians(theta_min), np.radians(theta_max), num_theta)
theta_grid, r_grid = np.meshgrid(theta, r)

# Convertir de polar a cartesiano
X = (r_grid * np.cos(theta_grid)).astype(int) + data.shape[1] // 2
Y = (r_grid * np.sin(theta_grid)).astype(int) + data.shape[0] // 2

# Extraer valores del sector
sector_data = np.full((num_r, num_theta), np.nan)  # Fondo vacío
valid_mask = (X >= 0) & (X < data.shape[1]) & (Y >= 0) & (Y < data.shape[0])
sector_data[valid_mask] = data[Y[valid_mask], X[valid_mask]]

# Transformar a coordenadas cartesianas (rectangulares)
sector_cartesian = map_coordinates(data, [Y.ravel(), X.ravel()], order=1).reshape(num_r, num_theta)

# Crear la figura con dos subgráficos
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# --- Primera ventana: Proyección Polar ---
ax1 = fig.add_subplot(121, projection='polar')
ax1.pcolormesh(theta_grid, r_grid, sector_data, cmap="gray", shading='auto')
ax1.set_ylim(num_r * 0.4, num_r)  # Ajustar el zoom
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_title("Proyección Polar")

# --- Segunda ventana: Proyección Rectangular ---
ax2 = axes[1]
ax2.imshow(sector_cartesian, aspect='auto', cmap="gray", extent=[theta_min, theta_max, 0, num_r])
ax2.set_xlabel("Ángulo (grados)")
ax2.set_ylabel("Radio (pixeles)")
ax2.set_title("Proyección Rectangular")

# Mostrar la figura con ambas ventanas
plt.tight_layout()
plt.show()