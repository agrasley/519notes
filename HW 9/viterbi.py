from collections import defaultdict


def _make_colls(n, edges):
    s = set([-1])
    to, fro = defaultdict(set), defaultdict(list)
    for x in xrange(n):
        fro[-1].append(x)
        to[x].add(-1)
    for x, y in edges:
        fro[x].append(y)
        to[y].add(x)
    return s, to, fro

# (8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])


def longest(n, edges):
    ordering = []
    s, to, fro = _make_colls(n, edges)
    while len(s):
        node = s.pop()
        ordering.append(node)
        for dest in fro[node]:
            to[dest].remove(node)
            if len(to[dest]) == 0:
                s.add(dest)
    l = [(0, None) for _ in xrange(len(ordering))]
    maximum = [(0, None)]

    def _update(node, dest, node_max):
        dest_max, _ = l[dest]
        if node_max > dest_max:
            l[dest] = (node_max, node)
            if node_max > maximum[0][0]:
                maximum[0] = (node_max, dest-1)

    for node in xrange(len(ordering)):
        node_max, _ = l[node]
        for dest in fro[node-1]:
            _update(node-1, dest+1, node_max+1)
    backtrace_results = []

    def backtrace(n):
        backtrace_results.append(n)
        _, prev = l[n+1]
        if prev >= 0:
            backtrace(prev)

    backtrace(maximum[0][1])
    backtrace_results.reverse()
    return maximum[0][0]-1, backtrace_results
