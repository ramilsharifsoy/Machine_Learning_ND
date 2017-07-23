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


# Solution:

"""
First make sure that both phrases entered.
 
With H Function, slice "s" into sections with legth of "t", feed slices of 
"s" with "t" to A Function. Which will sort and compare each slice of "s" 
with sorted "t".
"""

def question1(stringS, testT):                                 # H Function
    if stringS == "" or testT == "":
        return "Enter Both Words"      
    else:  
        testT_length = len(testT)
        stringS_length = len(stringS)
        for i in range(stringS_length - testT_length + 1):         # Limit counter to number of slices
          # print (stringS[i: i+testT_length], testT)              # Print slices of stringS with testT
            if is_anagrammer(stringS[i: i+testT_length], testT):   # End loop and return True if there is match
                return True
        return False

"""  
    1. Accept inputs as a strings
    2. Convert string to list and sort those lists
    3. Compared sorted lists. Regardless of initial configuration of 
    letters, sorted lists will match if they are same.
"""

def is_anagrammer(string1, string2):                          # A Function
    string1_list = list(string1)
    string1_list.sort()
    string2_list = list(string2)
    string2_list.sort()
    return string1_list == string2_list

# Test Code:
    
print (question1("udacity", "ad"))             # True
print (question1("udacity", "ram"))            # False
print (question1("udacity", " "))              # False
print (question1("udacity", "acid"))           # True
print (question1("udacity", ""))               # Enter Both Words
print (question1("", "udacity"))               # Enter Both Words
print (question1("udacity", "udacities"))      # t longer than s > False 


"""
Reference: https://github.com/bradd123/udacity-technical-interview-practice/blob/master/1.py
"""