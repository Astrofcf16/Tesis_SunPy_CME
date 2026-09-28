from sunpy.net import Fido, attrs as a
from sunpy.time import parse_time
import astropy.units as u
import os

# Definir intervalo de tiempo del Evento 2
inicio = parse_time("2024-04-04 20:20")
fin = parse_time("2024-04-04 21:00")

# Directorios de destino
carpeta_c2 = "/home/steve/lasco_evento2/c2"
carpeta_c3 = "/home/steve/lasco_evento2/c3"
os.makedirs(carpeta_c2, exist_ok=True)
os.makedirs(carpeta_c3, exist_ok=True)

# Descargar imágenes LASCO C2
print("🔽 Buscando imágenes LASCO C2...")
result_c2 = Fido.search(a.Time(inicio, fin),
                        a.Instrument.lasco,
                        a.Detector.c2,
                        a.Sample(12 * u.minute))  # intervalos más pequeños por tiempo corto

print(f"🔎 Se encontraron {len(result_c2[0])} imágenes C2")
files_c2 = Fido.fetch(result_c2, path=os.path.join(carpeta_c2, "{file}"))

# Descargar imágenes LASCO C3
print("\n🔽 Buscando imágenes LASCO C3...")
result_c3 = Fido.search(a.Time(inicio, fin),
                        a.Instrument.lasco,
                        a.Detector.c3,
                        a.Sample(12 * u.minute))

print(f"🔎 Se encontraron {len(result_c3[0])} imágenes C3")
files_c3 = Fido.fetch(result_c3, path=os.path.join(carpeta_c3, "{file}"))


