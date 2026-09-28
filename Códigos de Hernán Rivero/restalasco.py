#pro restalasco

import matplotlib.pyplot as plt
import sunpy.map

# Cargar los archivos
arch01 = '22936562.fts'
arch02 = '22936563.fts'

# Cargar los mapas solares
lascomap1 = sunpy.map.Map(arch01)
lascomap2 = sunpy.map.Map(arch02)

# Restar los datos de los mapas
data_difference = lascomap2.data - lascomap1.data

# Crear un nuevo mapa a partir de los datos resultantes
difference_map = sunpy.map.Map(data_difference, lascomap1.meta)

# Mostrar el resultado
plt.figure()
difference_map.plot()
plt.colorbar()
plt.title("Diferencia entre Mapas Solares")
plt.show()

#end restalasco