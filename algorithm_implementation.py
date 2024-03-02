import numpy as np


# We create a function that takes a dictionary of nodes and their score and returns a rank vector
def ranks(dict):
    a = sorted(dict.keys())
    k = [dict[key] for key in a]
    sorted_elements = sorted(enumerate(k), key=lambda x: x[1], reverse=True)
    ranks_dict = {index: rank + 1 for rank, (index, _) in enumerate(sorted_elements)}
    k = [ranks_dict[index] for index in range(len(k))]
    return k


# Implementation of indegree algorithm
def indegree(G):
    dict = {}
    for node in G.nodes:
        dict[node] = G.in_degree(node)
    return dict


# Implementation of PageRank algorithm with k = 100 steps
def pagerank(G):
    dict = {}
    beta = 0.85
    k = 100
    for node in G.nodes:
        dict[node] = 1 / len(G.nodes)

    for i in range(k):
        temp = dict.copy()
        for node in G.nodes:
            sum = 0
            in_edges = G.in_edges(node)
            for edge in in_edges:
                out = (G.out_degree(edge[0]))
                sum += temp[edge[0]] / out

            dict[node] = beta * sum + (1 - beta) / len(G.nodes)

    return dict


# Implementation of HITS algorithm with k = 100 steps
def hits(G):
    k = 100
    node_to_index = {node: i for i, node in enumerate(G.nodes)}

    adj = [[0 for _ in range(len(G.nodes))] for _ in range(len(G.nodes))]

    for edge in G.edges:
        i, j = node_to_index[edge[0]], node_to_index[edge[1]]
        adj[i][j] = 1

    matrix = np.array(adj)
    transpose = matrix.transpose()

    u = [[1] for x in range(len(G.nodes))]
    v = []
    for i in range(k):
        v = np.dot(transpose, u)  # authority
        u = np.dot(matrix, v)  # hub

    r = [x[0] for x in v]
    sorted_elements = sorted(enumerate(r), key=lambda x: x[1], reverse=True)
    ranks_dict = {index: rank + 1 for rank, (index, _) in enumerate(sorted_elements)}
    r = [ranks_dict[index] for index in range(len(r))]
    return r


# Implementation of function that calculates link distance between two graphs
def link_distance(g1, g2):
    edges1 = set(g1.edges)
    edges2 = set(g2.edges)

    link_distance = len(edges1.symmetric_difference(edges2))
    return link_distance
