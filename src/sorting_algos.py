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