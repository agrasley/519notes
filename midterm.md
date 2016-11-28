2. Path is nondeterministic/heap is not a BST. Still need log(n) swaps.
4.
  b. O(klogk + n * size of heap) = O(k log k + n log (n+k))
  c. Heapify--O(k + n log (n+k))
  d. k - n candidates will be ignored if k >> n. Quickselect O(k + n log n).
5.
  b. dp(xi) = smallest number of coins needed to make up xi cents
  c. Space: O(X) Time: O(nX)
  e. dp(x, M) = smallest n of types of coins needed considering first M types only
  f. dp(0, M) = 0;
  g. O(nX) for both
