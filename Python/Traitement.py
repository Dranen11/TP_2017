import sys

def Traitement(nom_exp, valeur_resistance, amplification = 1., diviseur = 1., offset = 0., freq_coupure = 0.):
    import numpy as np
    from Graphique import Graphique_Simple
    from Graphique import Graphique_Double_Echelle
    from Integration import Integrale_Trapeze
    from Filtre import Passe_bas

    data = np.loadtxt(nom_exp+'.dat')
    Temps = data[:,1]/1000000.
    Tension = (data[:,2]-offset)*diviseur/amplification
    Intensite = Tension/(valeur_resistance);

    if freq_coupure != 0:
            Tension = Passe_bas(Temps, Tension, freq_coupure)
            Intensite = Passe_bas(Temps, Intensite, freq_coupure)

    Puissance = Tension*Intensite;

    Graphique_Double_Echelle(Temps, Tension, Intensite, x_label = 'Temps [s]', y1_label = 'Tension [V]', y2_label = 'Intensite [A]', save_name = 'Graphique_'+nom_exp+'_TI', graph_name = 'Evolution de la tension et du courant au cours du temps')
    Graphique_Simple(Temps, Puissance, y_label = 'Puissance [W]', x_label = 'Temps [s]', graph_name = 'Evolution de la puissance électrique au cours du temps', save_name = 'Graphique_'+nom_exp+'_P')
    Energie = Integrale_Trapeze(Temps, Puissance)
    print("Energie : " + Energie + " J")

    return Energie



if __name__ == '__main__':
    print 'sys.argv: ', sys.argv
    if len(sys.argv) == 3:
        Traitement(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 4:
        Traitement(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 5:
        Traitement(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    elif len(sys.argv) == 6:
        Traitement(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    elif len(sys.argv) == 7:
        Traitement(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    else:
        message('No argument')
