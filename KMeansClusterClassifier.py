# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 02:08:03 2021

@author: ankok
"""

import random
import math


class KMeansClusterClassifier():
    
    def __init__(self, n_cluster):
        self.n_cluster = n_cluster
        self.cluster_centers = 0
    
    def fit(self,X):

        dim = len(X[0]) 
        max_iter = 100
        i = 0
        cluster = [0] * len(X)
        prev_cluster = [-1] * len(X)
        
        cluster_centers = []
        for i in range(0,self.n_cluster):
            cluster_centers += [random.choice(X)]           
            recall = False
        
        while (cluster != prev_cluster) or (i > max_iter) or (recall) :
            
            prev_cluster = list(cluster)
            recall = False
            i += 1
        
            for z in range(0,len(X)):
                min_dist = float("inf")
                
                for c in range(0,len(cluster_centers)):
                    
                    dist = self.eucldist(X[z],cluster_centers[c])
                    
                    if (dist < min_dist):
                        min_dist = dist  
                        cluster[z] = c   
            
            for k in range(0,len(cluster_centers)):
                new_center = [0] * dim
                m = 0
                for z in range(0,len(X)):
                    if (cluster[z] == k): 
                        for j in range(0,dim):
                            new_center[j] += X[z][j]
                        m += 1
                
                for j in range(0,dim):
                    if m != 0:
                        new_center[j] = new_center[j] / float(m) 
                    
                    else: 
                        new_center = random.choice(X)
                        recall = True
                    
                cluster_centers[k] = new_center
        
        self.cluster_centers = cluster_centers

        
   
    def predict(self,test):
       index = [] 
       
       for z in range(0,len(test)):
            min_dist = float("inf")
            
            for c in range(0,len(self.cluster_centers)):
                dist = self.eucldist(test[z],self.cluster_centers[c])
                
                if (dist < min_dist):
                    min_dist = dist  
                    min_index = c 
            index.append(min_index)
       return index

    def eucldist(self,d0,d1):
        dist = 0.0
        for i in range(0,len(d0)):
            dist += (d0[i] - d1[i])**2
        return math.sqrt(dist)
            

