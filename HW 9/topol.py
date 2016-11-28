from collections import defaultdict


def _make_colls(n, edges):
    s = set(xrange(n))
    to, fro = defaultdict(set), defaultdict(list)
    for x, y in edges:
        if y in s:
            s.remove(y)
        fro[x].append(y)
        to[y].add(x)
    return s, to, fro

# (8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])


def order(n, edges):
    l = []
    s, to, fro = _make_colls(n, edges)
    while len(s):
        node = s.pop()
        l.append(node)
        for dest in fro[node]:
            to[dest].remove(node)
            if len(to[dest]) == 0:
                s.add(dest)
    if len(l) == n:
        return l
    else:
        return None
