#lascomap02

import matplotlib.pyplot as plt
import numpy as np
import astropy.units as u

from astropy.coordinates import SkyCoord
from sunpy.map import Map
from sunpy.net import attrs as a

#Convertimos el archivo fts en mapa
lascomapc2 = Map('22375023.fts')
lascomapc3 = Map('32262248.fts')


fig = plt.figure(figsize=(10,4))
ax1 = fig.add_subplot(121, projection=lascomapc2)
lascomapc2.plot(axes=ax1)

ax2 = fig.add_subplot(122, projection=lascomapc3)
ax2 = fig.add_subplot(122, projection=lascomapc3)
lascomapc3.plot(axes=ax2)

plt.show()