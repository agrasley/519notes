# reverse an array
def rev(a):
    if a == []:
        return []
    else:
        return rev(a[1:]) + [a[0]]

# or a.reverse()

# quick sort
# not in-place, so a little less memory efficient
# O(n log n) average or best case
# worst case O(n**2) if already sorted or reverse sorted
# slightly faster than merge sort because of pivot
# default sorting alg in most languages
def sort(a):
    if a == []:
        return []
    else:
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot] # have to exclude pivot so a[1:]
        return sort(left) + [pivot] + sort(right)
