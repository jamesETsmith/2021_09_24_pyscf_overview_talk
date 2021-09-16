import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

#
# User parameters
#

# Graph settings
N = 5  # Size of starting variational space
avg_deg = 4  # Average degree of vertices
node_spacing = 2

# Plotting settings
v0_color = "#40E0D0"  # Turquoise
v1_color = "#98FB98"  # Turquoise
v2_color = "#7FFF00"  # Turquoise
node_size = 15
dpi = 600
filename = "SCI_0.png"
aspect_ratio = 0.015
fontsize = 17
alpha = 0

#
# Make graph
#
def make_graph(filename, case):
    if case == 0:  # Just plot V_0
        alpha1 = 0
        alpha2 = 0
    elif case == 1:
        alpha1 = 1
        alpha2 = 0
    else:
        alpha1 = 1
        alpha2 = 1

    np.random.seed(20)

    G = nx.Graph()
    pos = {}

    # Initial Variational Space (V0)
    for i in range(N):
        G.add_node(i)
        pos[i] = (0, i * node_spacing)

    # Applying Hamiltonian
    connections = np.random.randint(avg_deg * 2, size=N)
    last_y = 0
    el_1 = []
    for i in range(connections.shape[0]):
        for j in range(connections[i]):
            index = len(G)
            G.add_node(index)
            G.add_edge(i, index)
            el_1.append((i, index))
            pos[index] = (1, last_y)
            last_y += node_spacing

    # Applying Hamiltonian again
    connections2 = np.random.randint(avg_deg * 2, size=len(G) - N)
    last_y2 = 0
    el_2 = []
    for i in range(connections2.shape[0]):
        for j in range(connections2[i]):
            index = len(G)
            G.add_node(index)
            G.add_edge(i + N, index)
            el_2.append((i + N, index))
            pos[index] = (2, last_y2)
            last_y2 += node_spacing

    n0 = N
    n1 = connections.sum()
    n2 = connections2.sum()

    # Centering V0 and V1
    for i in range(n0):
        yi = node_spacing * (i - n0 / 2) + last_y2 / 2
        pos[i] = (0, yi)

    for i in range(n1):
        yi = node_spacing * (i - n1 / 2) + last_y2 / 2
        pos[i + n0] = (1, yi)

    # Draw Initial Variational Space
    nodes = nx.draw_networkx_nodes(
        G, pos, node_size=node_size, nodelist=range(n0), node_color=v0_color
    )
    nodes.set_edgecolor("k")
    nodes = nx.draw_networkx_nodes(
        G,
        pos,
        node_size=node_size,
        nodelist=range(n0, n0 + n1),
        node_color=v1_color,
        alpha=alpha1,
    )
    nodes.set_edgecolor("k")
    nodes = nx.draw_networkx_nodes(
        G,
        pos,
        node_size=node_size,
        nodelist=range(n0 + n1, n0 + n1 + n2),
        node_color=v2_color,
        alpha=alpha2,
    )
    nodes.set_edgecolor("k")

    if case > 0:
        nx.draw_networkx_edges(G, pos, alpha=0.5, width=0.75, edgelist=el_1)
    if case > 1:
        nx.draw_networkx_edges(G, pos, alpha=0.5, width=0.75, edgelist=el_2)

    # Add Selected CI Labels
    plt.text(0, last_y2 / 2 - 18, "$\mathcal{V}^0$", ha="center", fontsize=fontsize)
    if case > 0:
        plt.text(1, last_y2 / 2 - 35, "$\mathcal{V}^1$", ha="center", fontsize=fontsize)
        plt.text(
            0.5,
            last_y2 * 0.63,
            r"$ \hat{H} \mathcal{V}^0$",
            ha="center",
            fontsize=fontsize,
        )

    if case > 1:
        plt.text(2, -10, "$\mathcal{V}^2$", ha="center", fontsize=fontsize)
        plt.text(
            1.5,
            last_y2 * 0.9,
            r"$ \hat{H} \mathcal{V}^1$",
            ha="center",
            fontsize=fontsize,
        )

    # Plot formatting
    plt.gca().set_aspect(aspect_ratio)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(filename, dpi=dpi, transparent=True, bbox_inches="tight", pad_inches=0)
    # plt.show()


if __name__ == "__main__":
    make_graph("SCI_0.png", 0)
    make_graph("SCI_1.png", 1)
    make_graph("SCI_2.png", 2)
