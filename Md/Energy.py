from sympy import symbols, diff, lambdify
import numpy as np

k = 1
def pe(x):
    return 0.5*k*x*x

x = symbols('x')
f = pe(x)
force = diff(f, x)
F = lambdify(x, force)

def keSys(V):
    return np.sum(V**2) * 0.5
    
def peSys(X):
    te = 0
    for l in X:
        te += pe(np.sqrt(np.sum((X-l)**2)))
    return te*0.5