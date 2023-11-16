import networkx as nx
import graph6
import graph7
import graph8
import graph9
import graph10


def bfs(G,a,b):
    G.add_nodes_from(G.nodes(), label = -1) # initialization of all labels
    G.nodes[a]['label'] = 0

    queue = [a] #initialises queue starting at a
    while len(queue) != 0: #runs until queue is empty and all nodes have been labeled
        a = queue.pop(0) #receives next node
        G.node[a]['visited'] = 'yes' #marks as visited
        for v in G.neighbors(a): #iterates through all neighbours of current node
            if G.node[v]['visited'] == 'no' and v not in queue: #if neighbour has not been visited and not already in queue then added to queue
                queue.append(v)
            if G.node[v]['label'] == -1: #if neighbour doesn't have a distance assigned to it, given distance of current node + 1
                G.node[v]['label'] = G.node[a]['label'] + 1
            elif G.node[a]['label'] + 1 < G.node[v]['label']: #checks if length of new path to neighbour is less than length of old path to neighbour
                G.node[v]['label'] = G.node[a]['label'] + 1
    return G.node[b]['label'] #returns distance to b


G6=graph6.Graph()
a=12
b=40
print('Graph G6:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G6,a,b))
print()


G7=graph7.Graph()
a=5
b=36
print('Graph G7:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G7,a,b))
print()


G8=graph8.Graph()
a=15
b=35
print('Graph G8:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G8,a,b))
print()


G9=graph9.Graph()
a=1
b=19
print('Graph G9:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G9,a,b))
print()


G10=graph10.Graph()
a=6
b=30
print('Graph G10:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G10,a,b))
print()
