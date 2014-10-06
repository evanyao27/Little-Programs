# -*- coding: utf-8 -*-
"""
Created on Fri May 02 21:34:46 2014

@author: Evan
"""
import itertools 
import sys

print "Enter Max Rating"
maxRating = int(raw_input())

print "Enter Names of People (separated by space): "
names = raw_input().split()
numPeople = len(names)
ratings = [[0 for j in range(numPeople)] for i in range(numPeople)]

for i in range(numPeople): 
    print "-------------------------------------------------"
    print "The names IN ORDER are: " + str(names) 
    print "%s enter your utility (0-%d inclusive) in the order of the names above:" % (names[i], maxRating)
    
    ratings[i] = map(int, raw_input().split())
    for i in ratings[i]:
        if i < 0 or i > maxRating:
            print "YOU BIG FAT CHEATER!!!"
            sys.exit()
            
    if len(ratings[i]) != numPeople: 
        print "You didn't type the correct number of people!! START OVER!"
        sys.exit()
    else: 
        
        for i in range(30):
            print ""
            print "The previous entry is now hidden"       
        
print "-------------------------------------------------"
nC2 = numPeople * (numPeople - 1) / 26
nC3 = numPeople * (numPeople - 1) * (numPeople -2) / 6
nC4 = numPeople * (numPeople - 1) * (numPeople - 2) * (numPeople - 3) / 24

bank = [i for i in range(numPeople)]

weights = []
combinations = []
counter = 0

withs = [[] for i in range(numPeople)]

for i in itertools.combinations(bank, 2):
    first = i[0]
    second = i[1]
    combinations.append([first,second]) 
    
    for i in range(numPeople):
        if i in [first,second]:
            withs[i].append(counter)
    weights.append(ratings[first][second] + ratings[second][first])
    
    counter += 1
    
for i in itertools.combinations(bank, 3):
    first = i[0]
    second = i[1]
    third = i[2]
    combinations.append([first,second,third])
    
    for i in range(numPeople):
        if i in [first,second, third]:
            withs[i].append(counter)
            
    weights.append((ratings[first][second] + ratings[second][first] + ratings[first][third] + ratings[third][first] + ratings[second][third] + ratings[third][second])/2)
    counter += 1
    
for i in itertools.combinations(bank, 4):
    first = i[0]
    second = i[1]
    third = i[2]
    fourth = i[3]
    combinations.append([first,second,third,fourth])
    
    for i in range(numPeople):
        if i in [first,second, third, fourth]:
            withs[i].append(counter)
    weights.append((ratings[first][second] + ratings[second][first] +ratings[first][third] +ratings[third][first] +ratings[first][fourth] +ratings[fourth][first] +ratings[second][third] +ratings[third][second] +ratings[second][fourth] +ratings[fourth][second] +ratings[third][fourth] +ratings[fourth][third])/3)
    counter += 1

graph = [[] for i in range(len(combinations))] 

for i in range(len(graph)):
    sets = []
    for j in combinations[i]:
        sets.append(set(withs[j]))
    graph[i] = (list(set.union(*sets)))

def wis(current):
    if len(current) == 0: 
        return [0,[]]
        
    first = current[0]
    
    A = current[1:len(current)]
    B = current[1:len(current)]
    
    # Use that node
    for i in graph[first]:
        if i in A: 
            A.remove(i)
    
    use = wis(A)
    use_value = weights[first] + use[0]
   
    # Don't use that node 
    dontuse = wis(B)
    dontuse_value = dontuse[0]
    
    if use_value > dontuse_value: 
        return [use_value, use[1] + [first]]
    else: 
        return [dontuse_value, dontuse[1]]

arrangement= wis([i for i in range(len(combinations))])[1]

def printresult(i):
    result = combinations[i]
    print "----------------Rooming Together-----------------"
    for i in result:
        print names[i]
    

for i in arrangement:
    printresult(i)