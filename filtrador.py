import csv
from scipy.spatial import Delaunay
from scipy.spatial import Delaunay, delaunay_plot_2d
import numpy as np
import matplotlib.pyplot as plt
with open('basecarpetas.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
dosmilveinte =[]
tipo=[]
lugar=[]
points=[]
Sininfo=0
#Es importante no intentar juntar los filtros
#Primer filtro Es para indicar el año
for i in data:
	if i[0]=="2020":
		dosmilveinte.append(i)
#Segundo filtro es para ver el tipo de delito
for j in dosmilveinte:
	if j[10]=="ROBO DE VEHÍCULO CON Y SIN VIOLENCIA":
	#if j[10]=="DELITO DE BAJO IMPACTO"
		tipo.append(j)
print("Numero de este tipo de delito en el año seleccionado",len(tipo))
#Buscamos en el sector que queramos.
for k in tipo:
	if k[14]=="IZTACALCO":
		lugar.append(k)
print("Numeros de delitos en la delegación seleccionada:",len(lugar))
#Preparamos la lista para poder utiliarla como coordenadas

for i in lugar:
    if i[16]!='NA' and i[17]!='NA':
        a=float(i[16])
        b=float(i[17])
        points.append([a,b])
    else:
        Sininfo+=1 #Variable que te dice en cuantos casos no fue reportado el lungar
pointsnp=np.array(points)
tri = Delaunay(pointsnp)
#print(tri.simplices)
delaunay_plot_2d(tri)
plt.plot(pointsnp[:, 0], pointsnp[:, 1], 'o')
plt.show()
