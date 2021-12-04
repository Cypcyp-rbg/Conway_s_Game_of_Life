#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from random import *
import math 

#création de la grille
largeur_grille = 10
x = [0 for i in range (largeur_grille)]
y = []

for i in range (largeur_grille):
    y.append(x)
        
grille = np.array(y)

mines = np.array(y)

bombe = 0
while bombe<20:
    i = randrange(0,largeur_grille-1,1)
    j = randrange(0,largeur_grille-1,1)
    mines[i,j]=1
    bombe += 1
     

def voisin(x,y,M):
    voisins=[]
    
    voisins.append(M[x-1,y])
    voisins.append(M[x-1,y+1])
    voisins.append(M[x-1,y-1])
    voisins.append(M[x,y+1])
    voisins.append(M[x,y-1])
    voisins.append(M[x+1,y])
    voisins.append(M[x+1,y+1])
    voisins.append(M[x+1,y-1])
        
    somme = sum(voisins)
    return somme

fig = plt.imshow(grille)
# plt.xticks([])
# plt.yticks([])
plt.show()

continuer = 1
while continuer:
    print ('Où voulez-vous creuser ?')
    X = int(input())
    Y = int(input())
    if X<largeur_grille-1 and Y<largeur_grille-1:
        print(X, 'pas en bas !', Y, 'pas à droite !')
        
        if mines[X,Y]==1:
             print('LOSE')
             continuer = 0
            
        else:
            if voisin(X,Y,mines)==0 and mines[X,Y]==0:
                grille[X,Y]=1
            
            else:
                if voisin(X,Y,mines) != 0 and mines[X,Y]==0:
                    grille[X,Y]=voisin(X,Y,mines)
                    print(voisin(X,Y,mines))
            
               
        
        fig = plt.imshow(grille,cmap=plt.cm.winter)
        cb = plt.colorbar(fig,shrink=0.5)
        cb.set_label('Bombes à proximité')
        # plt.xticks([])
        # plt.yticks([])
        plt.show()
    else:
        print('Trop loin !')
    
plt.close()
