# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 10:12:43 2017

@author: Ramil Sharifsoy
"""

"""
Question 1: Given two strings s and t, determine whether some anagram 
of t is a substring of s. For example: if s = "udacity" and t = "ad", 
then the function returns True. Your function definition should look
like: question1(s, t) and return a boolean True or False.
"""

""" 
Solution:  
    1. Accept input as a string
    2. Convert string to list and sort  those lists
    3. Compared sorted lists. Regardless of initial configuration of 
    letters, sorted lists will match if they are same.
"""

def is_anagrammer(string1, string2):
    string1_list = list(string1)
    string1_list.sort()
    string2_list = list(string2)
    string2_list.sort()
    return string1_list == string2_list

"""
Slice "s" into sections with legth of "t" and compare each sorted slice 
of "s" with sorted "t". If there is match print True, if not False.
"""

def question1(stringS, testT):
    testT_length = len(testT)
    stringS_length = len(stringS)
    for i in range(stringS_length - testT_length + 1):         # Limit counter to number of slices
        print (stringS[i: i+testT_length], testT)              # Print slices of stringS with testT
        if is_anagrammer(stringS[i: i+testT_length], testT):   # End loop and return True if there is match
            return True
    return False

print (question1("udacity", "ad"))  # True
print (question1("udacity", "ram")) # False

"""
Reference: https://github.com/bradd123/udacity-technical-interview-practice/blob/master/1.py
"""