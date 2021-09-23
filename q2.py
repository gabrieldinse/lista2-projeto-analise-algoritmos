import numpy as np

def cost(u, v, w, p, k):
    return w[(u, v)] * k + p[v]


def dijisktra(V, E, w, p, k, s):
    D = {v:999999999 for v in V}  # int em python não tem limite
    A = {v:None for v in V}
    C = {v:False for v in V}
    D[s] = 0

    while not all_visited(C):
        u = V[np.argmin(C.values())]
        C[u] = True
        for v in get_N(V)
            c = cost(u, v, w, p, k):
            if D[v] > D[u] + c
                D[v] = D[u] + c
                E[v] = u
    return D, A


def all_visited(C):
    for value in C.values():
        if not value: return False
    return True


def get_N(E, v):
    N = []
    for e in E:
        if e[0] == v:
            N.append(e[1])
        elif e[1] == v:
            N.append(e[0])
    return N


def cheaper_path(C, L, cs, ct):
    D, A = min_paths(C, L, cs)
    p = [ct]
    current = ct
    while A[current]:
        current = A[current]
        p.insert(0, current)
    return p

f = cheaper_path(['a', 'b', 'c', 'd', 'e', 'f', 'g'],
             [('a', 'c'), ('b', 'd'), ('c', 'f'), ('d', 'e'), ('d', 'f'), ('d', 'g')],
             'a', 'g')
print(f'path: {f}')
