import numpy as np
import matplotlib.pyplot as plt
import poliastro.plotting as plotting

from astropy import units as u

from poliastro.bodies import Earth, Mars, Sun
from poliastro.twobody import Orbit

plt.style.use("seaborn")  

 # Definim cada orbita on:
	
	# a: semieix major
	# ecc: excentricitat
	# inc: inclinacio respecte la horizontal(sera 0 en totes les orbites 
	# 	ja que es troben en el mateix pla per guio del treball)
	# raan: inclinacio respecte la vertical
	# argp: argument del periheli
	# nu: posicio punt 

a = 0.999855 * u.AU
ecc = 0  * u.one
inc = 0 * u.deg
raan = 0 * u.deg
argp = 0 * u.deg
nu = 0 * u.deg

Terra = Orbit.from_classical(Sun, a, ecc, inc, raan, argp, nu)

a = 5.20336301 * u.AU
ecc = 0  * u.one
inc = 0 * u.deg
raan = 0 * u.deg
argp = 0 * u.deg
nu = 163 * u.deg

Jupiter = Orbit.from_classical(Sun, a, ecc, inc, raan, argp, nu)

a = 9.53707032 * u.AU
ecc = 0 * u.one
inc = 0 * u.deg
raan = 0 * u.deg
argp = 0 * u.deg
nu = 181.425 * u.deg

Saturn = Orbit.from_classical(Sun, a, ecc, inc, raan, argp, nu)

a = 3.35 * u.AU
ecc = 0.7014925373 * u.one
inc = 0 * u.deg
raan = 0 * u.deg
argp = 0 * u.deg
nu = 270 * u.deg

Orbita_57_UA = Orbit.from_classical(Sun, a, ecc, inc, raan, argp, nu)

a = 734538419370 * u.m
ecc = 0.9423428459 * u.one
inc = 0 * u.deg
raan = 1.425 * u.deg
argp = 0 * u.deg
nu = 170 * u.deg

Hohman_J_S = Orbit.from_classical(Sun, a, ecc, inc, raan, argp, nu)


# Creem la grafica on representarem les diferents orbites

fig, ax = plt.subplots()

ax.grid(True)
ax.set_title("De la Terra a Saturn amb asistència en Júpiter")
ax.set_facecolor('None')

# Representem les orbites que hem definit previament

plotter = plotting.OrbitPlotter(ax)

plotter.plot(Terra, label="Terra")
plotter.plot(Jupiter, label="Júpiter")
plotter.plot(Saturn, label="Saturn")
plotter.plot(Orbita_57_UA, label="El·lipse T-J")
plotter.plot(Hohman_J_S, label="Hohman J-S")


plt.show()
