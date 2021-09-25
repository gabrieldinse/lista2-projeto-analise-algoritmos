def caminhao(v, w, C):
    N = len(v)
    M = {}
    for i in range(C+1):
        M[(0,i)] = 0
    for i in range(1, N+1):
        for j in range(C+1):
            if j < w[i-1]:
                M[(i, j)] = M[(i-1, j)]
            else:
                M[(i, j)] = max(M[(i-1, j)], v[i-1] + M[(i-1, j-w[i-1])])
    return M[(N,C)]

T = ['t1', 't2', 't3']                                            #T: Conjunto de caminhões.
c = [2000, 4000, 3000]                                            #t: Capacidade de carga dos caminhões em kg
G = ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9', 'g10'] #G: Conjunto de itens.
w = [500, 300, 750, 650, 250, 200, 800, 400, 100, 550]            #w: Peso dos intens em kg.
v = [3000, 1500, 400, 5000, 10000, 200, 300, 2000, 4100, 6100]    #w: Lucro na entrega em reais de cada item.

print('Soma do lucro dos itens entregues:',caminhao(v, w, c[1]))