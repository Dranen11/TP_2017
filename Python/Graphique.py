def Graphique_Simple(x, y,x_label = "",y_label = "", graph_name = "", linestyle = 'b-', save_name = "",):
    import numpy as np
    import matplotlib.pyplot as plt


    plt.rcParams.update({'font.size': 22})

    plt.figure(figsize=(16,7.5))
    plt.plot(x, y, linestyle)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(graph_name)

    if save_name == "":
        plt.savefig(graph_name + '.eps', format = 'eps')
        plt.savefig(graph_name + '.svg', format = 'svg')
    else :
        plt.savefig(save_name + '.eps', format = 'eps')
        plt.savefig(save_name + '.svg', format = 'svg')
    plt.show(block = False)

def Graphique_Double_Echelle(x, y1, y2,x_label = "",y1_label = "", y2_label = "", graph_name = "", save_name = "", linestyle1 = '-', linestyle2 = '-', color1 = 'b', color2 = 'g'):
    import numpy as np
    import matplotlib.pyplot as plt

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(x, y1, color1+linestyle1)
    ax2.plot(x, y2, color1+linestyle2)
    ax1.set_xlabel(x_label)
    ax1.set_ylabel(y1_label, color = color1)
    ax2.set_ylabel(y2_label, color = color2)
    plt.title(graph_name)

    if save_name == "":
        plt.savefig(graph_name + '.eps', format = 'eps')
        plt.savefig(graph_name + '.svg', format = 'svg')
    else :
        plt.savefig(save_name + '.eps', format = 'eps')
        plt.savefig(save_name + '.svg', format = 'svg')
    plt.show(block = False)
