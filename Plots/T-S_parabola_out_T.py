import numpy as np
import poliastro
import matplotlib.pyplot as plt
import poliastro.plotting as plotting

from astropy import units as u

from poliastro.bodies import Earth, Mars, Sun
from poliastro.twobody import Orbit

from astropy.coordinates import CartesianRepresentation

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





r = [13371000, 0, 0] * u.m
v = [0,7748.9 , 0] * u.m / u.s

hiperbola = Orbit.from_vectors(Earth, r, v)

# Creem la grafica on representarem les diferents orbites

fig, ax = plt.subplots()

ax.grid(True)
ax.set_title("Paràbola de sortida de la Terra")
ax.set_facecolor('None')

# Representem les orbites que hem definit previament

plotter = plotting.OrbitPlotter(ax)

plotter.plot(hiperbola, label="Paràbola")

plt.show()

