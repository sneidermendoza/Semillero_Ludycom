import networkx as nx
import matplotlib.pyplot as plt


grafo = nx.Graph()

grafo.add_nodes_from(["a","b","c","d","e","f","g","h","i"])

grafo.add_edges_from([
    ("a","b"),
    ("a","c"),
    ("a","e"),
    ("b","c"),
    ("b","f"),
    ("e","d"),
    ("d","h"),
    ("d","g"),
    ("f","b"),
    ("f","i"),
    ("i","c"),
    ("i","d"),
])

print(nx.adjacency_matrix(grafo).todense())
print(nx.incidence_matrix(grafo).todense())
nx.draw(grafo)
plt.show()