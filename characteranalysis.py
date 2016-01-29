# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 17:04:26 2014

@author: Evan Yao

Program that analyzes the character count of each person in a groupchat. 
"""

import matplotlib.pyplot as plt 
import numpy as np 

f = open("chat.txt", "r")

print "Enter the full facebook names of the people in this chat. Type 'done' to end" 

names = [] 

while (True):
    new_name = str(raw_input())
    if (new_name == 'done'):
        break
    else:
        names.append(new_name + '\n')    

h = f.readlines()

if (len(names) == 0):
    names = ['Sam Wu\n', 'Evan Yao\n', 'Frances Ding\n', 'Ignacio P. Bayardo\n', 'Cherie Hu\n']

freq = [0 for i in range(len(names))]

h = h[0].split('\r')

i = 0 

while i != len(h):
    
    if h[i] in names: 
,         index = names.index(h[i])
        
        i = i + 1

        while i != len(h) and h[i] not in names: 

            freq[index] += len(h[i])
            i = i + 1
    else: 
        i = i+1 
name = ['Sam', 'Evan', 'Frances', 'Nacho', 'Cherie']
x = np.arange(1, len(freq)+1)
width = 1
bar1 = plt.bar(x, freq, width, color="b" )
plt.ylabel( 'Total Number of Characters' )
plt.xlabel('Name of Person')
plt.xticks(x + 1/2.0, name)
plt.title('Lost Crew (FENS) + Cherie \n Groupchat Frequency')
plt.show()
