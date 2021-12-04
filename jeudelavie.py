#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#============JEU DE LA VIE===========

import numpy as np
import matplotlib
from matplotlib import pyplot as plt

#création de la grille
largeur_grille = 101
x = [0 for i in range (largeur_grille)]
y = []

for i in range (largeur_grille):
    y.append(x)
        
grille = np.array(y)

if largeur_grille%2==1:
    a = (largeur_grille-1)//2
else:
    print('ERREUR')


#créeation d'une fonction permettant de calculer pour une cellule donnée le nombre de voisins vivants autour
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

'''
#Configuration des 5 cellules vivantes alignées
grille[a,a]=1
grille[a-1,a]=1
grille[a+1,a]=1 
grille[a-2,a]=1
grille[a+2,a]=1
'''

#Configuration du canon à planneurs
grille[a,a]=1
grille[a-1,a]=1
grille[a+1,a]=1 
grille[a,a-1]=1
grille[a+1,a+1]=1 

'''
#Configuration finale
grille[5,1]=1
grille[6,1]=1
grille[5,2]=1
grille[6,2]=1

grille[5,11]=1
grille[6,11]=1
grille[7,11]=1
grille[4,12]=1
grille[8,12]=1
grille[3,13]=1
grille[9,13]=1
grille[3,14]=1
grille[9,14]=1

grille[6,15]=1

grille[4,16]=1
grille[8,16]=1
grille[5,17]=1
grille[6,17]=1
grille[7,17]=1
grille[6,18]=1

grille[3,21]=1
grille[4,21]=1
grille[5,21]=1
grille[3,22]=1
grille[4,22]=1
grille[5,22]=1
grille[2,23]=1
grille[6,23]=1

grille[1,25]=1
grille[2,25]=1
grille[6,25]=1
grille[7,25]=1

grille[3,35]=1
grille[4,35]=1
grille[3,36]=1
grille[4,36]=1
'''

#création d'une 2e grille dans laquelle je viens mettre les modifications de la première grille en suivant les règles du jeu de la vie
X = [0 for i in range (largeur_grille)]
Y = []

for i in range (largeur_grille):
    Y.append(X)
        
grille1 = np.array(Y)

#création de boucles pour mettre en place les conditions qui régissent le jeu de la vie
t=0
while t<200:
    i=0
    while i<largeur_grille-1:
        j=0
        while j<largeur_grille-1:  
            if voisin(i,j,grille)>3 and grille[i,j]==1:
                grille1[i,j]=0
            if voisin(i,j,grille)==3 and grille[i,j]==0:
                grille1[i,j]=1
            if voisin(i,j,grille)<3 and grille[i,j]==0:
                grille1[i,j]=0   
            if voisin(i,j,grille)<2 and grille[i,j]==1:
                grille1[i,j]=0
            if voisin(i,j,grille)==2 and grille[i,j]==1:
                grille1[i,j]=1
            if voisin(i,j,grille)==3 and grille[i,j]==1:
                grille1[i,j]=1
            j+=1
        i+=1    
  
#affichage de la grille avec la situation initiale (pour la première itération) et qui ensuite prendra les modifications    
    fig = plt.imshow(grille) 
    plt.xticks([])
    plt.yticks([])
    
    plt.pause(0.02)
#la grille initiale prend les valeur de la grille qui a porté les modifications
    grille=grille1
#la grille qui portera les modifications de la prochaine itération redevient pleine de 0
    grille1=np.array(Y)
    plt.show()
    t+=1

 
plt.close()
    
    
    
    
