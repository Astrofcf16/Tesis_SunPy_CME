import numpy as np
import matplotlib.pyplot as plt
import sunpy.map
from sunpy.data.sample import AIA_171_IMAGE
from scipy.ndimage import map_coordinates

# Cargar imagen de ejemplo del sol
aia_map = sunpy.map.Map(AIA_171_IMAGE)

# Convertir datos a escala logarítmica para mejor contraste
data = np.log10(aia_map.data - np.min(aia_map.data) + 1)

# Definir el sector angular a extraer (en grados)
theta_min, theta_max = 0, 5  # Ejemplo: 0° a 5°
num_r = data.shape[0] // 2  # Radio máximo
num_theta = 72  # Número de divisiones angulares

# Crear la malla de coordenadas en polares
r = np.linspace(0, num_r, num_r)
theta = np.linspace(np.radians(theta_min), np.radians(theta_max), num_theta)

# Convertir de polar a cartesiano
X = (r[:, None] * np.cos(theta)).astype(int) + data.shape[1] // 2
Y = (r[:, None] * np.sin(theta)).astype(int) + data.shape[0] // 2

# Extraer los valores de la imagen
sector_data = map_coordinates(data, [Y.ravel(), X.ravel()], order=1).reshape(num_r, num_theta)

# Mostrar la imagen transformada de polar a cartesiano
plt.figure(figsize=(8, 6))
plt.imshow(sector_data, aspect='auto', cmap="gray", extent=[theta_min, theta_max, 0, num_r])
plt.xlabel("Ángulo (°)")
plt.ylabel("Altura (píxeles)")
plt.title("Transformación de sector polar a cartesiano")
plt.colorbar(label="Intensidad")
plt.show()