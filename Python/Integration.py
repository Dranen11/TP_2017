def Integrale_Trapeze(temps,valeur):
    import numpy as np
    integral = 0.;
    for i in np.arange(temps.size-2):
        integral += 0.5*(valeur[i]+valeur[i+1])*(temps[i+1]-temps[i])
    return integral
