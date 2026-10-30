#Activdad 10
from collections import deque

grafo = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}

def bfs(inicio, meta):
    cola = deque([[inicio]])
    visitados = set()

    while cola:
        camino = cola.popleft()
        nodo = camino[-1]

        if nodo == meta:
            return camino

        if nodo not in visitados:
            visitados.add(nodo)

            for vecino in grafo[nodo]:
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)

ruta = bfs("A", "D")

print("Ruta encontrada:")
for lugar in ruta:
    print(lugar)