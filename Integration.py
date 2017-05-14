import numpy as np

def Integrale_Trapeze(temps,valeur):
    integral = 0.;
    for i in np.arrange(temps.ndarray.size-2):
        integral += 0.5*(valeur[i]+valeur[i+1])*(temps[i+1]-temps[i])
    return integral
