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
