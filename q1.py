from queue import Queue



def get_N(E, v):
    N = []
    for e in E:
        if e[0] == v:
            N.append(e[1])
        elif e[1] == v:
            N.append(e[0])
    return N


def width_search(V, E, s):
    C = {v:False for v in V}
    D = {v:999999999 for v in V}  # int em python não tem limite
    A = {v:None for v in V}
    C[s] = True
    D[s] = 0
    Q = Queue()
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for v in get_N(E, u):
            if not C[v]:
                C[v] = True
                D[v] = D[u] + 1
                A[v] = u
                Q.put(v)
    return D, A

def min_path(C, L, cs, ct):
    D, A = width_search(C, L, cs)
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
