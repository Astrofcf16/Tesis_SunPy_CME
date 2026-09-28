import matplotlib.pyplot as plt
import numpy as np
import astropy.units as u
from astropy.coordinates import SkyCoord

from sunpy.map import Map
from sunpy.map.maputils import all_coordinates_from_map
from sunpy.net import Fido
from sunpy.net import attrs as a

result = Fido.search(a.Time('2011/06/07 06:30', \
'2011/06/07 06:36'), a.Instrument.lasco, a.Detector.c2)

archivo = Fido.fetch(result, path = '\Walter_asesoria')
lasco_map = Map(archivo)