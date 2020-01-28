import numpy as np

import matplotlib.pyplot as plt
import poliastro.plotting as plotting

from astropy import units as u

from poliastro.bodies import Earth, Mars, Sun
from poliastro.twobody import Orbit

plt.style.use("seaborn")  

# Definim cada orbita on:
	
	#r: vector posició en coord cartesianes

	#v: vector velocitat en coord cartesianes

# o tambe les podem definir amb les seves caracteristiques:
	
	# a: semieix major
	# ecc: excentricitat
	# inc: inclinacio respecte la horizontal(sera 0 en totes les orbites 
	# 	ja que es troben en el mateix pla per guio del treball)
	# raan: inclinacio respecte la vertical
	# argp: argument del periheli
	# nu: posicio punt 

a = 6571000 * u.m
ecc = 0  * u.one
inc = 0 * u.deg
raan = 0 * u.deg
argp = 0 * u.deg
nu = 0 * u.deg

Terra = Orbit.from_classical(Sun, a, ecc, inc, raan, argp, nu)

r = [6571000, 0, 0] * u.m
v = [0,5984.96 + 61734.8 , 0] * u.m / u.s

hiperbola = Orbit.from_vectors(Earth, r, v)

# Creem la grafica on representarem les diferents orbites

fig, ax = plt.subplots()

ax.grid(True)
ax.set_title("Hipèrbola sortida de la Terra")

ax.set_facecolor('None')


# Representem les orbites que hem definit previament

plotter = plotting.OrbitPlotter(ax)

plotter.plot(hiperbola, label="hipèrbola")

plt.show()