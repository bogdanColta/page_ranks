import random

import networkx as nx

from algorithm_implementation import *


# Adds or removes an edge from the graph with probability 0.5. This action is repeated k times.
def make_change(G, k):
    G1 = G.copy()
    list_removed = []
    list_added = []
    for i in range(k):
        p = random.randint(0, 1)
        # remove edge
        if p == 0:
            choices = [x for x in list(G1.edges()) if x not in list_added]
            if choices:
                edge_removed = random.choice(choices)
                list_removed.append(edge_removed)
                G1.remove_edge(*edge_removed)
            # if there are no edges to be removed, we will add an edge
            else:
                choices = [x for x in list(nx.non_edges(G1)) if x not in list_removed]
                if choices:
                    edge_added = random.choice(choices)
                    list_added.append(edge_added)
                    G1.add_edge(*edge_added)
        # add edge
        else:
            choices = [x for x in list(nx.non_edges(G1)) if x not in list_removed]
            if choices:
                edge_added = random.choice(choices)
                list_added.append(edge_added)
                G1.add_edge(*edge_added)
            # if there are no edges to be added, we will remove an edge
            else:
                choices = [x for x in list(G1.edges()) if x not in list_added]
                if choices:
                    edge_removed = random.choice(choices)
                    list_removed.append(edge_removed)
                    G1.remove_edge(*edge_removed)
    return G1


# Implementation of function that calculates the Euclidean distance between two ranking vectors
def diff_ranks(rank1, rank2):
    return np.linalg.norm(np.array(rank1) - np.array(rank2))


# The following code generates different types of graphs:
def generate_random_graph(n, p):
    G = nx.erdos_renyi_graph(n, p, directed=True)
    return G


def generate_random_regular_graph(n, d):
    G = nx.DiGraph()

    if n * d % 2 != 0 or d >= n:
        raise ValueError("Invalid combination of n and d for a random regular directed graph.")

    nodes = [i for i in range(n) for _ in range(d)]

    random.shuffle(nodes)

    for i in range(n):
        for j in range(1, d // 2 + 1):
            neighbor = nodes[(i + j) % n]
            G.add_edge(i, neighbor)

    return G


def generate_scale_free_graph(n, m):
    G = nx.DiGraph()

    for i in range(m):
        G.add_node(i)
        for j in range(i):
            G.add_edge(i, j)

    for i in range(m, n):
        nodes = list(G.nodes())
        selected_nodes = random.sample(nodes, m)
        G.add_node(i)
        for node in selected_nodes:
            G.add_edge(i, node)

    return G


def generate_small_world_graph(n, k, p):
    G = nx.DiGraph()

    for i in range(n):
        for j in range(1, k // 2 + 1):
            neighbor = (i + j) % n
            G.add_edge(i, neighbor)

    for edge in list(G.edges()):
        if np.random.rand() < p:
            new_target = np.random.choice(
                [node for node in G.nodes() if node != edge[0] and not G.has_edge(edge[0], node)])
            G.remove_edge(edge[0], edge[1])
            G.add_edge(edge[0], new_target)

    return G


def generate_hierarchical_graph(levels, nodes_per_level):
    G = nx.DiGraph()

    for level in range(levels):
        for i in range(nodes_per_level):
            node_id = level * nodes_per_level + i
            G.add_node(node_id)

            if level > 0:
                for j in range(nodes_per_level):
                    prev_level_node = (level - 1) * nodes_per_level + j
                    G.add_edge(prev_level_node, node_id)

    return G


def generate_complete_graph(n):
    G = nx.DiGraph()

    G.add_nodes_from(range(n))
    G.add_edges_from([(i, j) for i in range(n) for j in range(n) if i != j])

    return G


def generate_grid_graph(rows, columns):
    G = nx.DiGraph()

    for i in range(rows):
        for j in range(columns):
            node_id = i * columns + j
            G.add_node(node_id)

    for i in range(rows):
        for j in range(columns):
            node_id = i * columns + j

            if j < columns - 1:
                neighbor_id = i * columns + (j + 1)
                G.add_edge(node_id, neighbor_id)

            if i < rows - 1:
                neighbor_id = (i + 1) * columns + j
                G.add_edge(node_id, neighbor_id)

    return G


def generate_cyclic_graph(n):
    return nx.cycle_graph(n, create_using=nx.DiGraph())


def generate_bipartite_graph(n):
    return nx.bipartite.random_graph(5, 5, 0.3, directed=True)
