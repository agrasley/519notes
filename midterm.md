2. Path is nondeterministic/heap is not a BST. Still need log(n) swaps.
4.
  b. O(klogk + n * size of heap) = O(k log k + n log (n+k))
  c. Heapify--O(k + n log (n+k))
  d. k - n candidates will be ignored if k >> n. Quickselect O(k + n log n).
5.
  b. dp(Xi) = smallest number of coins needed to make up Xi cents
  c. Space: O(X) Time: O(nX)
  e. dp(x, t) = smallest n of types of coins needed considering type t only
  f. dp(0, t) = 0; dp(x>0, t>=len(v)) = None; dp(x, t) = min([dp(x-vt*k, t+1) + k for k in xrange(x//vt)])
  g. O(nX) for both
