#program lascomap03

import matplotlib.pyplot as plt
import numpy as np
import astropy.units as u
import sunpy.map

#Convertimos el archivo fts en mapa
lascomap = sunpy.map.Map('22375023.fts')

fig = plt.figure()
ax1 = fig.add_subplot(121, projection=lascomap)
lascomap.plot(axes=ax1)

ax2 = fig.add_subplot(122, projection=lascomap)
lascomap.plot(axes=ax2, clip_interval=(1,99.9)*u.percent)
lascomap.draw_limb()
ax2.coords[0].grid(draw_grid=False)
ax2.coords[1].grid(draw_grid=False)
 
plt.show()