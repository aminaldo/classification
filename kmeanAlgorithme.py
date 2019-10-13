import os
import csv
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from scipy import *

test=pd.read_csv("C:/Users/aminaGueye/data.csv" ,sep=";" ,header=0)#recuperartion du fichier csv
test.fillna(test.mean(), inplace=True)# fonction permettant de remplacer toute les valeurs nulles par 0
print("donne brute") #lecture donnee
print(test)
#print("\n")
#print("\n") 
#print("\n")
#print(test.describe())
print("\n")
print("\n")
x = test.values #convertir en liste de sous liste les données
#print("valeur totale")
print(x)
test2=x[:,1:]
#print("\n")
print("\n")
print("\n")
#print("tableau de donne")
print(test2)
test3=test2[:,:71]#extraction des colonnes utilisable pour le kmean
print("dernier extraction")# exclusion de la colonne Pathologies et pour celle de Patiente dea fai en haut
#print(test3)
print("\n")
print("\n")
print("\n")
Kmean = KMeans(n_clusters=59) #definition du nombre de cluster a generer
Kmean.fit(test3)
print("liste centroide")
print("\n")
#print(Kmean.cluster_centers_)#liste des valeurs des centroisdes 
print("\n")
print("\n")
print("liste clusters")
print("\n")
print(Kmean.labels_)#affichage de la liste des clusters 
print("\n")
print("\n")

#print("AFFICHAGE LISTE PATHOLOGIES")
Pathologies=x[:,72:]
#print(Pathologies)
print("classement des clusters selon les patiente")
print("\n")
for index, values in enumerate(Pathologies):
    for index2, value2 in enumerate(Kmean.labels_):
        if (index == index2):
            s= values + ":::" + str(value2)
            print(s)
print("\n")
print("\n")
print("deuxiemme classements DE Cluster avec 'eensemble de ses pathologies ou groupe de patologies")
print("\n")
L=dict()
for index, value in enumerate(Pathologies):
    cluster = Kmean.labels_[index]
    if cluster in L.keys():
        L.get(cluster).append(value)
        
        
    else:
        l=list()
        l.append(value)
        L[cluster] = l
print(L)

print("\n")
print("\n")

print("etiquettage2")

print("\n")



L2 =dict()
for index, value in enumerate(L):
    ch = L[value]
    ch2 = ch[0]
    ch3 = ch2[0]
    #print(ch3)
    st = ch3[0:3]
    nb = 0
    for index, value3 in enumerate(ch3):#parcours de liste de pathologies du cluster
        if (ch3[nb]==","):#test il existe un separateur d , t si oui 
            st = st + ch3[nb+1:nb + 4]# pour chaque cluster on pren lesz 3 premiers lettrers de la pathologie ensuite concataner avec les pemies lettre de l'autre pathologie pour avoir le nom
        cluster = Kmean.labels_[index]
        
        nb = nb + 1
    L2[cluster] = [st]
print(L2)
print("\n")
print("\n")
tst = input("Entrez un cluster \n") # TESTE DE SAISIE  D'UN CLUSTER
tst_int = int(tst)
erreur = " "
