def mergesort(x):
    len_x = len(x)
    if len_x == 1:
        return x
    else:
        l = x[:(len_x / 2)]
        r = x[(len_x / 2):]
        return _merge(mergesort(l), mergesort(r))


def _merge(l, r):
    result = []
    i = j = 0
    len_l = len(l)
    len_r = len(r)
    while i < len_l and j < len_r:
        if l[i] <= r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    if i < len_l:
        result.extend(l[i:])
    elif j < len_r:
        result.extend(r[j:])
    return result
