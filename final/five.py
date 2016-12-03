from collections import defaultdict


def dfs_topol(n, _edges):
    l = []
    temp = [False] * n
    perm = [False] * n
    cand = set(xrange(n))

    edges = defaultdict(list)
    for u, v in _edges:
        edges[u].append(v)

    def visit(v):
        print v
        if temp[v]:
            return None
        elif not perm[v]:
            temp[v] = True
            for u in edges[v]:
                visit(u)
            perm[v] = True
            temp[v] = False
            cand.remove(v)
            print l
            l.append(v)
            print l

    while len(cand):
        v = next(iter(cand))
        visit(v)

    l.reverse()

    return l
