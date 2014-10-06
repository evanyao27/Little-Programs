# -*- coding: utf-8 -*-
"""
Created on Thu May 01 02:42:20 2014

@author: Evan

Solves a game of 24, where you are given n numbers and you must 
make the number 24 using ALL n numbers exactly once. 

Plots the result in a histogram showing possible values from 0 through 50
"""
import itertools
import matplotlib.pyplot as plt 

inputs = map(int,raw_input().split())

possibles = []

def solve(solution, array, current):
    # print str(array) + "current: " + str(current) 
    if len(array) == 0: 
        possibles.append(current)
        if current == 24: 
            print solution
            return True
        else: 
            return False
    x = array.pop()
    a = solve("(" + solution + " + " + str(x) +")", array[::1], current + x)

    b = solve("(" + solution + " - " + str(x) +")", array[::1], current - x)

    c = solve("(" + solution + " * " + str(x) +")", array[::1], current * x)

    d = solve("(" + solution + " / " + str(x) +")", array[::1], current / float(x))
    
    return a or b or c or d

comb = itertools.permutations(inputs)

b = False
for c in comb: 
    array = list(c)
    start = array.pop()
    s = solve(str(start), array, start)
    if s: 
        print "Solution Exists"
        b = True
        break

if not b:
    print "Solution Doesn't Exist"

result = []

for i in range(50):
    result.append(possibles.count(i))


bar = plt.bar(range(50), result)
bar[24].set_color('r')
if result[24] > 0: 
    s = "24 Can Be Achieved" 
else: 
    s = "24 Cannot Be Achieved"
plt.title(s)
plt.ylabel("Frequency")
plt.xlabel("Value to Attain")
plt.show()