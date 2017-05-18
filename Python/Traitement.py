import sys

def Traitement(nom_exp, valeur_resistance, amplification = 1., diviseur = 1., offset = 0., freq_coupure = 0.):
    import numpy as np
    from Graphique import Graphique_Simple
    from Graphique import Graphique_Double_Echelle
    from Integration import Integrale_Trapeze
    from Filtre import Passe_bas

    data = np.loadtxt(nom_exp+'.dat', delimiter = ';')
    Temps = np.asarray(data[:,0], dtype=float)/1000000.
    Tension = (np.asarray(data[:,1], dtype=float)-offset)*diviseur/amplification
    Intensite = Tension/(valeur_resistance);

    if freq_coupure != 0:
            Tension = Passe_bas(Temps, Tension, freq_coupure)
            Intensite = Passe_bas(Temps, Intensite, freq_coupure)

    Puissance = Tension*Intensite;

    Graphique_Double_Echelle(Temps, Tension, Intensite, x_label = 'Temps [s]', y1_label = 'Tension [V]', y2_label = 'Intensite [A]', save_name = 'Graphique_'+nom_exp+'_TI', graph_name = 'Evolution de la tension et du courant au cours du temps')
    Graphique_Simple(Temps, Tension, x_label = 'Temps [s]', y_label = 'Tension [V]', save_name = 'Graphique_'+nom_exp+'_T', graph_name = 'Evolution de la tension au cours du temps')
    Graphique_Simple(Temps, Puissance, y_label = 'Puissance [W]', x_label = 'Temps [s]', graph_name = 'Evolution de la puissance electrique au cours du temps', save_name = 'Graphique_'+nom_exp+'_P')
    Energie = Integrale_Trapeze(Temps, Puissance)
    print("Energie : " + str(Energie) + " J")

    return Energie



if __name__ == '__main__':
    print 'sys.argv: ', sys.argv
    if len(sys.argv) == 3:
        Traitement(sys.argv[1], float(sys.argv[2]))
    elif len(sys.argv) == 4:
        Traitement(sys.argv[1], float(sys.argv[2]), float(sys.argv[3]))
    elif len(sys.argv) == 5:
        Traitement(sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]))
    elif len(sys.argv) == 6:
        Traitement(sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]))
    elif len(sys.argv) == 7:
        Traitement(sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]))
    else:
        message('No argument')
