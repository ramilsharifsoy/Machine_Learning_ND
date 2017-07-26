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
    def nthNodeFromLast(self, m):
        main_ptr = self.head
        ref_ptr = self.head 
     
        count = 0
        if(self.head is not None):
            while(count < m):
                if(ref_ptr is None):
                    print ("\n ERROR: %d is greater than the no. of nodes in list" % (m))
                    return
  
                ref_ptr = ref_ptr.next
                count += 1
 
        while(ref_ptr is not None):
            main_ptr = main_ptr.next
            ref_ptr = ref_ptr.next
        
        return main_ptr
    
# main
def question5(ll, m):
    if ll:
        return ll.nthNodeFromLast(m)

# setup nodes
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

# setup LinkedList
ll = LinkedList(n1)
ll.append(n2)
ll.append(n3)
ll.append(n4)
ll.append(n5)

m = 5
answer = question5(ll, m) # expect 3
print ("\n Node in linked list that is {} steps from the end is {}".format(m, answer.data))

# edge testcase-1
m = 99
answer = question5(ll, m) # expect ERROR: 99 is greater than the no. of nodes in list

# edge testcase-2
ll = None
m = 3
answer = question5(ll, m) # expect None
print ("\n Node in linked list that is {} steps from the end is {}".format(m, answer))

"""
Refernce:
    [1] http://www.openbookproject.net/thinkcs/python/english2e/ch18.html
    [2] http://interactivepython.org/UhZmZ/courselib/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html
    [3] https://github.com/srikanthpagadala/udacity/tree/master/Machine%20Learning%20Engineer%20Nanodegree/Technical%20Interview%20Practice
"""