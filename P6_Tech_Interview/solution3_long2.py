# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 13:19:22 2017

@author: Dumanisi
"""

from collections import defaultdict

class Graph:

    def __init__(self,vertices):
        self.V= vertices
        self.graph = []

    def Edge(self,u,v,w):
        self.graph.append([u,v,w])

    # A utility function to find set of an element i
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # A function that does union of two sets of x and y
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of high rank tree
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        # If ranks are same, then make one as root and increment rank by one
        else :
            parent[yroot] = xroot
            rank[xroot] += 1

    # The main function to build the MST
    def Question3(G):

        MST =[] # This will store the MST
        e = 0 # An index variable used for MST[]
        i = 0 # An index variable for sorted edges
        G.graph =  sorted(G.graph,key=lambda item: item[2])

        parent = [] ; rank = []

        # Create V subsets with single elements
        for node in range(G.V):
            parent.append(node)
            rank.append(0)

        # Edges to be taken is equal to V-1
        while e < G.V -1 :

            # Take smallest edge and increment the index
            u,v,w =  G.graph[i]
            i = i + 1
            x = G.find(parent, u)
            y = G.find(parent ,v)

            # If including this edge does't cause cycle, include it
            # in result and increment the index of result for next edge
            if x != y:
                e = e + 1
                MST.append([u,v,w])
                G.union(parent, rank, x, y)
            # Else discard the edge
        print ("Minimum Spanning Tree")
        for u,v,weight  in MST:
            print ("%d -- %d == %d" % (u,v,weight))

g = Graph(4)
g.Edge(0, 1, 9)
g.Edge(0, 2, 6)
g.Edge(0, 3, 5)
g.Edge(1, 3, 12)
g.Edge(2, 3, 4)
g.Question3()
print (g.Question3())