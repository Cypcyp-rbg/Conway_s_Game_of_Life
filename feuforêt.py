#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.colors as colors
import matplotlib.pyplot as plt
from random import *
import math 

#création de la grille
largeur_grille = 50
x = [0 for i in range (largeur_grille)]
y = []

for i in range (largeur_grille):
    y.append(x)
        
grille = np.array(y)

#remplissage de la grille
i=0
while i<largeur_grille:
     j=0
     while j<largeur_grille:
        P = random()
        if P<0.8:
            grille[i,j]=0
        else:
            grille[i,j]=-1
        j+=1
     i+=1
     


def voisin(x,y,M):
    voisins=[]
    if M[x-1,y]==-2:
        voisins.append(M[x-1,y])
    if M[x,y+1]==-2:
        voisins.append(M[x,y+1])
    if M[x,y-1]==-2:
        voisins.append(M[x,y-1])
    if M[x+1,y]==-2:
        voisins.append(M[x+1,y])
    somme = sum(voisins)
    return somme



cmap = colors.ListedColormap(['red','white','green','grey']) 
boundaries = [-2,-1,0,1,2]
norm = colors.BoundaryNorm(boundaries, cmap.N, clip=True)



for a in range(3):
    X = randrange(0,largeur_grille-1,1)
    Y = randrange(0,largeur_grille-1,1)
    grille[X,Y]=-2

fig = plt.imshow(grille,cmap=cmap,norm=norm)
plt.xticks([])
plt.yticks([])
plt.show()
plt.pause(0.02)

grille1 = np.array(y)

t=0
while t<50:
    
    i=0
    while i<largeur_grille-1:
        j=0
        while j<largeur_grille-1: 
            
            if grille[i,j] == 0 and voisin(i,j,grille)==0:
                grille1[i,j]=0
            if grille[i,j] == 1 or grille[i,j]==-1:
                grille1[i,j]=grille[i,j]    
            if grille[i,j] == -2:
                grille1[i,j] = 1
            if grille[i,j] == 0 and voisin(i,j,grille) <= -2:
                grille1[i,j] = -2
            j+=1
        i+=1
      
    fig = plt.imshow(grille,cmap=cmap,norm=norm)
    plt.xticks([])
    plt.yticks([])
    plt.pause(0.02)
    grille = grille1
    grille1 = np.array(y)
    plt.show()           
    t+=1
   

plt.close()













