import numpy as np

def cost(u, v, w, p, k, c):
    return (w[(u, v)] / k) * c + p[v]


def dijisktra(V, E, w, p, k, c, s):
    D = {v:999999999 for v in V}  # int em python não tem limite
    A = {v:None for v in V}
    C = {v:False for v in V}
    D[s] = 0

    while not all_visited(C):
        u = arg_min(D, C) 
        C[u] = True
        for v in get_N(E, u, C):
            c_aux = cost(u, v, w, p, k, c)
            if D[v] > D[u] + c_aux:
                D[v] = D[u] + c_aux
                A[v] = u
    return D, A

def arg_min(D, C):
    min_val = 9999999999999 
    min_arg = None
    for v, d in D.items():
        if d < min_val and not C[v]:
            min_val = d
            min_arg = v
    return min_arg

def all_visited(C):
    for visited in C.values():
        if not visited: return False
    return True


def get_N(E, v, C):
    N = []
    for e in E:
        if e[0] == v and not C[e[1]]:
            N.append(e[1])
    return N


def cheaper_path(V, E, w, p, k, c, s, t):
    D, A = dijisktra(V, E, w, p, k, c, s)
    path = [t]
    current = t
    while A[current]:
        current = A[current]
        path.insert(0, current)
    return path

V = ['a', 'b', 'c', 'd', 'e', 'f']
E = [('a', 'c'), ('c', 'f'), ('a', 'b'), ('b', 'd'), ('d', 'f'), ('a', 'f'), ('e', 'b')]
w = {('a', 'c'):3, ('c', 'f'):3, ('a', 'b'):1, ('b', 'd'):1, ('d', 'f'):1, ('a', 'f'):10, ('e', 'b'):2}
p = {'a':1.5, 'b':3, 'c':5, 'd':2, 'e':10, 'f':4}
k = 10 
c = 5
s = 'a'
t = 'f'

f = cheaper_path(V, E, w, p, k, c, s, t)
print(f'path: {f}')
