from collections import defaultdict
from heapdict import heapdict


def shortest(target, edges):
    h = heapdict()
    dist = defaultdict(lambda: float('inf'))
    dist[0] = 0
    prev = defaultdict(lambda: None)
    fro = defaultdict(list)
    for x, y, d in edges:
        if x not in h:
            h[x] = dist[x]
        if y not in h:
            h[y] = dist[y]
        fro[x].append((y, d))
    backtrace_results = []

    def backtrace(u):
        if u is not None:
            backtrace_results.append(u)
            backtrace(prev[u])

    while True:
        u, _ = h.popitem()
        if u == target-1:
            backtrace(u)
            backtrace_results.reverse()
            return dist[u], backtrace_results
        for v, d in fro[u]:
            alt = dist[u] + d
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                h[v] = alt
