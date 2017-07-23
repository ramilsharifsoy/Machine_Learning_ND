# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 12:12:43 2017
@author: Ramil Sharifsoy
"""

"""
Given a string a, find the longest palindromic substring contained in a.
Your function definition should look like question2(a), and return a string.
"""
# Main function.
def Question2(a):
    a = a.lower()
    a = a.replace(" ", "")
    for l in substrings(a):
        if palindrome(l):
            return l

# Gives substrings of s in decending order.
def substrings(s):
    
    # Declare local variable for the length of s.
    length_s = len(s)

    # Here I chose range over xrange for python version compatibility.
    for end in range(length_s, 0, -1):
        for i in range(length_s-end+1):
            yield s[i: i+end]

# Define palindrome.
def palindrome(s):
    return s == s[::-1]

# Simple test case.
print (Question2("I love bananas !!!"))
print (Question2("I have a racecar !!!"))
print (Question2("A nut for a jar of tuna."))
print (Question2("Was it a car or a cat I saw?"))
print (Question2("Murder for a jar of red rum."))
print (Question2("Gateman sees name, garageman sees nametag."))

"""
Reference: https://codereview.stackexchange.com/questions/160142/finding-the-longest-palindromic-substring
"""