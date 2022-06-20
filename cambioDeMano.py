import networkx as nx
import matplotlib.pyplot as plt


#lectura de archivo de entrada
data=""

with open("entrada.txt") as file:
    data = file.read()

esquinasTotales = esquinaColectivo = esquinaEscuela = callesTotales = 0
calles = []

data = data.split("\n")
for line in data:
    iteracion = data.index(line)
    if(iteracion == 0):
        esquinasTotales, esquinaColectivo, esquinaEscuela = line.split(" ")
    elif(iteracion == 1):
        callesTotales = line
    else:
        temp=line.split(" ")
        calles.append(temp)

#Se cargan las aristas y los vertices
aristas=[]
diferentesVertices = set()
for calle in calles:
    aristas.append([calle[0], calle[1], int(calle[2])])
    diferentesVertices.add(calle[0])
    diferentesVertices.add(calle[1])


vertice=list(diferentesVertices)


#creacion de grafo
GrafoD = nx.DiGraph()
GrafoD.add_nodes_from(vertice)
GrafoD.add_weighted_edges_from(aristas)
GrafoND = nx.Graph()
GrafoND.add_nodes_from(vertice)
GrafoND.add_weighted_edges_from(aristas)

recorridoMasCorto=nx.dijkstra_path(GrafoND, esquinaColectivo, esquinaEscuela)
recorridoNormal=nx.dijkstra_path(GrafoD, esquinaColectivo, esquinaEscuela)
costeMenor = nx.dijkstra_path_length(GrafoND, esquinaColectivo, esquinaEscuela)




#Se carga el array con los nodos a cambiar
nodosACambiar = []
for nodo in recorridoMasCorto:
    if(nodo not in recorridoNormal):
        nodosACambiar.append(int(nodo)+2)

#Se carga el array con las calles a cambiar de sentido
callesACambiarSentido=[]
for calle in calles:
    if(int(calle[0]) in nodosACambiar):
        callesACambiarSentido.append(calles.index(calle)+1)




# print(calles)   
# print("Recorrido Normal:",recorridoNormal)
# print("Recorrido Mas Corto:",recorridoMasCorto)
# print(nodosACambiar)
# print(callesACambiarSentido)


#Creacion de archivo de salida
f = open("salida.txt", "w")
f.write(str(costeMenor)+"\n")
for calle in callesACambiarSentido:
    f.write(str(calle)+ (" "))
f.close()




#Se grafica el grafo

#print("Grafo no Dirigido:",(nx.dijkstra_path(GrafoND, esquinaColectivo, esquinaEscuela)))
# print(nx.dijkstra_path_length(GrafoND, esquinaColectivo, esquinaEscuela))
#print("Grafo Dirigido:",(nx.dijkstra_path(GrafoD, esquinaColectivo, esquinaEscuela)))
#print(nx.dijkstra_path_length(GrafoD, esquinaColectivo, esquinaEscuela))

#nx.draw(GrafoND, pos=nx.circular_layout(GrafoND), node_color='r', edge_color='b', with_labels=True)
#nx.draw(GrafoD, pos=nx.circular_layout(GrafoND), node_color='r', edge_color='b', with_labels=True)

#plt.show()