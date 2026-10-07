# Cinemática y estimación volumétrica de una CME tipo halo con SunPy

Tesis de Licenciatura en Física — Universidad Nacional Mayor de San Marcos (UNMSM)
**Autor:** Steve Nina Cutipa · [ORCID 0000-0001-8197-8665](https://orcid.org/0000-0001-8197-8665)
**Asesor:** Lic. Walter Guevara Day — Grupo de Investigación en Astronomía, Facultad de Ciencias Físicas

## Descripción

Análisis cinemático y volumétrico de la eyección de masa coronal (CME) tipo halo del **17 de diciembre de 2024**, a partir de imágenes de los coronógrafos **SOHO/LASCO C2 y C3**, procesadas en Python con **SunPy** y **Astropy**.

El flujo de trabajo:

1. Descarga las imágenes FITS desde el Virtual Solar Observatory con `Fido` (SunPy).
2. Procesa las imágenes por diferencia corrida y detecta el frente de la CME dentro de un sector angular, con control de calidad visual de cada cuadro.
3. Construye el diagrama **altura–tiempo (h vs t)** por dos métodos: automático y manual.
4. Ajusta modelos cinemáticos lineal y cuadrático por mínimos cuadrados ponderados para obtener la velocidad y la aceleración.
5. Estima el **volumen de la CME en función del tiempo** con el modelo de cono (sector esférico), V(t) = (2π/3) R³(t) (1 − cos θ), y lo compara con la aproximación esférica.

## Resultado principal

![Diagrama altura–tiempo con ajustes lineal y cuadrático](Cuadernos%20Jupyter%20para%20tesis/Resultados%20obtenidos%20%28al%20ejecutar%20los%20cuadernos%29/fig1_ht_ajustes.png)

| Ajuste (serie manual) | Resultado |
|---|---|
| Lineal | v = 1942 km/s |
| Cuadrático | v₀ = 2509 km/s, a = −152 m/s² (la CME se desacelera) |

Las alturas son proyectadas en el plano del cielo. En una CME halo representan una cota inferior de las alturas reales.

## Estructura del repositorio

| Carpeta / archivo | Contenido |
|---|---|
| `Cuadernos Jupyter para tesis/01_descargar_evento1.ipynb` | Descarga de imágenes LASCO C2 y C3 con SunPy (Fido) |
| `Cuadernos Jupyter para tesis/02_procesar_evento1.ipynb` | Procesamiento de imágenes y diagrama h–t automático |
| `Cuadernos Jupyter para tesis/03_grafica_manual_evento1.ipynb` | Diagrama h–t a partir de mediciones manuales |
| `Cuadernos Jupyter para tesis/04_cinematica_volumen_evento1.ipynb` | Ajuste cinemático y estimación del volumen |
| `Cuadernos Jupyter para tesis/Resultados obtenidos (al ejecutar los cuadernos)/` | Figuras, tablas CSV y control de calidad (C2 y C3) |
| `Informe pasado 19-06-25/` | Informe de avance (junio 2025) con scripts y figuras del análisis de los eventos 1 y 2 |

## Requisitos

- Python 3.11
- SunPy, Astropy, NumPy, SciPy, Matplotlib

```bash
pip install sunpy astropy numpy scipy matplotlib
```

Los cuadernos se ejecutan en orden (01 → 04). Los archivos FITS no se incluyen por su tamaño; el cuaderno 01 los descarga.
