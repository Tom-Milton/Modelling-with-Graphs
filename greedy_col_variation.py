import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_next_vertex(G):
    new_graph_nodes = [i for i in G.nodes() if G.node[i]['visited'] == 'yes'] #creates list of nodes that have been visited
    new_graph = []
    for i in new_graph_nodes:
        new_graph.extend([j for j in G[i] if G.node[j]['visited'] == 'no']) #creates list of the neighbours of those nodes that have not been visited
    if len(new_graph) == 0: #initalises first node
        return 1
    else:
        next_vertex = min(new_graph) #finds smallest node in the new graph
        return next_vertex

def find_smallest_colour(G,i):
    n = len(G.nodes())

    adjacent_colours = list(set([G.node[j]['colour'] for j in G[i]]))  # finds adjacent colours to node
    if 'never coloured' in adjacent_colours:  # removes nodes without a colour
        adjacent_colours.remove('never coloured')
    next_colour = next(k for k, v in enumerate(sorted(adjacent_colours) + [None], 1) if k != v)  # finds smallest number (colour) not in sorted adjacent_colours
    return next_colour


def greedy(G):
    n = len(G.nodes())
    global kmax
    global visited_counter

    kmax = 0 #initalises max number of colours used
    visited_counter = 0 #initalises number of notes visited
    while visited_counter != n: #runs until all nodes have been visited
        i = find_next_vertex(G) #finds next node
        next_colour = find_smallest_colour(G, i) #finds colour for node
        if next_colour > kmax: #if the colour is higher than current max colour updates kmax
            kmax = next_colour
        G.node[i]['colour'] = next_colour #assigns colour
        G.node[i]['visited'] = 'yes' #marks as visited
        visited_counter += 1 #increases counter

    print()
    for i in G.nodes():
        print('vertex', i, ': colour', G.nodes[i]['colour'])
    print()
    print('The number of colours that Greedy computed is:', kmax)
    print()



print('Graph G1:')
G=graph1.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G2:')
G=graph2.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G3:')
G=graph3.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G4:')
G=graph4.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G5:')
G=graph5.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)
