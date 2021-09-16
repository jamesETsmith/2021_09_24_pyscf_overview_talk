import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def add_excitations(
    output: str,
    screen: bool = False,
    screen_frac: float = 0.15,
    sample: bool = False,
    sample_frac: float = 0.1,
):

    # Graph settings
    N = 100  # Size of starting variational space
    avg_deg = 5  # Average degree of vertices

    # Plotting settings
    v0_color = "#40E0D0"  # Turquoise
    v1_color = "#03a1fc"  # Blue
    v2_color = "#62ff29"  # Green
    node_size = 35
    dpi = 600
    aspect_ratio = 0.015
    fontsize = 20
    v_spread = 0.1
    c_spread = 0.3

    alpha0 = 1
    alpha1 = 1

    # Graph Setup
    np.random.seed(20)
    G = nx.Graph()
    pos = {}

    # Initial Variational Space
    for i in range(N):
        G.add_node(i)

    # Applying Hamiltonian
    connections = np.random.randint(avg_deg * 2, size=N)
    el_1 = []
    for i in range(connections.shape[0]):
        for _ in range(connections[i]):
            index = len(G)
            G.add_node(index)
            G.add_edge(i, index)
            el_1.append((i, index))

    el_1 = np.array(el_1)
    n0 = N
    n1 = connections.sum()

    # Create Positions
    pos = np.random.rand(n0 + n1, 2)
    pos[:n0, 0] *= v_spread  # Scale dist.
    pos[n0:, 0] *= c_spread  # Scale dist.
    pos[n0:, 0] += 1  # Shift dist.

    # Draw Variational Space
    nx.draw_networkx_nodes(
        G,
        pos,
        node_size=node_size,
        nodelist=range(n0),
        node_color=v0_color,
        edgecolors="k",
        alpha=alpha0,
    )

    # Draw Connected Space
    s_edge_idx = np.random.choice(el_1.shape[0], int(el_1.size * screen_frac))
    other_edge_idx = np.array([x for x in range(el_1.shape[0]) if x not in s_edge_idx])
    s_edges = el_1[s_edge_idx]
    ns_edges = el_1[other_edge_idx]
    unimportant_idx = np.array([x for x in ns_edges[:, 1]])
    pos[unimportant_idx, 0] += 1

    # Draw Connected Space
    nx.draw_networkx_nodes(
        G,
        pos,
        node_size=node_size,
        nodelist=set(s_edges[:, 1]),
        node_color=v1_color,
        edgecolors="k",
        alpha=alpha1,
    )

    # Draw Connected Space
    nx.draw_networkx_nodes(
        G,
        pos,
        node_size=node_size,
        nodelist=set(ns_edges[:, 1]),
        node_color=v2_color,
        edgecolors="k",
        alpha=alpha1,
    )

    nx.draw_networkx_edges(G, pos, alpha=0.35, width=0.75, edgelist=s_edges)
    nx.draw_networkx_edges(
        G, pos, alpha=0.25, width=0.75, edgelist=ns_edges, style="dashed"
    )
    plt.show()


if __name__ == "__main__":
    add_excitations("test")
