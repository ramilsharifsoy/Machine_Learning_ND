# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 12:12:43 2017
@author: Ramil Sharifsoy
"""

"""
Given a string a, find the longest palindromic substring contained in a.
Your function definition should look like question2(a), and return a string.
"""

# Solution:
    
"""
1. Lowercase all input
2. Remove spaces to recognize sentences
3. Slice string in substrings
4. Feed slices to palindrome function to compare mirrored strings
"""

def Question2(string_a):
    
    string_a = string_a.lower()                       # Lowercase letters
    string_a = string_a.replace(" ", "")              # Remove Spaces
    string_a = string_a.replace(",", "")              # Remove commas
    
    for slice_s in substrings(string_a):              # String in > slice out
        if palindrome(slice_s):                       # Compare slice with its mirrored copy
            return slice_s

"""
5. Slice from the end and the begnning of the string
6. Move slice along the string
"""

def substrings(string_in):
    
    length_s = len(string_in)
    for backward in range(length_s, 0, -1):
        for forward in range(length_s - backward + 1):
            yield string_in[forward: forward + backward]

"""
7. Feed each slice to palindrome
"""

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

"""
Reference: https://codereview.stackexchange.com/questions/160142/finding-the-longest-palindromic-substring
"""