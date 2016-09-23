from random import randrange

def qselect(k, l):
    pivot = l[randrange(0,len(l))]
    left = [x for x in l if x < pivot]
    right = [x for x in l[1:] if x >= pivot]
    ll = len(left)
    if ll == k - 1:
        return pivot
    elif ll >= k:
        return qselect(k, left)
    else:
        return qselect(k - (ll + 1), right)
