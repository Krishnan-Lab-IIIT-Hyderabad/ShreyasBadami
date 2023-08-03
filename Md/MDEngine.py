import sys
sys.path.append('./src')
import System
import Propagator
from Thermostats import Anderson, VelocityRescale, NoThermostat
from Minimisation import minimisation



particles = System.createSystem(1000,10,3)
sim = Propagator.createSim(100, 0.001)
sim.velocityVerlet(particles, NoThermostat)
'''
i, pe, X = minimisation(sim, particles)
print(i)
print(pe)
print(X)
'''
sim.plot()