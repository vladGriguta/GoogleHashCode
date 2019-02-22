import pandas as pd
import numpy as np

def maxTuples(a, n, m):
	for k in range (0, n):
		maxx = 0
		maxi = 0
		maxj = 0 
		for i in range (0, n):
			for j in range (0, m):
		                if a[i][j] > maxx:
    		                	maxx = a[i][j]
                    			maxi = i      
			              	maxj = j
		for i in range (0, m):
			a[maxi][i] = -1
    	        for j in range (0, n):
    			a[j][maxj] = -1  
		print (maxx, maxi, maxj)

maxTuples(matrix, n, m)