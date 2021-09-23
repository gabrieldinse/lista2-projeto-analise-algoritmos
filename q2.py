def cost(u, v, w, p, k):
    return w[(u, v)] * k + p[v]

    def ad_pedagio(self, u, v, peso):
        self.grafo[u-1][v-1] = peso
        self.grafo[v-1][u-1] = peso

def dijisktra(V, E, c, s):
    D = {v:999999999 for v in V}  # int em python não tem limite
    A = {v:None for v in V}
    D[s] = 0

    for i in range(len(V)):
        for u, v in E:
            # Usa-se as duas condições pois o
            # grafo é não dirigido
            if D[v] > D[u] + 1:
                D[v] = D[u] + 1
                A[v] = u
            if D[u] > D[v] + 1:
                D[u] = D[v] + 1
                A[u] = v
    return A


def min_path(C, L, cs, ct):
    A = min_paths(C, L, cs)
    p = [ct]
    current = ct
    while A[current]:
        current = A[current]
        p.insert(0, current)
    return p

f = min_path(['a', 'b', 'c', 'd', 'e', 'f', 'g'],
             [('a', 'c'), ('b', 'd'), ('c', 'f'), ('d', 'e'), ('d', 'f'), ('d', 'g')],
             'a', 'g')
print(f'path: {f}')
