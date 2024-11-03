import math
import numpy as np

G = []

def findAugmentingPath(G, s, t):
    n = len(G)
    visited = [False]*n
    augPath = []

    def dfs(u, bottleNeck):
        visited[u] = True
        augPath.append(u)
        if u == t:
            return bottleNeck
        for v in range(n):
            if G[u, v] > 0 and not visited[v]:
                bn2 = dfs(v, bottleNeck if bottleNeck <= G[u, v] else G[u, v])
                if visited[t]:
                    return bn2
        augPath.pop()

    bottleNeck = dfs(s, math.inf)

    return augPath, bottleNeck


n = len(G)
G1 = np.full((n, n), np.nan)


def fordFulkerson(G, s, t):
    n = len(G)
    Gres = G.copy()
    for i in range(n):
        for j in range(n):
            if not np.isnan(Gres[i, j]) and np.isnan(Gres[j, i]):
                Gres[j, i] = 0
    Gflow = np.zeros((n, n))

    maxFlow = 0
    augmentingPath, bottleNeck = findAugmentingPath(Gres, s, t)
    while augmentingPath:
        for i in range(len(augmentingPath) - 1):
            u = augmentingPath[i]
            v = augmentingPath[i+1]
            Gres[u, v] -= bottleNeck
            Gres[v, u] += bottleNeck
            Gflow[u, v] += bottleNeck
        maxFlow += bottleNeck
        augmentingPath, bottleNeck = findAugmentingPath(Gres, s, t)

    return maxFlow, Gflow