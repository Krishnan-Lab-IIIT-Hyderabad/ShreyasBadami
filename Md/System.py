import numpy as np
import sympy as sp
import math
import matplotlib.pyplot as plt

class System:
    def __init__(self,n,L,dim):
        self.n = n
        self.L = L
        self.dim = dim
        self.X = np.random.uniform(0.001,L,(n,dim))
        self.V = np.zeros((n,dim))
        
    
    def update(self,X,V):
        self.X = X
        self.V = V

def createSystem(n,l,dim):
    v = System(n,l,dim)
    return v

