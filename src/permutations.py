"""
Write code to generate all possible permutations of the integers 0 through n − 1 for a given small n. For example, if n = 3, your generator must produce:

{0, 1, 2}, {0, 2, 1}, {1, 0, 2}, {1, 2, 0}, {2, 0, 1}, {2, 1, 0}

Implement a standard lexicographic permutation algorithm (recommended) or any correct algorithm that enumerates all permutations without duplicates.
"""
import itertools
import math
from typing import Iterator, List, Tuple

def next_permutation(i: List[int]) -> bool:
    """
    Boolean that returns true or false if there is a next permutation in List[int] i.
    True means there is another permutation, false means there is not.
    """
    n = len(i)

    k = n - 2 #2nd to last index
    while k >= 0 and i[k] >= i[k + 1]: #looping through the list from second to last index to the last index
        k -= 1
    if k < 0:
        return False
    # find the smallest value that can possibly go in position k
    l = n - 1 
    while i[k] >= i[l]:
        l -= 1

    i[k], i[l] = i[l], i[k] #swap the values at index k and l

    i[k +1:] = reversed(i[k +1])

    return True


def permutations(n: int) -> Iterator[Tuple[int]]:
    """
    Generates all possible permuations of range(n) in lexicographic order one at time.

    example: list(permuations(3)) 
    returns [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
    """