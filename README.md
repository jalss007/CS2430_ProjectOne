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
*Merge sort:
*Quick sort:
*Shaker sort:
*Heap sort: 
