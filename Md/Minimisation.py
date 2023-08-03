import numpy as np
import System
from Energy import peSys, F
import Propagator
import copy

def minimisation(sim,particles):
        X = copy.copy(particles.X)
        V = copy.copy(particles.V)
        a1 = np.zeros((particles.n,particles.dim))
        for particle in X:
            a1 -= F(X - particle)
        sim.PE[0] = peSys(X)
        for i in range(1,sim.numSteps):
            sim.PE[i] = peSys(X)
            if(sim.PE[i] > sim.PE[i-1]):
                return i,sim.PE[i-1],X
            X += sim.timeStep*V + 0.5*sim.timeStep*sim.timeStep*a1
            a2 = np.zeros((particles.n,particles.dim))
            for l in X:
                a2 -= F(X-l)
            a1+=a2
            V += 0.5*a1*sim.timeStep
            a1 = a2
            Propagator.pbc(X,V,particles.L)   