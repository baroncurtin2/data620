#This code adapted from here:
#https://raw.githubusercontent.com/mesarpe/sonetor/master/graphs/facebook.py

#Load libraries.

import networkx as nx
import matplotlib.pyplot as plt

#Create an empty graph.

g = nx.Graph()

#Set path to input files.
#Source: Explanation https://snap.stanford.edu/data/ego-Facebook.html.
#Actual download https://snap.stanford.edu/data/facebook.tar.gz.
#For this homework, let's just use the part of the network where all nodes in the edges and circles files are connected to node 0.

edges_file = "facebook/0.edges"
circles_file = "facebook/0.circles"

#Set node to 0.

node = 0

#Read in edges file.

content = open(edges_file,'r').read()
lines = content.split('\n')

#Run through the file line by line.
#If line is non-empty, should have two columns.
#For each column, create an edge between the values in the first and second columns.
#Also create edges for each of these values back to node 0.

for l in lines:
    if l != '':
        d = l.split(' ')
        g.add_edge(int(d[0]), int(d[1])) #Int = convert to numeric from string.
        g.add_edge(int(node), int(d[0]))
        g.add_edge(int(node), int(d[1]))

#Read in circles file.

content = open(circles_file,'r').read()
lines = content.split('\n')

#Run through the file line by line.
#The first column of this file just has a row number, basically.
#Then have anywhere from one to many (100+) additional columns, giving node IDs.
#Each of the values in these additional columns are connected to node 0.

for l in lines:
    if l != '':
        nodes = l.split('\t')[1:]
        [g.add_edge(int(node), int(n)) for n in nodes]

#For each possible combination of nodes, check the shortest path between them.
#Run through all these combinations in a for loop. If we encounter a shortest path that is longer than we have seen previously, that is now our new "longest shortest path".

longest_shortest_path = -1

nodes_list = g.nodes()

for node1 in nodes_list:
    for node2 in nodes_list:
        m = nx.shortest_path_length(g, node1, node2)
    if m > longest_shortest_path:
        longest_shortest_path = m

print(longest_shortest_path)

#Result: 2. For this very simple network, makes sense. Longest shortest path would be from 0 to one of the first column values in the ".edges" file to one of the second column values from the same line in the ".edges" file.


