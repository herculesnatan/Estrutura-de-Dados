from pythonds.graphs import PriorityQueue, Graph, Vertex

def dijkstra(inicio):
    fila = PriorityQueue()
    fila.add(inicio,0)
    inicio.setDistance(0)

    while not fila.isEmpty():
        atual_Vert = fila.delMin()
        atual_Vert.setColor("gray")

        for prx_Vert in atual_Vert.getConnections():
            if atual_Vert.getColor() == "white":
                nova_distancia =atual_Vert.getDistance() + atual_Vert.getWeight(atual_Vert)

                if nova_distancia < atual_Vert.getDistance():
                    atual_Vert.setDistance(nova_distancia)
                    atual_Vert.setPred(atual_Vert)

                    fila.decreaseKey(atual_Vert, nova_distancia)
    

"""
Complexidade O(VE log V)
"""