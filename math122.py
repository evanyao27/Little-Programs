# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 00:26:31 2014

@author: evanyao
"""
import itertools
import numpy as np 
import matplotlib.pyplot as plt

n = range(3)

def mod3(matrix):
    for i in range(2):
        for j in range(2):
            matrix[i,j] %= 3
    return matrix 
matrices = []
order = []

for p in itertools.product(n, repeat = 4):
    matrix = np.matrix([[p[0], p[1]], [p[2], p[3]]])
    if np.round(np.linalg.det(matrix)) % 3 == 0: 
        continue
    element = np.matrix([[p[0], p[1]], [p[2], p[3]]])
    i = 1
    while (not (element == np.matrix([[1,0],[0,1]])).all()):
        element = mod3(element * matrix)
        i+= 1
    matrices.append(matrix)
    order.append(i)

total = zip(matrices, order)
total.sort(key = lambda t: t[1])

for i in total: 
    print "Matrix: " 
    print i[0] 
    print "order = %d" % (i[1])
    print "------"

plt.hist(order)


    
