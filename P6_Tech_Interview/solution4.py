# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 13:21:10 2017
@author: Ramil Sharifsoy
"""

"""
Question 4:

Find the least common ancestor between two nodes on a binary search tree. 
The least common ancestor is the farthest node from the root that is an 
ancestor of both nodes. For example, the root is a common ancestor of all 
nodes on the tree, but if both nodes are descendents of the root's left child, 
then that left child might be the lowest common ancestor. You can assume 
that both nodes are in the tree, and the tree itself adheres to all BST 
properties. The function definition should look like question4(T, r, n1, n2), 
where T is the tree represented as a matrix, where the index of the list is 
equal to the integer stored in that node and a 1 represents a child node, r 
is a non-negative integer representing the root, and n1 and n2 are non-negative 
integers representing the two nodes in no particular order. For example, 
one test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)

and the answer would be 3.
"""
# Solution
"""
 T:       Tree Represented as a matrix
 r:       Non-negative integer representing the root
 n1, n2:  Non-negative integers representing the two nodes in no particular order
-------------------------------------------------------------------------------
 Let T be a rooted tree. The lowest common ancestor (LCA) between two nodes n1 and n2
 is defined as the lowest node in T that has both n1 an d n2 as descendants.[2]
-------------------------------------------------------------------------------
 Steps:
     1. Find parents of node 1
     2. Find which parent of node 2 shared with node 1
     3. Shared pared is the LCA
"""


def question4(T, r, n1, n2):

    n1_parents = []               # Initiate empty list to store ancestors of n1
    
    while n1 != r:                # Search when n1 is not root, otherwise return -1
        n1 = node_parent(T, n1) 
        n1_parents.append(n1)
    
    while n2 != r:                # Search when n2 is not root, otherwise return -1
        n2 = node_parent(T, n2) 
        if n2 in n1_parents:      # Find parents of n2 and compare with parents of n1
            return n2             # n2 parent in n1 parents is a common parent and is the LCA
    return -1
    
def node_parent(T, n):             # Return parent of node if it exists, otherwise return -1
    numrows = len(T)               # Search BST for 1s at [i][n] 
    for i in range(numrows):
        if T[i][n] == 1:
            return i               # i is the parent for matching [i][n]
    return -1

print ("Least common ancestor between two nodes is (root if -1)",
       question4([[0,1,0,0,0],
                 [0,0,0,0,0],
                 [0,0,0,0,0],
                 [1,0,0,0,1],
                 [0,0,0,0,0]],
                3,
                1,
                4))

"""
References:
    [1] http://www.geeksforgeeks.org/construct-tree-from-ancestor-matrix/
    [2] http://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/
    [3] http://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
    [4] http://www.geeksforgeeks.org/construct-a-binary-tree-from-parent-array-representation/ 
    [5] https://github.com/jldbc/Udacity/tree/master/Interview%20Prep
"""