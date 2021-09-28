def caminhao(v, w, C, delivered):
    N = len(v)
    M = [[0 for i in range(C+1)] for j in range(N+1)] 
    for i in range(1, N):
        if not delivered[i]:
            for j in range(C+1):
                if j < w[i]:
                    M[i][j] = M[i-1][j]
                else:
                    M[i][j] = max(M[i-1][j], v[i] + M[i-1][j-w[i]])
    total = M[N][C]
    remaining_w = C
    items = [] 

    for i in reversed(range(1, len(v))):
        if not delivered[i]:
            if M[i][remaining_w] == M[i - 1][remaining_w] + v[i]:
               items.append(i)
               remaining_w -= w[i]
    return items

   # return M[(N,C)]

T = ['t1', 't2', 't3']                                            #T: Conjunto de caminhões.
C = [2000, 4000, 3000]                                            #t: Capacidade de carga dos caminhões em kg
G = [None, 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9', 'g10'] #G: Conjunto de itens.
w = [None, 11500, 1300, 11750, 111650, 1250, 11200, 1800, 1400, 1100, 1550]            #w: Peso dos intens em kg.
v = [None, 3000, 1500, 400, 5000, 10000, 200, 300, 2000, 4100, 6100]    #w: Lucro na entrega em reais de cada item.
delivered = [False] * len(v)

for c in C:
    items = caminhao(v, w, c, delivered)
    for item in items:
        delivered[item] = True

print(f'Itens não entregues: {[g for i, g in enumerate(G[1:]) if not delivered[i]]}')
print(f'Valor não entregue: {sum([value for i, value in enumerate(v[1:]) if not delivered[i]])}')
