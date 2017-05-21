import sys

def Traitement_Difference(nom_exp1, nom_exp2, nom_resultat, valeur_resistance, t1, t2, duree,amplification1 = 1., amplification2 = 1., diviseur = 1., offset = 0., freq_coupure = 0.):
    import numpy as np
    from Graphique import Graphique_Simple
    from Graphique import Graphique_Double_Echelle
    from Integration import Integrale_Trapeze
    from Filtre import Passe_bas
    from scipy import fftpack

    data1 = np.loadtxt(nom_exp1+'.dat', delimiter = ';')
    data2 = np.loadtxt(nom_exp2+'.dat', delimiter = ';')

    Temps1 = np.asarray(data1[:,0], dtype=float)/1000000.
    Temps1 = Temps1 - Temps1[0]
    Tension1 = (np.asarray(data1[:,1], dtype=float)-offset)*diviseur/amplification1

    Temps2 = np.asarray(data2[:,0], dtype=float)/1000000.
    Temps2 = Temps2 - Temps2[0]
    Tension2 = (np.asarray(data2[:,1], dtype=float)-offset)*diviseur/amplification1

    i1 = 0
    for i in range(0, Temps1.size):
        if abs(Temps1[i1]-t1) > abs(Temps1[i]-t1) :
            i1 = i
    di = 0
    for i in range(i1, Temps1.size):
        if abs(Temps1[di+i1]-(t1+duree)) > abs(Temps1[i]-(t1+duree)) :
            di = i - i1

    i2 = 0
    for i in range(0, Temps2.size):
        if abs(Temps2[i2]-t2) > abs(Temps2[i]-t2) :
            i2 = i

    Temps = np.zeros(di)
    T1 = np.zeros(di)
    T2 = np.zeros(di)

    for i in range(i1, i1+di):
        Temps[i-i1] = Temps1[i]-Temps1[i1]
        T1[i-i1] = Tension1[i]

    for i in range(i2, i2+di):
        T2[i-i2] = Tension2[i]

    Tension = T1-T2
    freq_echantillonage = Temps[Temps.size-1]/Temps.size
    freqs = fftpack.fftfreq(Temps.size, d=freq_echantillonage)
    TFT_M = abs(fftpack.fft(Tension-np.mean(Tension)))
    TFT = abs(fftpack.fft(Tension))

    Graphique_Simple(Temps, Tension, x_label = 'Temps [s]', y_label = 'Tension [V]', save_name = 'Graphique_'+nom_resultat+'_T', graph_name = 'Difference de la tension au cours du temps')
    Graphique_Simple(freqs, TFT, x_label = 'Temps [s]', y_label = 'Tension [V]', save_name = 'Graphique_'+nom_resultat+'_TFT', graph_name = 'TF Difference de la tension au cours du temps')
    Graphique_Simple(freqs, TFT_M, x_label = 'Temps [s]', y_label = 'Tension [V]', save_name = 'Graphique_'+nom_resultat+'_TTF-M', graph_name = 'TF sans la composante continu Difference de la tension au cours du temps')



if __name__ == '__main__':
    print 'sys.argv: ', sys.argv
    if len(sys.argv) == 8:
        Traitement_Difference(sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7]))
    elif len(sys.argv) == 10:
        Traitement_Difference(sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7]), float(sys.argv[8]), float(sys.argv[9]))
    elif len(sys.argv) == 11:
        Traitement_Difference(sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7]), float(sys.argv[8]), float(sys.argv[9]), float(sys.argv[10]))
    elif len(sys.argv) == 12:
        Traitement_Difference(sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7]), float(sys.argv[8]), float(sys.argv[9]), float(sys.argv[10]), float(sys.argv[11]))
    elif len(sys.argv) == 13:
        Traitement_Difference(sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7]), float(sys.argv[8]), float(sys.argv[9]), float(sys.argv[10]), float(sys.argv[11]), float(sys.argv[12]))
    else:
        message('No argument')
