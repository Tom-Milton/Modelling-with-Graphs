import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_smallest_colour(G,i):
    n = len(G.nodes())

    adjacent_colours = list(set([G.node[j]['colour'] for j in G[i]])) #finds adjacent colours to node
    if 'never coloured' in adjacent_colours: #removes nodes without a colour
        adjacent_colours.remove('never coloured')
    next_colour = next(k for k, v in enumerate(sorted(adjacent_colours) + [None], 1) if k != v) #finds smallest number (colour) not in sorted adjacent_colours
    return next_colour


def greedy(G):
    global kmax

    kmax = 0 #initalises max number of colours used
    for i in G.nodes():
        next_colour = find_smallest_colour(G, i) #finds colour for node
        if next_colour > kmax: #if the colour is higher than current max colour updates kmax
            kmax = next_colour
        G.node[i]['colour'] = next_colour #assigns colour

    print()
    for i in G.nodes():
        print('vertex', i, ': colour', G.nodes[i]['colour'])
    print()
    print('The number of colours that Greedy computed is:', kmax)


print('Graph G1:')
G=graph1.Graph()
greedy(G)


print('Graph G2:')
G=graph2.Graph()
greedy(G)


print('Graph G3:')
G=graph3.Graph()
greedy(G)


print('Graph G4:')
G=graph4.Graph()
greedy(G)


print('Graph G5:')
G=graph5.Graph()
greedy(G)
