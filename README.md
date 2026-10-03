# Sorting Algorithm Comparisons 

## The 3 files that make up the structure of the project:
| File | Purpose |
| :-- | :-- |
| `permutations.py` | Part 1: generates every purmutation of `0..n-1` in lexicographic order |
| `sorting_algos.py` | Part 2: The given sorts of mergesort, quicksort, shaker sort (bidirectional bubble sort, and heap sort. Each takes an unsorted list of integers and returns a `sorted_array, comparison_count)` |
| `driver.py` | Part 3 & 4: A driver program that runs all four algorithms against every permutation of `0..n-1` for sizes of `n = 4,6,8` and reports the results into a `csv` file.

This project does not run on any external dependencies. It strictly runs on a regular Python 3 interpreter (`csv`, `pathlib` and `typing` are all standard libraries)
## How to run the experiments
To execute the driver, run the following command in the terminal:
```bash
python3 driver.py
```
This is the only command needed to reproduce every table needed for the report. With no arguments, the driver should automaticall run
all 3 requires sizes of (`n = 4, 6, 8`) against all four algorithms. 
Optionally, one of more sizes can be passed on the command line to run a different set instead for example:
```bash
python3 driver.py 3 #setting it at n = 3, for a quick check at first
python3 driver.py 5 7 # different sizes for fun
```

## Sorting Algorithms used:
* Merge sort: A sort that uses the divide-and-conquer method. It works by dividing the list in half, recursively sorts the 2 separated lists and eventually merges them back into one list that is sorted. The time complexity for this sort is a stable O(nLogn), which makes it good for sorting larger datasets with the trade offs of it requiring more memory due to needing hold 2 separate lists for the elements to break off into.
* Quick sort: A comparison based sort that also uses the divide-and-conquer method. It differs from merge sort as instead of partitioning the list in to halves, it does it based on a selected pivot. This pivot will is then used to recursively sort the sub-arrays. The average time complexity of this sort is O(n log n) with the worst case scenario being O(n^2). The time complexity varies depending on the size as well as if the data sets are partially or fully sorted. 
* Shaker sort:
* Heap sort: 

## Average Number of Comparisons n = 4
<img width="1938" height="1321" alt="n4 average graph" src="https://github.com/user-attachments/assets/0d0a71b1-1031-4885-b40d-986d45abc0dd" />


## Average Number of Comparisons n = 6
<img width="1921" height="1316" alt="n6 average graph" src="https://github.com/user-attachments/assets/a6c38d67-8aed-4428-9842-e23c58fc866f" />




## Average Number of Comparisons n = 8
<img width="2035" height="1244" alt="n8 average graph" src="https://github.com/user-attachments/assets/c1de49b4-e793-478f-b5f8-ae9f92433afb" />
