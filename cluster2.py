import os
import csv
from sklearn import datasets
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from scipy import * 
test=pd.read_csv("C:/Users/DELL/test.csv" ,sep=";" ,header=0)#recuperartion du fichier csv
test.fillna(test.mean(), inplace=True) # fonction permettant de remplacer toute les valeurs nulles par 0
#print("donne brute") #lescture donnee
print(test)
x = test.values #convertir en liste de sous liste les donn�es
#print("valeur totale")
#print(x)
#print("tableau de donne")
#print(test2)
test3=x[:,:8]#extraction des colonnes utilisable pour le kmean
#print("dernier extraction")# exclusion de la colonne Pathologies et pour celle de Patiente dea fai en haut
#print(test3)
#print(test3[5])
#print(test3[1])
print("\n")
L2 =dict()
def mafonction(tt):
 Kmean = KMeans(n_clusters=30) #definition du nombre de cluster a generer
 Kmean.fit(test3)
 print("liste centroide")
 print("\n")
 print(Kmean.cluster_centers_)#liste des valeurs des centroisdes 
 print("liste cluster")
 #print("liste clusters")
 #lab = input("afficher clustering oui ou non \n")
 #if lab == "oui":
 print(Kmean.labels_)#affichage de la liste des clusters 
 Pathologies=x[:,8:]
 #print(Pathologies) 
 #affcl = input("afficher clustering selon les patients oui ou non \n")
 #if affcl  == "oui":
 print("classement des clusters selon les patiente")
 for index, values in enumerate(Pathologies):
     for index2, value2 in enumerate(Kmean.labels_): 
        if (index == index2):
            s= values + ":::" + str(value2)
            print(s)
 L=dict()
 for index, value in enumerate(Pathologies):
    cluster = Kmean.labels_[index]
    if cluster in L.keys():
        L.get(cluster).append(value)
    else:
        l=list()
        l.append(value)
        L[cluster] = l
 #print(L)

 for index, value in enumerate(L):
    ch = L[value]
    #print(ch)
    ch2 = ch[0]
    ch3 = ch2[0] 
    #print(ch3)
    st = ch3
    #print(ch3)
    for index, value3 in enumerate(ch3): #parcours de liste de pathologies du cluster
       cluster = Kmean.labels_[index]  
    L2[cluster] = [st]
 #eti = input("afficher l'etiquettage? oui ou non \n")
 #if eti == "oui":
 print("etiquettage2")
 print(L2)

 #tt=input("enter un nouveau objet a predir \n") # nouveau objet a predir
 tt_int = (list(tt.strip()))
 erreur = " "
 ttt= Kmean.predict([tt_int])
 #print(ttt)
 #print("\n")
 return ttt

print("\n")
def nompredict(varprec):
    ttt2=mafonction(varprec)
    print(ttt2[0])
    for index, value3 in enumerate(L2):
   # print(value3)
     if (ttt2[0] == value3):
        s = L2[ttt2[0]]
        erreur = " " 
        break
    else:
        erreur = "pas de cluster correspondante"
    print(erreur)
    return str(s)

