def num_inversions(x):
    return _helper(x)[0]


def _helper(x):
    len_x = len(x)
    if len_x == 1:
        return 0, x
    else:
        l = x[:(len_x / 2)]
        r = x[(len_x / 2):]
        return _merge(_helper(l), _helper(r))


def _merge(lt, rt):
    l = lt[1]
    r = rt[1]
    result = []
    total = lt[0] + rt[0]
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
            total += len(l[i:])
    if i < len_l:
        result.extend(l[i:])
    elif j < len_r:
        result.extend(r[j:])
    return total, result
