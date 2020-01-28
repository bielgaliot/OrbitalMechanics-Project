import numpy as np
import matplotlib.pyplot as plt
import poliastro.plotting as plotting

from astropy import units as u

from poliastro.bodies import Earth, Mars, Sun, Jupiter
from poliastro.twobody import Orbit

plt.style.use("seaborn")  

 # Definim cada orbita on:
	
	#r: vector posició en coord cartesianes

	#v: vector velocitat en coord cartesianes

r = [353244470, 0, 0] * u.m
v = [0,27729.5 , 0] * u.m / u.s

hiperbola = Orbit.from_vectors(Jupiter, r, v)


# Creem la grafica on representarem les diferents orbites

fig, ax = plt.subplots()

ax.grid(True)
ax.set_facecolor('None')

# Representem les orbites que hem definit previament

plotter = plotting.OrbitPlotter(ax)

plotter.plot(hiperbola, label="hipèrbola")

plt.show()