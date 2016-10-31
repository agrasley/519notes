def memoize(f):
    d = dict()

    def wrapper(*args):
        if args in d:
            return d[args]
        else:
            result = f(*args)
            d[args] = result
            return result

    return wrapper


def best(weight, items):

    @memoize
    def b(weight):
        cand = [(b(weight-w)[0] + v, -j) for (j, (w, v)) in enumerate(items) if w <= weight]
        cand.append((0, None))
        return max(cand)

    results = b(weight)
    backtrace_results = [0] * len(items)

    def backtrace(weight):
        (_, j) = b(weight)
        if j is not None:
            backtrace_results[-j] += 1
            backtrace(weight - items[-j][0])

    backtrace(weight)
    return results[0], backtrace_results
