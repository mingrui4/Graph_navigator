import itertools
import copy
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

edgelist = pd.read_csv("edge_data.csv")

edgelist.head(10)

nodelist = pd.read_csv("nodes.csv")

nodelist.head(5)
# Create empty graph
g = nx.DiGraph()

# Add edges and edge attributes
for i, elrow in edgelist.iterrows():
    g.add_edge(elrow[0], elrow[1], attr_dict=elrow[2:].to_dict())

# Add node attributes
for i, nlrow in nodelist.iterrows():
    g.node[nlrow['id']].update(nlrow[1:].to_dict())

print(nlrow)


# Preview first 5 edges
list(g.edges(data=True))[0:5]

# Preview first 10 nodes
list(g.nodes(data=True))[0:10]

print('# of edges: {}'.format(g.number_of_edges()))
print('# of nodes: {}'.format(g.number_of_nodes()))

edge_type = dict([((e[0], e[1]), e[2]['attr_dict']['distance']) for e in g.edges(data=True)])

edge_colors = [e[2]['attr_dict']['color'] for e in g.edges(data=True)]

colors = {1:'red',2:'orange',3:'yellow',4:'green',5:'skyblue',6:'blue',7:'purple',0:'grey',8:'pink'}
node_c = [node[1]['property'] for node in g.nodes(data=True)]
node_colors = []
for j in node_c:
    node_colors.append(colors[j])

#edge_weights = dict([((e[0], e[1]), e[2]['attr_dict']['distance']) for e in g.edges(data=True)])

# Define node positions data structure (dict) for plotting
node_positions = {node[0]: (node[1]['left'], -node[1]['top']) for node in g.nodes(data=True)}

dict(list(node_positions.items())[0:5])


# calculate distance between two nodes using nodelist dataframe

dist_result1 =[]
for i in range(1, nodelist.shape[0]):
    for j in range(1, nodelist.shape[0]):
        temp_dict = {}
        if i !=j:
            temp = np.sqrt(np.square(nodelist.iloc[i]['left'] - nodelist.iloc[j]['left']) + \
            np.square(nodelist.iloc[i]['top'] - nodelist.iloc[j]['top']))
            temp = round(temp/100, 2)
            temp_dict['distance'] = temp
            t = ((nodelist.iloc[i]['id'], nodelist.iloc[j]['id']), )
            t += (temp_dict, )
            dist_result1.append(t)


plt.figure(figsize=(8, 6))
nx.draw(g, pos=node_positions, edge_color=edge_colors, node_size=1000, node_color=node_colors, alpha=0.8)
graph_pos = nx.spring_layout(g, weight=3)
nx.draw_networkx_edges(g, graph_pos, edge_color=edge_colors)
nx.draw_networkx_labels(g, pos=node_positions, font_size=8)
nx.draw_networkx_edge_labels(g, pos=node_positions, edge_labels=edge_type, font_size=6)

#labels = [(e[2]['attr_dict']['Type_of_road'], e[2]['attr_dict']['color']) for e in g.edges(data=True)]
plt.title('Zoo Map', size=20)
line1, = plt.plot([1,2,3], label='Not for Disabled', color='red', linewidth=2)
line2, = plt.plot([3,2,1], label='Accessible route – ADA', color='gray', linewidth=2)
node1, = plt.plot([1,2,3], label='Reptiles', color='red',ls = 'dotted', linewidth=2)
node2, = plt.plot([3,2,1], label='Big cats', color='orange',ls = 'dotted', linewidth=2)
node3, = plt.plot([3,2,1], label='Birds', color='yellow',ls = 'dotted', linewidth=2)
node4, = plt.plot([3,2,1], label='Hoofed Mammals', color='green',ls = 'dotted', linewidth=2)
node5, = plt.plot([3,2,1], label='Bears', color='skyblue',ls = 'dotted', linewidth=2)
node6, = plt.plot([3,2,1], label='Invertebrates', color='blue',ls = 'dotted', linewidth=2)
node7, = plt.plot([3,2,1], label='Other Mammals', color='purple',ls = 'dotted', linewidth=2)
node8, = plt.plot([3,2,1], label='Primates', color='pink',ls = 'dotted', linewidth=2)
plt.legend(handles=[line1, line2, node1, node2, node3, node4, node5, node6, node7, node8])


# plt.show()

plt.savefig('St Louis Zoo.png')


