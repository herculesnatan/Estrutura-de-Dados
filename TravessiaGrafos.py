from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue

def encontrar_caminhos(grafo, i, j, caminho_atual = []):
    caminhos = []
    caminho_atual = caminho_atual.copy() + [i]
    if i == j:
        return [caminho_atual]
    for vizinho in grafo.getVertex(i).getConnections():
        if vizinho.getId() not in caminho_atual:
            novos_caminhos = encontrar_caminhos(grafo, vizinho.getId(), j, caminho_atual)
            for novo_caminho in novos_caminhos:
                caminhos.append(novo_caminho)
    return caminhos

 	

g = Graph()
g.addEdge("i","x")
g.addEdge("i","w")
g.addEdge("i","y")
g.addEdge("w","x")
g.addEdge("y","z")
g.addEdge("x","z")
g.addEdge("x","f")
g.addEdge("x","A")
g.addEdge("A","f")
print(encontrar_caminhos(g,"i","f"))