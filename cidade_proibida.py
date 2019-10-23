from collections import defaultdict


class Grafo:
    def __init__(self, nVertices):
        # default dictionary para armazenar o grafo
        self.adjs = defaultdict(list)
        self.nVertices = nVertices
        # Inicializa todos os vértices
        for vertice in range(nVertices):
            self.adjs[vertice] = []
        # <<Conjuntos>> para Dijkstra
        self.fechado = [False] * nVertices
        self.aberto = [True] * nVertices

    def adiciona_aresta(self, u, v, peso):
        self.adjs[u].append((v, peso))
        self.adjs[v].append((u, peso))

    def dijkstra(self, inicio):
        distV = list(map(lambda x: 0 if x == inicio else float("inf"), range(self.nVertices)))
        # print(distV)

        self.adjs[inicio]
        while True in self.aberto:
            indiceMenor = self.aberto.index(True)
            # print(f"Aberto: {self.aberto}")
            # print(f"Fechado: {self.fechado}")
            # print(f"Distancias: {distV}")
            for dist in distV:
                if self.aberto[distV.index(dist)] and dist < distV[indiceMenor]:
                    indiceMenor = distV.index(dist)
                # print(f"Indice Menor: {indiceMenor}, dist: {distV.index(dist)}")
            # print(indiceMenor)
            self.aberto[indiceMenor] = False
            self.fechado[indiceMenor] = True

            vizinhos = [x for x in self.adjs[indiceMenor] if self.aberto[x[0]]]
            for vizinho in vizinhos:
                custo = min(distV[vizinho[0]], distV[indiceMenor] + vizinho[1])
                distV[vizinho[0]] = custo

        return distV

    def dijkstra_proibido(self, inicio, proibido):
        distV = list(map(lambda x: 0 if x == inicio else float("inf"), range(self.nVertices)))
        # print(distV)

        self.aberto[proibido] = False
        self.adjs[inicio]
        while True in self.aberto:
            indiceMenor = self.aberto.index(True)
            # print(f"Aberto: {self.aberto}")
            # print(f"Fechado: {self.fechado}")
            # print(f"Distancias: {distV}")
            for dist in distV:
                if self.aberto[distV.index(dist)] and dist < distV[indiceMenor]:
                    indiceMenor = distV.index(dist)
                # print(f"Indice Menor: {indiceMenor}, dist: {distV.index(dist)}")
            # print(indiceMenor)
            self.aberto[indiceMenor] = False
            self.fechado[indiceMenor] = True

            vizinhos = [x for x in self.adjs[indiceMenor] if self.aberto[x[0]]]
            for vizinho in vizinhos:
                custo = min(distV[vizinho[0]], distV[indiceMenor] + vizinho[1])
                distV[vizinho[0]] = custo

        return distV

# inicio = 0
# print(f"Distância do vértice {inicio} para todos os outros: \n{g.dijkstra(inicio)}")

if __name__ == "__main__":
    while True:
        try:
            entrada = input().strip().split(' ')
            N = int(entrada[0])
            M = int(entrada[1])
        except EOFError:
            break

        g = Grafo(N)
        # print(N, M)

        for vertice in range(M):
            entradaArestas = input().strip().split(' ')
            # Subtraindo 1 pois vértices do grafo começam do 0
            V = int(entradaArestas[0]) - 1
            W = int(entradaArestas[1]) - 1
            g.adiciona_aresta(V, W, 1)
            # print(V, W)

        entradaCidades = input().strip().split(' ')
        C = int(entradaCidades[0]) - 1
        R = int(entradaCidades[1]) - 1
        E = int(entradaCidades[2]) - 1
        # print(C, R, E)

        dists = g.dijkstra_proibido(C, E)
        # print(dists)
        distR = dists[R]
        # print(f"Distância de {C} até {R} sem passar por {E}: {distR}\n")
        print(distR)
