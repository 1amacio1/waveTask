import networkx as nx
import matplotlib.pyplot as plt
from random import *
graph = nx.Graph()
nodes = 'ABCDEFGHIFGHIJK'
res = []
s = []
for i in nodes[randint(0, 7):randint(10, 16)]:
    graph.add_node(i)
    res.append(i)
    s.append(i)
shuffle(res)
for j in range(len(s)):
    if s[j] != res[j]:
        graph.add_edge(s[j], res[j], weight=randint(1, 10))
pos = nx.circular_layout(graph)
nx.draw(graph, pos, with_labels=True, font_weight='bold')
edge_weight = nx.get_edge_attributes(graph,'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels = edge_weight)
plt.show()
