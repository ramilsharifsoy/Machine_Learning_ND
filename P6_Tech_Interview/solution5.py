# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 13:24:02 2017
@author: Ramil Sharifsoy
"""

"""
Question 5: Find the element in a singly linked list that's m elements from the end. 
For example, if a linked list has 5 elements, the 3rd element from the end 
is the 3rd element. The function definition should look like question5(ll, m), 
where ll is the first node of a linked list and m is the "mth number from the end". 
You should copy/paste the Node class below to use as a representation of a node in 
the linked list. Return the value of the node at that position.

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
"""

################################### Solution 5: ###############################

"""
    Use two pointers:
    One of two pointers marks the mth node from the beginning. At this point second
    pointers starts at the beginning. From here, both move together to next untill
    first pointer reaches the end. While first pointers reaches the end, second pointer
    reaches mth node from the end.
    
    Implementation Steps [4]:
    - Maintain two pointers – reference_pointer and main_pointer 
    - Initialize both reference and main pointers to head 
    - First move reference pointer to m nodes from head 
    - Next, move both pointers one by one until reference pointer reaches end 
    - Lastly, main pointer will point to nth node from the end. Return main pointer
"""
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

m = 1
answer = question5(ll, m) # Test Code
print ("Node {} is {} step(s) from the end.".format(answer.data, m))

m = 10
answer = question5(ll, m) # Error message test

"""
Refernce:
    [1] http://www.openbookproject.net/thinkcs/python/english2e/ch18.html
    [2] http://interactivepython.org/UhZmZ/courselib/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html
    [3] https://github.com/srikanthpagadala/udacity/tree/master/Machine%20Learning%20Engineer%20Nanodegree/Technical%20Interview%20Practice
    [4] http://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/
"""
###############################################################################