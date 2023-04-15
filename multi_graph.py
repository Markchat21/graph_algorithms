import networkx as nx
import matplotlib.pyplot as plt

# Creamos un grafo no dirigido
G = nx.MultiGraph()

# Agregamos nodos
G.add_nodes_from(['a', 'b', 'c', 'd'])

# Agregamos aristas con etiquetas
G.add_edge('a', 'a', label='e1')
G.add_edge('a', 'b', label='e2')
G.add_edge('a', 'b', label='e3')
G.add_edge('a', 'b', label='e4')
G.add_edge('b', 'd', label='e5')
G.add_edge('d', 'c', label='e6')
G.add_edge('d', 'c', label='e7')
G.add_edge('c', 'c', label='e8')
G.add_edge('c', 'c', label='e9')

# Creamos la disposición del grafo
pos = nx.spring_layout(G)

# Dibujamos el grafo
nx.draw(G, pos, with_labels=True, node_size=1000)

# Agregamos las etiquetas de las aristas
edge_labels = nx.get_edge_attributes(G, 'label')

"""
NOTA: no se pueden mostrar ni etiquetar aristas paralelas
asi que la linea siguiente dará error si se ejecuta
"""

# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

# Creamos y mostramos las matrices de adyaciencia e incidencia
adjacency_matrix = nx.adjacency_matrix(G)
incidence_matrix = nx.incidence_matrix(G)
print(adjacency_matrix.todense())
print(incidence_matrix.todense())

# Calculamos la suma de los grados
sum = 0
for node, degree in G.degree():
    sum += degree

print(sum)

# Mostramos la figura
plt.show()
