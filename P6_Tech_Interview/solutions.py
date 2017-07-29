################################### Solution 1: ###############################

def question1(stringS, testT):                                     # H Function
    if stringS == "" or testT == "" or stringS == " " or testT == " ":
        return "Enter Both Words"      
    else:  
        testT_length = len(testT)
        stringS_length = len(stringS)
        for i in range(stringS_length - testT_length + 1):         # Limit counter to number of slices
            if is_anagrammer(stringS[i: i+testT_length], testT):   # End loop and return True if there is match
                return True
        return False

def is_anagrammer(string_1, string_2):                          # A Function
    counter_1 = [0]*26
    counter_2 = [0]*26

    for i in range(len(string_1)):
        position = ord(string_1[i])-ord('a')
        counter_1[position] = counter_1[position] + 1

    for i in range(len(string_2)):
        position = ord(string_2[i])-ord('a')
        counter_2[position] = counter_2[position] + 1

    j = 0
    ItIsAnagram = True
    while j<26 and ItIsAnagram:
        if counter_1[j] == counter_2[j]:
            j = j + 1
        else:
            ItIsAnagram = False

    return ItIsAnagram

# Test Code:
print (question1("udacity", "ad"))             # True
print (question1("udacity", "ram"))            # False
print (question1("udacity", " "))              # False
print (question1("udacity", "acid"))           # True
print (question1("udacity", ""))               # Enter Both Words
print (question1("", "udacity"))               # Enter Both Words
print (question1("udacity", "udacities"))      # t longer than s > False 

################################### Solution 2: ###############################

def Question2(string_a):
    
    string_a = string_a.lower()                       # Lowercase letters
    string_a = string_a.replace(" ", "")              # Remove Spaces
    string_a = string_a.replace(",", "")              # Remove commas
    
    for slice_s in substrings(string_a):              # String in > slice out
        if palindrome(slice_s):                       # Compare slice with its mirrored copy
            return slice_s

def substrings(string_in):
    
    length_s = len(string_in)
    for backward in range(length_s, 0, -1):
        for forward in range(length_s - backward + 1):
            yield string_in[forward: forward + backward]

def palindrome(mirror_s):
    return mirror_s == mirror_s[::-1]

print (Question2(""))
print (Question2(" "))
print (Question2("I"))
print (Question2("I love bananas !!!"))
print (Question2("Bananas that I saw!!!"))
print (Question2("I drive a racecar !!!"))
print (Question2("A nut for a jar of tuna."))
print (Question2("Was it a car or a cat I saw?"))
print (Question2("Murder for a jar of red rum."))
print (Question2("Gateman sees name, garageman sees nametag."))

################################### Solution 3: ###############################

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

G1 = {'A': [('B', 2), ('C', 4)],
     'B': [('A', 2), ('D', 3), ('E', 4)],
     'C': [('B', 1), ('B', 5), ('D', 6)],
     'D': [('B', 7), ('E', 2)],
     'E': [('B', 2)]}

print ("\n Input Graph:") 
pp.pprint(G1)
print("\n Minimum Spanning Tree of Input Graph with Kruskal Algorithm:\n", "MST =", question3(G1))

G2 = {'A': [('C', 1)],
     'B': [('A', 2)],
     'C': [('B', 3)],
     'D': [('E', 4)],
     'E': [('B', 5)]}

print ("\n Input Graph:") 
pp.pprint(G2)
print("\n Minimum Spanning Tree of Input Graph with Kruskal Algorithm:\n", "MST =", question3(G2))

G3 = {} # Empty Input, expect empty output

print ("\n Input Graph:") 
pp.pprint(G3)
print("\n Minimum Spanning Tree of Input Graph with Kruskal Algorithm:\n", "MST =", question3(G3))

################################### Solution 4: ###############################

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

################################### Solution 5: ###############################

# linked list node
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
   
# linked list 
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_node):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
    
    def mthElementFromTheEnd(self, m): # Setting both pointers to head
        main_pointer = self.head
        reference_pointer = self.head 
     
        count = 0
        if(self.head is not None): # Moving reference pointer to mth node from the beginning
            while(count < m):
                if(reference_pointer is None):
                    print ("ERROR: %d is greater than the number of nodes in the list." % (m))
                    return
  
                reference_pointer = reference_pointer.next
                count += 1
 
        while(reference_pointer is not None): # Moving pointers together
            main_pointer = main_pointer.next
            reference_pointer = reference_pointer.next
        
        return main_pointer
    
def question5(ll, m): # Main Function
    if ll:
        return ll.mthElementFromTheEnd(m)

# List of nodes
node_1 = Node('A') 
node_2 = Node('B')
node_3 = Node('C')
node_4 = Node('D')
node_5 = Node('E')
node_6 = Node('F')
node_7 = Node('G')
node_8 = Node('H')
node_9 = Node('I')

# Linked List of Nodes
ll = LinkedList(node_1)
ll.append(node_2)
ll.append(node_3)
ll.append(node_4)
ll.append(node_5)
ll.append(node_6)
ll.append(node_7)
ll.append(node_8)
ll.append(node_9)

m = 6
answer = question5(ll, m) # Test Code
print ("Node {} is {} step(s) from the end.".format(answer.data, m))

m = 8
answer = question5(ll, m) # Test Code
print ("Node {} is {} step(s) from the end.".format(answer.data, m))

m = 10
answer = question5(ll, m) # Error message test


###############################################################################