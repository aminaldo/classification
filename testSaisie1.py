from scipy import *
from xml.dom import minidom
import cluster2
import xml.etree.ElementTree as ET
import os

tab = [0, 0, 0, 0, 0, 0, 0, 0]
n=0
doc = minidom.parse("staff.xml")

staffs = doc.getElementsByTagName("staff")
maliste = ""

for staff in staffs:

        nom = staff.getElementsByTagName("nom")[0]

        tab[n]=maliste+nom.firstChild.data
        n= n+1 


obj=[0, 0, 0, 0, 0, 0, 0, 0]
#print (tab)
def percoure(tab):
 nbb=len(tab)
 for j in range(nbb):
  obj[j]=tab[j]
  objStr = ''.join(map(str, obj))
 varesult=cluster2.nompredict(objStr)
 print(varesult)
 return varesult

percoure(tab)


varres=percoure(tab)

p = ET.Element('resul')

#c = ET.SubElement(p, 'staff')
p.text = varres
ET.dump(p)

os.remove("resul.xml")

tree = ET.ElementTree(p)
#ET.Element.set(p, 'attribute_value')
tree.write("resul.xml")
