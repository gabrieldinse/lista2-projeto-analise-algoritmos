import math

class HeapMin:

    def __init__(self):
        self.nos = 0
        self.heap = []

    def ad_custo(self, u, indice):
        self.heap.append([u, indice])
        self.nos += 1
        f = self.nos
        while True:
            if f == 1:
                break
            p = f // 2
            if self.heap[p-1][0] <= self.heap[f-1][0]:
                break
            else:
                self.heap[p-1], self.heap[f-1] = self.heap[f-1], self.heap[p-1]
                f = p

    def rem_custo(self):
        x = self.heap[0]
        self.heap[0] = self.heap[self.nos - 1]
        self.heap.pop()
        self.nos -= 1
        p = 1
        while True:
            f = 2 * p
            if f > self.nos:
                break
            if f + 1 <= self.nos:
                if self.heap[f][0] < self.heap[f-1][0]:
                    f += 1
            if self.heap[p-1][0] <= self.heap[f-1][0]:
                break
            else:
                self.heap[p-1], self.heap[f-1] = self.heap[f-1], self.heap[p-1]
                p = f
        return x

    def tamanho(self):
        return self.nos

class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def ad_pedagio(self, u, v, peso):
        self.grafo[u-1][v-1] = peso
        self.grafo[v-1][u-1] = peso

    def mostra_localizacao_e_peso_pedagios(self):
        print('Mapa dos pedagios:')
        for i in range(self.vertices):
            print(self.grafo[i])

    def dijkstra(self, origem):
        custo_vem = [[-1, 0] for i in range(self.vertices)]
        custo_vem[origem - 1] = [0, origem]
        h = HeapMin()       
        h.ad_custo(0, origem)
        while h.tamanho() > 0:
            dist, v = h.rem_custo()
            for i in range(self.vertices):
                if self.grafo[v-1][i] != 0:     #self.grafo = matriz de distância
                    if custo_vem[i][0] == -1 or custo_vem[i][0] > dist + self.grafo[v-1][i]:
                        custo_vem[i] = [dist + self.grafo[v-1][i], v]
                        h.ad_custo(dist + self.grafo[v-1][i], i+1)
        return custo_vem

g = Grafo(10)

g.ad_pedagio(1, 2, 3.5) #onde ad_pedagio(vertice de origim, vertice de destino, valor cobrado do pedagio)
g.ad_pedagio(1, 3, 6.5)
g.ad_pedagio(1, 4, 7.3)
g.ad_pedagio(1, 10, 18.6)
g.ad_pedagio(2, 5, 8.7)
g.ad_pedagio(2, 8, 11.5)
g.ad_pedagio(3, 4, 13.2)
g.ad_pedagio(3, 5, 13.4)
g.ad_pedagio(3, 6, 14.6)
g.ad_pedagio(3, 7, 15.3)
g.ad_pedagio(4, 5, 16.1)
g.ad_pedagio(4, 6, 16.3)
g.ad_pedagio(5, 7, 18.3)
g.ad_pedagio(6, 7, 20.9)
g.ad_pedagio(9, 1, 25.9)

g.mostra_localizacao_e_peso_pedagios()

resultado_dijkstra = g.dijkstra(1)
print(resultado_dijkstra)
