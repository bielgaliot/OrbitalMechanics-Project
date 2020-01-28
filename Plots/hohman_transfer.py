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

r = [1, 0, 0] * u.AU
v = [0,40.07839651 , 0] * u.km / u.s

ss = Orbit.from_vectors(Sun, r, v)

a = 9.53707032 * u.AU
ecc = 0  * u.one
inc = 0 * u.deg
raan = 0 * u.deg
argp = 0 * u.deg
nu = 180 * u.deg

vv = Orbit.from_classical(Sun, a, ecc, inc, raan, argp, nu)

a = 0.999855 * u.AU
ecc = 0 * u.one
inc = 0 * u.deg
raan = 0 * u.deg
argp = 0 * u.deg
nu = 0 * u.deg

gg = Orbit.from_classical(Sun, a, ecc, inc, raan, argp, nu)


# Representem les orbites que hem creat previament


plt.show()


fig, ax = plt.subplots()

ax.grid(True)
ax.set_title("Hohman de la Terra a Saturn")
ax.set_facecolor('None')

# Representem les orbites que hem definit previament

plotter = plotting.OrbitPlotter(ax)

plotter.plot(ss, label="Hohman")
plotter.plot(vv, label="Saturn")
plotter.plot(gg, label="Terra")


plt.show()
