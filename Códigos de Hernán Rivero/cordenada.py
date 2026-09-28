import sunpy.map
import matplotlib.pyplot as plt
import numpy as np
from sunpy.data.sample import AIA_171_IMAGE  # Imagen de ejemplo

# Cargar imagen AIA
aia_map = sunpy.map.Map(AIA_171_IMAGE)

# Aplicar escala logarítmica para mejorar el contraste
data_log = np.log10(aia_map.data - np.min(aia_map.data) + 1)  # Evita log(0)

# Crear la figura y el eje
fig, ax = plt.subplots(figsize=(8, 8))

# Dibujar la imagen con la escala ajustada (zorder=0 para que esté debajo)
ax.imshow(data_log, cmap="sdoaia171", origin="lower", zorder=0)

# Obtener el centro de la imagen
height, width = aia_map.data.shape
center_x, center_y = width // 2, height // 2
radius = min(center_x, center_y)  # Radio basado en el tamaño de la imagen

# Dibujar líneas radiales cada 5° (zorder=1 para que estén sobre la imagen)
for angle in np.arange(0, 360, 5):
    theta = np.radians(angle)
    x = [center_x, center_x + radius * np.cos(theta)]
    y = [center_y, center_y + radius * np.sin(theta)]
    ax.plot(x, y, color='red', linewidth=0.7, alpha=0.8, zorder=1)

# Ocultar ejes
ax.axis("off")

# Mostrar la imagen
plt.show()