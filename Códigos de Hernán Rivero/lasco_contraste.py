import matplotlib.pyplot as plt
import sunpy.map
import astropy.units as u

my_maps = sunpy.map.Map("c:/walter_asesoria/steve_nina/lascoc2")

data_diff = my_maps[1].data - my_maps[0].data
diff_map = sunpy.map.Map(data_diff, my_maps[0].meta)

fig = plt.figure()
ax = fig.add_subplot(projection = diff_map)
diff_map.plot(cmap = 'grey', vmin = 0, vmax = 2000)
plt.colorbar()
plt.show()