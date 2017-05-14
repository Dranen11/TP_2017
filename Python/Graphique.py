def Graphique_Simple(x, y,x_label = "",y_label = "", graph_name = ""):
    import numpy as np
    import matplotlib.pyplot as plt

    plt.figure(figsize=(16,6))
    plt.plot(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(graph_name)

    plt.savefig(graph_name + '.eps', format = 'eps')
    plt.savefig(graph_name + '.svg', format = 'svg')
    plt.show(block = False)
