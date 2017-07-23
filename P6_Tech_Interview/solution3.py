# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 12:55:38 2017
@author: Ramil Sharifsoy
"""

'''
Question 3

Given an undirected graph G, find the minimum spanning tree within G. 
A minimum spanning tree connects all vertices in a graph with the smallest 
possible total weight of edges. Your function should take in and return an 
adjacency list structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}

Vertices are represented as unique strings. The function definition should 
be question3(G)
'''

def question3(Graph):
    vertices = Graph.keys() # Vertices are represented as unique strings
    
    p = {}   #parent node
    rank = {}
    for vertice in vertices:
        p[vertice] = vertice
        rank[vertice] = 0
    min_spanning_tree = []
    edges = []
	
    for node in vertices:
        edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if Graph.find(vertice1) != Graph.find(vertice2):
            Graph.union(vertice1, vertice2)
            min_spanning_tree.add(edge)
        return min_spanning_tree


TGraph = {'A':[('B',2)],
          'B':[('A',2),('C',5)],
          'C':[('B',5)]}

print (question3(TGraph))

"""
References: 
    https://www.ics.uci.edu/~eppstein/161/960206.html
    https://codereview.stackexchange.com/questions/128479/graph-and-minimum-spanning-tree-in-python
    https://github.com/jldbc/Udacity/blob/master/Interview%20Prep/Problem_3.py
"""