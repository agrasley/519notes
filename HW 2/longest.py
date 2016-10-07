def longest(tree):
    return _helper(tree)[0]


def _helper(tree):
    if tree == []:
        return 0, 0
    else:
        l, i, r = tree
        l_result = _helper(l)
        r_result = _helper(r)
        combined_depths = l_result[1] + r_result[1]
        if combined_depths > l_result[0] and combined_depths > r_result[0]:
            path = combined_depths
        elif l_result[0] > r_result[0]:
            path = l_result[0]
        else:
            path = r_result[0]
        if l_result[1] > r_result[1]:
            return path, l_result[1] + 1
        else:
            return path, r_result[1] + 1
