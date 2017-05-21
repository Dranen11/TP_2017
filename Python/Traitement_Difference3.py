import sys

def Traitement_Difference3(nom_exp1a, nom_exp1b, nom_exp1c, nom_exp2a, nom_exp2b, nom_exp2c, nom_resultat, valeur_resistance, t1a, t1b, t1c, t2a, t2b, t2c, duree,amplification = 1., diviseur = 1., offset = 0.):
    import numpy as np
    from Graphique import Graphique_Simple
    from Graphique import Graphique_Double_Echelle
    from Integration import Integrale_Trapeze
    from Filtre import Passe_bas
    from scipy import fftpack

    data1a = np.loadtxt(nom_exp1a+'.dat', delimiter = ';')
    data1b = np.loadtxt(nom_exp1b+'.dat', delimiter = ';')
    data1c = np.loadtxt(nom_exp1c+'.dat', delimiter = ';')
    data2a = np.loadtxt(nom_exp2a+'.dat', delimiter = ';')
    data2b = np.loadtxt(nom_exp2b+'.dat', delimiter = ';')
    data2c = np.loadtxt(nom_exp2c+'.dat', delimiter = ';')

    Temps1a = np.asarray(data1a[:,0], dtype=float)/1000000.
    Temps1a = Temps1a - Temps1a[0]
    Tension1a = (np.asarray(data1a[:,1], dtype=float)-offset)*diviseur/amplification

    Temps1b = np.asarray(data1b[:,0], dtype=float)/1000000.
    Temps1b = Temps1b - Temps1b[0]
    Tension1b = (np.asarray(data1b[:,1], dtype=float)-offset)*diviseur/amplification

    Temps1c = np.asarray(data1c[:,0], dtype=float)/1000000.
    Temps1c = Temps1c - Temps1c[0]
    Tension1c = (np.asarray(data1c[:,1], dtype=float)-offset)*diviseur/amplification

    Temps2a = np.asarray(data2a[:,0], dtype=float)/1000000.
    Temps2a = Temps2a - Temps2a[0]
    Tension2a = (np.asarray(data2a[:,1], dtype=float)-offset)*diviseur/amplification

    Temps2b = np.asarray(data2b[:,0], dtype=float)/1000000.
    Temps2b = Temps2b - Temps2b[0]
    Tension2b = (np.asarray(data2b[:,1], dtype=float)-offset)*diviseur/amplification

    Temps2c = np.asarray(data2[:,0], dtype=float)/1000000.
    Temps2c = Temps2b - Temps2b[0]
    Tension2c = (np.asarray(data2b[:,1], dtype=float)-offset)*diviseur/amplification

    i1a = 0
    for i in range(0, Temps1a.size):
        if abs(Temps1a[i1a]-t1a) > abs(Temps1a[i]-t1a) :
            i1a = i

    i1b = 0
    for i in range(0, Temps1b.size):
        if abs(Temps1b[i1b]-t1b) > abs(Temps1b[i]-t1b) :
            i1b = i

    i1c = 0
    for i in range(0, Temps1c.size):
            if abs(Temps1c[i1c]-t1c) > abs(Temps1c[i]-t1c) :
                i1c = i

    di = 0
    for i in range(i1a, Temps1a.size):
        if abs(Temps1a[di+i1a]-(t1a+duree)) > abs(Temps1a[i]-(t1a+duree)) :
            di = i - i1a

    i2a = 0
    for i in range(0, Temps2a.size):
        if abs(Temps2a[i2a]-t2a) > abs(Temps2a[i]-t2a) :
            i2a = i

    i2b = 0
    for i in range(0, Temps2b.size):
        if abs(Temps2b[i2b]-t2b) > abs(Temps2b[i]-t2b) :
            i2b = i

    i2c = 0
    for i in range(0, Temps2c.size):
        if abs(Temps2c[i2c]-t2c) > abs(Temps2c[i]-t2c) :
            i2c = i

    Temps = np.zeros(di)
    T1a = np.zeros(di)
    T1b = np.zeros(di)
    T1c = np.zeros(di)
    T2a = np.zeros(di)
    T2b = np.zeros(di)
    T2c = np.zeros(di)

    for i in range(i1a, i1a+di):
        Temps[i-i1a] = Temps1a[i]-Temps1a[i1a]
        T1a[i-i1a] = Tension1a[i]

    for i in range(i1b, i1b+di):
        T1b[i-i1b] = Tension1b[i]

    for i in range(i1b, i1b+di):
        T1b[i-i1b] = Tension1b[i]

    for i in range(i2a, i2a+di):
        T2a[i-i2a] = Tension2a[i]

    for i in range(i2b, i2b+di):
        T2b[i-i2b] = Tension2b[i]

    for i in range(i2b, i2b+di):
        T2b[i-i2b] = Tension2b[i]

    Tension = T1a+T1b+T1c-T2a-T2b-T2c
    freq_echantillonage = Temps[Temps.size-1]/Temps.size
    freqs = fftpack.fftfreq(Temps.size, d=freq_echantillonage)
    TFT_M = abs(fftpack.fft(Tension-np.mean(Tension)))
    TFT = abs(fftpack.fft(Tension))

    Graphique_Simple(Temps, Tension, x_label = 'Temps [s]', y_label = 'Tension [V]', save_name = 'Graphique_'+nom_resultat+'_T', graph_name = 'Difference de la tension au cours du temps')
    Graphique_Simple(freqs, TFT, x_label = 'Temps [s]', y_label = 'Tension [V]', save_name = 'Graphique_'+nom_resultat+'_TFT', graph_name = 'TF Difference de la tension au cours du temps')
    Graphique_Simple(freqs, TFT_M, x_label = 'Temps [s]', y_label = 'Tension [V]', save_name = 'Graphique_'+nom_resultat+'_TTF-M', graph_name = 'TF sans la composante continu Difference de la tension au cours du temps')



if __name__ == '__main__':
    print 'sys.argv: ', sys.argv
    if len(sys.argv) == 16:
        Traitement_Difference3(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], float(sys.argv[8]), float(sys.argv[9]), float(sys.argv[10]), float(sys.argv[11]), float(sys.argv[12]), float(sys.argv[13]), float(sys.argv[14]), float(sys.argv[15]))
    elif len(sys.argv) == 17:
        Traitement_Difference3(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], float(sys.argv[8]), float(sys.argv[9]), float(sys.argv[10]), float(sys.argv[11]), float(sys.argv[12]), float(sys.argv[13]), float(sys.argv[14]), float(sys.argv[15]), float(sys.argv[16]))
    elif len(sys.argv) == 18:
        Traitement_Difference3(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], float(sys.argv[8]), float(sys.argv[9]), float(sys.argv[10]), float(sys.argv[11]), float(sys.argv[12]), float(sys.argv[13]), float(sys.argv[14]), float(sys.argv[15]), float(sys.argv[16]), float(sys.argv[17]))
    elif len(sys.argv) == 19:
        Traitement_Difference3(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], float(sys.argv[8]), float(sys.argv[9]), float(sys.argv[10]), float(sys.argv[11]), float(sys.argv[12]), float(sys.argv[13]), float(sys.argv[14]), float(sys.argv[15]), float(sys.argv[16]), float(sys.argv[17]), float(sys.argv[18]))
    else:
        message('No argument')
