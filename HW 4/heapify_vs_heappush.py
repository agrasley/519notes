from heapq import heapify, heappush
from random import randint
import time


def random_list(start, stop, size):
    return [randint(start, stop) for _ in xrange(size)]


def build_by_push(l):
    heap = []
    for item in l:
        heappush(heap, item)
    return heap


a = random_list(-500, 500, 10000)
b = range(-5000, 5000)
c = b[:]
c.reverse()
push_random_t0 = time.clock()
build_by_push(a)
push_random_t1 = time.clock() - push_random_t0
heapify_random_t0 = time.clock()
heapify(a)
heapify_random_t1 = time.clock() - heapify_random_t0
push_sorted_t0 = time.clock()
build_by_push(b)
push_sorted_t1 = time.clock() - push_sorted_t0
heapify_sorted_t0 = time.clock()
heapify(b)
heapify_sorted_t1 = time.clock() - heapify_sorted_t0
push_reverse_t0 = time.clock()
build_by_push(c)
push_reverse_t1 = time.clock() - push_reverse_t0
heapify_reverse_t0 = time.clock()
heapify(c)
heapify_reverse_t1 = time.clock() - heapify_reverse_t0
print "Random:\n"
print push_random_t1, heapify_random_t1, '\n'
print "Sorted:\n"
print push_sorted_t1, heapify_sorted_t1, '\n'
print "Reverse sorted:\n"
print push_reverse_t1, heapify_reverse_t1
