import random 
from typing import List, Tuple

# --------------------------------------------------------------------------
# Sort 1: Mergesort
# --------------------------------------------------------------------------

def mergesort(arr: List[int]) -> Tuple[List[int], int]:
    """
    Sort `arr` using top-down merge sort (divide and conquer).
 
    Split the array in half, recursively sort each half, then merge
    the two sorted halves back together. All the actual work -- and
    all the comparisons -- happen in the merge step.
 
    Returns:
        (sorted_array, comparison_count)
    """
    comparisons = 0
 
    def sort(a: List[int]) -> List[int]:
        nonlocal comparisons
        if len(a) <= 1:
            return a[:]  # 0 or 1 elements: already sorted, nothing to do
 
        mid = len(a) // 2
        left = sort(a[:mid])
        right = sort(a[mid:])
        return merge(left, right)

    
    def merge(left : List[int], right: List[int]) -> List[int]:
        nonlocal comparisons
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        # one of the two lists is exhausted, append the other list
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    sorted_arr = sort(arr)
    return sorted_arr, comparisons

# --------------------------------------------------------------------------
# Sort 2: Quicksort
# --------------------------------------------------------------------------
def quicksort(arr: List[int], randomized_pivot: bool = False) -> Tuple[List[int], int]:
    """
    Sort `arr` using quicksort (Lomuto partition scheme).
 
    Picks a pivot, partitions the array so everything <= pivot ends up
    to its left and everything > pivot ends up to its right, then
    recursively sorts each side.
 
    Args:
        randomized_pivot: if True, swap in a random element as the
            pivot before partitioning, which avoids the O(n^2) worst
            case on already-sorted or reverse-sorted input that a
            fixed "last element" pivot choice suffers from. Off by
            default for reproducible comparison counts.
 
    Returns:
        (sorted_array, comparison_count)
    """
    comparisons = 0
    a = arr[:]  # work on a private copy; never mutate the caller's list
 
    def _partition(lo: int, hi: int) -> int:
        nonlocal comparisons
        if randomized_pivot:
            r = random.randint(lo, hi)
            a[r], a[hi] = a[hi], a[r]
 
        pivot = a[hi]        # pivot is always the last element of this range
        i = lo - 1           # boundary: everything a[lo..i] is <= pivot so far
        for j in range(lo, hi):
            comparisons += 1
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[hi] = a[hi], a[i + 1]   # put the pivot in its final spot
        return i + 1                        # pivot's final index
 
    def _sort(lo: int, hi: int) -> None:
        if lo < hi:
            p = _partition(lo, hi)
            _sort(lo, p - 1)      # everything left of the pivot
            _sort(p + 1, hi)      # everything right of the pivot
 
    _sort(0, len(a) - 1)
    return a, comparisons
# --------------------------------------------------------------------------
# Sort 3: Shaker sort (bidirectional bubble sort)
# --------------------------------------------------------------------------
def shaker_sort(arr: List[int]) -> Tuple[List[int], int]:
    """
    Sort 'arr' using shaker sort which is a type of bubble sort that alternates between left and right
    on every pass. Compared to traditional bubble sort which always sweeps left to right, shaker sort
    can be more efficient in some cases because it can move elements to their correct position faster
    by moving in both directions.

    Returns: (sorted_array, comparison_count)
    """
    comparisons = 0
    a = arr[:]  # work on a private copy; never mutate the caller's list
    low = 0
    high = len(a) - 1
 
    while low < high:
        # Forward pass: bubble the largest item in a[lo..hi] to a[hi].
        swapped = False
        for i in range(low, high):
            comparisons += 1
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        high -= 1  # a[hi] (pre-decrement) is now the largest remaining item, so it's placed
 
        if not swapped:
            break  # nothing moved on the forward pass: already sorted
 
        # Backward pass: bubble the smallest item in a[lo..hi] to a[lo].
        swapped = False
        for i in range(high, low, -1):
            comparisons += 1
            if a[i - 1] > a[i]:
                a[i - 1], a[i] = a[i], a[i - 1]
                swapped = True
        low += 1  # a[lo] (pre-increment) is now the smallest remaining item, so it's placed
 
        if not swapped:
            break  # nothing moved on the backward pass: already sorted
 
    return a, comparisons
# --------------------------------------------------------------------------
# Sort 4: Heapsort
# --------------------------------------------------------------------------
def heapsort(arr: List[int]) -> Tuple[List[int], int]:
    """
    Sort 'arr' using heapsort which is a comparison-based sorting algorithm that uses a binary heap data structure.
    It works by first building a max heap from the input data, and then repeatedly extracting the maximum element from the heap and rebuilding the heap until all elements are sorted.
    
    Returns:
        (sorted_array, comparison_count)
    """
    comparisons = 0
    a = arr[:]  # work on a private copy; never mutate the caller's list
    n = len(a)
 
    def _sift_down(root: int, size: int) -> None:
        """Restore the max-heap property for the subtree rooted at `root`,
        within a[0:size], assuming both of its children are already
        valid heaps."""
        nonlocal comparisons
        while True:
            largest = root
            left = 2 * root + 1
            right = 2 * root + 2
 
            if left < size:
                comparisons += 1
                if a[left] > a[largest]:
                    largest = left
            if right < size:
                comparisons += 1
                if a[right] > a[largest]:
                    largest = right
 
            if largest == root:
                return  # root is already >= both children: heap restored
            a[root], a[largest] = a[largest], a[root]
            root = largest  # keep sifting the displaced value down
 
    # Phase 1: build the max-heap bottom-up. Leaves (indices >= n // 2)
    # are trivially valid 1-element heaps already, so start just above them.
    for root in range(n // 2 - 1, -1, -1):
        _sift_down(root, n)
 
    # Phase 2: repeatedly move the max to the end of the unsorted region.
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]  # largest remaining item -> its final slot
        _sift_down(0, end)           # heap now covers a[0:end]; restore it
 
    return a, comparisons


