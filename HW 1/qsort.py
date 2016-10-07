def sort(a):
    if a == []:
        return []
    else:
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]  # have to exclude pivot-a[1:]
        return [sort(left)] + [pivot] + [sort(right)]


def sorted(a):
    if a == []:
        return []
    else:
        left, center, right = a
        return sorted(left) + [center] + sorted(right)


def search(t, x):
    res = _search(t, x)
    if res == []:
        return False
    else:
        return True


def insert(t, x):
    res = _search(t, x)
    if res == []:
        res.extend([[], x, []])


def _search(t, x):
    if t == []:
        return t
    else:
        left, center, right = t
        if center == x:
            return t
        elif center > x:
            return _search(left, x)
        else:
            return _search(right, x)
