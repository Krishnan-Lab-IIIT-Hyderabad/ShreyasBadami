import numpy as np
import System 
from Energy import peSys, keSys, F
import matplotlib.pyplot as plt

def pbc(X,V,L):
    V[X >= L] *= -1
    V[X <= 0] *= -1

class Propagator:
    def __init__(self,numSteps,timeStep):
        self.numSteps = numSteps
        self.timeStep = timeStep
        self.H = np.zeros(numSteps)
        self.KE = np.zeros(numSteps)
        self.PE = np.zeros(numSteps)
        self.sigma = 5
        self.nu = 5
        self.ke_T = 5

    def velocityVerlet(self,particles,thermostat):
        a1 = np.zeros((particles.n,particles.dim))
        for particle in particles.X:
            a1 -= F(particles.X-particle)
        for i in range(self.numSteps):
            self.KE[i] = keSys(particles.V)
            self.PE[i] = peSys(particles.X)
            particles.X += self.timeStep*particles.V + 0.5*self.timeStep*self.timeStep*a1
            a2 = np.zeros((particles.n,particles.dim))
            for particle in particles.X:
                a2 -= F(particles.X-particle)
            a1+=a2
            particles.V += 0.5*a1*self.timeStep
            a1 = a2
            thermostat(particles.V,self.timeStep,self.sigma,self.nu,self.ke_T,particles.dim)
            pbc(particles.X,particles.V,particles.L)   
        self.H = self.KE + self.PE
        particles.update(particles.X,particles.V)


    def plot(self):
        x1 = np.linspace(0, 1, self.numSteps)
        plt.plot(x1, self.PE,color='blue')
        plt.plot(x1, self.KE, color='red')   
        plt.plot(x1, self.H,color='green')
        plt.savefig('energyplot.png')
        plt.close()

def createSim(numSteps,timeStep):
    v = Propagator(numSteps,timeStep)
    return v