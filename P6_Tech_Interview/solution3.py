# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 12:55:38 2017
@author: Ramil Sharifsoy
"""

"""
Question 3: Given an undirected graph G, find the minimum spanning tree within G. 
A minimum spanning tree connects all vertices in a graph with the smallest 
possible total weight of edges. Your function should take in and return an 
adjacency list structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}

Vertices are represented as unique strings. The function definition should 
be question3(G)
"""
#############################################################################################################
"""
Steps:
    1. Extract vertices and edges into saperate lists
    2. Edges contain information about their beginning and ending vertices with weights
    3. Feed vertices and edges to Kruskal Algorithm and find MST 
"""
parent = {}
rank = {}

def make_set(vertice):            # For pseudocode of function MAKE SET go to reference [5]
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):                # For pseudocode of function FIND go to reference [5]
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):     # For pseudocode of function UNION go to reference [5]
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1


def kruskal(vertices, edges):     # For pseudocode of function KRUSKAL go to reference [4]
    minimum_spanning_tree = set()
    
    for vertice in vertices:
        make_set(vertice)

    edges = sorted(edges, key = lambda x : x[2])     # Convert str into int and sort edges
    
    for edge in edges:
        vertice1, vertice2, wt = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)   
    return minimum_spanning_tree


def question3(G):
    
    Graph = G
    Vertices = []
    Edges = []

    for Vertice in Graph.keys():                             # Extract all vertices and edges
        
        Vertices.append(Vertice)                             # List of all vertices from Graph keys
        VerticeToVertices = Graph[Vertice]                   # List of directions of weights from Graph values
        
        for VerticeToVertice in VerticeToVertices:
            StartVertice = Vertice                           # Define starting verice
            EndVertice, Weight = VerticeToVertice            # Extract weights of edges and destination vertice
            Edges.append((StartVertice, EndVertice, Weight)) # Collect Enges with start, end, and weight info
        
    MST = kruskal(Vertices, Edges)                       # perform Kruskal algorithm to find MST
    
    
    Q3_Answer_MST = {}
    for MST_Edge in MST:                                     # Question 3 requred answer format
        StartVertice, EndVertice, Weight = MST_Edge
        
        if EndVertice < StartVertice:                        # Make sure vertices ordered alphabetically
            StartVertice = MST_Edge[1]
            EndVertice = MST_Edge[0]

        if StartVertice in Q3_Answer_MST:
            Q3_Answer_MST[StartVertice].append((EndVertice, Weight))  # Add next end point with weight
        else:
            Q3_Answer_MST[StartVertice] = [(EndVertice, Weight)]  # Create key with desired values
            
    return Q3_Answer_MST

import pprint
pp = pprint.PrettyPrinter(indent=5)

G = {'A': [('B', 2), ('C', 4)],
     'B': [('A', 2), ('D', 3), ('E', 4)],
     'C': [('B', 1), ('B', 5), ('D', 6)],
     'D': [('B', 7), ('E', 2)],
     'E': [('B', 2)]}

print ("\n Input Graph:") 
pp.pprint(G)
print("\n Minimum Spanning Tree of Input Graph with Kruskal Algorithm:\n", "MST =", question3(G))

"""
References: 
    [1] https://www.ics.uci.edu/~eppstein/161/960206.html
    [2] https://codereview.stackexchange.com/questions/128479/graph-and-minimum-spanning-tree-in-python
    [3] https://github.com/srikanthpagadala/udacity/tree/master/Machine%20Learning%20Engineer%20Nanodegree
    [4] https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
    [5] https://en.wikipedia.org/wiki/Disjoint-set_data_structure
"""