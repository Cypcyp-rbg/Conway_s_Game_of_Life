#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#===============ISING MODEL============

import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from random import *
import math 

#création de la grille
largeur_grille = 50
x = [0 for i in range (largeur_grille)]
y = []

for i in range (largeur_grille):
    y.append(x)
        
grille = np.array(y)

#remplissage de la grille avec des -1 et 1 aléatoirement
i=0
while i<largeur_grille:
     j=0
     while j<largeur_grille:
        grille[i,j]=randrange(-1,2,2)
        j+=1
     i+=1

# affichage de la grille initiale
fig = plt.imshow(grille) 
plt.xticks([])
plt.yticks([])  
plt.show()

#Fonction pour calculer la magnétisation moyenne de la grille
def magnetisation(M):
    
    somme=0
    i=0
    while i<largeur_grille:
        j=0
        while j<largeur_grille:
            somme += M[i,j]
            j+=1
        i+=1

    av_magn = somme / (largeur_grille*largeur_grille)
    return(av_magn)    

ABSCISSE = []
ORDONNEE = []

#Algorithme de Metropolis pour T de 4K à 1K
T=4
while T!=0:
    t=0
    while t<100000:
        
        X=randrange(0,largeur_grille-1,1)
        Y=randrange(0,largeur_grille-1,1)
        
        a=grille[X,Y]
        b=grille[X+1,Y]
        c=grille[X-1,Y]
        d=grille[X,Y+1]
        e=grille[X,Y-1]
    
        E = -(a*b + a*c + a*d + a*e)
        NvE = (a*b + a*c + a*d + a*e)
        
        deltaE = (NvE - E)
        beta = 1/T
    
        
        P = random()
        Prob = math.exp(-beta*deltaE)
        
        if deltaE <=0:
            grille[X,Y]=-grille[X,Y]
        elif P<Prob:
            grille[X,Y]=-grille[X,Y]
        else:
            grille[X,Y]=grille[X,Y]
    
        
        
        t+=1
        
    fig = plt.imshow(grille) 
    plt.xticks([])
    plt.yticks([])  
    plt.show()    
    plt.close()
    ABSCISSE.append(T)
    ORDONNEE.append(magnetisation(grille))


    T-=1

plt.plot(ABSCISSE, ORDONNEE)
