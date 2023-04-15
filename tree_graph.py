import networkx as nx
import matplotlib.pyplot as plt

# Creamos un grafo conexo no dirigido
G = nx.Graph()

# Agregamos nodos
G.add_nodes_from(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

# Agregamos aristas con peso
G.add_edge('a', 'b', weight=6)
G.add_edge('a', 'h', weight=15)
G.add_edge('a', 'f', weight=10)
G.add_edge('a', 'd', weight=30)
G.add_edge('f', 'b', weight=10)
G.add_edge('f', 'h', weight=40)
G.add_edge('f', 'g', weight=30)
G.add_edge('f', 'e', weight=45)
G.add_edge('e', 'g', weight=27)
G.add_edge('e', 'c', weight=12)
G.add_edge('e', 'b', weight=25)
G.add_edge('b', 'd', weight=27)
G.add_edge('b', 'c', weight=31)
G.add_edge('d', 'c', weight=18)
G.add_edge('g', 'h', weight=12)

# Buscamos la expasion minimal
minimal_tree = nx.minimum_spanning_tree(G)

# Dibujamos el grafo original
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

# Dibujamos la expasion minimal en rojo
nx.draw_networkx_edges(minimal_tree, pos, edge_color='r', width=2)

# Sumamos y mostramos el peso
sum = 0
for u, v, wt in minimal_tree.edges.data('weight'):
    sum += wt

print(sum)
# Comprobamos is es euleriano
print(nx.is_eulerian(G))

# Mostramos la figura
plt.show()
