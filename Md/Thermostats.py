import numpy as np
from Energy import keSys

def Anderson(V,t,sigma,nu,ke_T,dim):
    colProb = t*nu
    prob = np.random.uniform(0, 1, len(V))
    V[prob <= colProb] = np.random.normal(0, sigma, dim)
    V -= np.mean(V)
    
def VelocityRescale(V,t,sigma,nu,ke_T,dim):
    vScale = np.sqrt(ke_T/keSys(V))
    V *= vScale

def NoThermostat(V,t,sigma,nu,ke_T,dim):
    return None