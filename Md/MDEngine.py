import sys
sys.path.append('./src')
import System
import Propagator
from Thermostats import Anderson, VelocityRescale, NoThermostat
from Minimisation import minimisation



particles = System.createSystem(10,10,3)
sim = Propagator.createSim(10000, 0.01)
sim.velocityVerlet(particles, VelocityRescale)
'''
i, pe, X = minimisation(sim, particles)
print(i)
print(pe)
print(X)
'''
sim.plot()