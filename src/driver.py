"""
Driver program: ties the permutation generator and all four sorting
algorithms together. As per the assignment requirements, this driver records the

- Algorithm name
- Unsorted array
- Number of comparisons

Run with no arguments to reproduce the required experiment (n = 4, 6, 8).
Optionally, one or more sizes can be passed on the command line to run a
different set instead, e.g. `python3 driver.py 3` or `python3 driver.py 5 7`.
"""

import csv
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

from permutations import permutations
from sorting_algos import mergesort, quicksort, shaker_sort, heap_sort

# Required experiment sizes (permutations(n) produces n! arrays, and
# each is run through all 4 algorithms -- 8! = 40320 arrays x 4
# algorithms = 161,280 runs, which still finishes in a couple seconds).
N_Values = [4, 6, 8] # number of elements in the array to be sorted per the assignment.
Top_N = 10

ALGORITHMS = {
    "mergesort": mergesort,
    "quicksort": quicksort,
    "shaker sort": shaker_sort,
    "heapsort": heap_sort,
}


@dataclass
class Result:
    algorithm: str
    unsorted_array: Tuple[int, ...]
    comparisons: int


def run_test(n: int) -> List[Result]:
    """
    Run every algorithm in ALGORITHMS against every permutation of
    0..n-1, and return one Result per (algorithm, array) run.

    Each algorithm's own sorted output is checked against Python's
    built-in sorted() as a correctness safety net. A driver that
    records comparison counts is only meaningful if the counts came
    from a run that actually sorted correctly.
    """
    results: List[Result] = []

    for perm in permutations(n):
        unsorted_array = perm            # a tuple, e.g. (2, 0, 1)
        expected = sorted(unsorted_array)

        for name, sort_fn in ALGORITHMS.items():
            sorted_array, comparisons = sort_fn(list(unsorted_array))
            if sorted_array != expected:
                raise AssertionError(
                    f"{name} produced an incorrect result for input "
                    f"{unsorted_array}: got {sorted_array}, expected {expected}"
                )
            results.append(Result(name, unsorted_array, comparisons))

    return results


def print_report(results: List[Result], n: int) -> None:
    """Print a clearly labeled best-N / worst-N / average summary per algorithm."""
    print(f"\n{'=' * 70}")
    print(f"n = {n}   ({len(list(permutations(n)))} permutations, {len(results)} total runs)")
    print(f"{'=' * 70}")

    for name in ALGORITHMS:
        runs = [r for r in results if r.algorithm == name]
        by_comparisons = sorted(runs, key=lambda r: r.comparisons)
        best = by_comparisons[:Top_N]
        worst = list(reversed(by_comparisons[-Top_N:]))
        average = sum(r.comparisons for r in runs) / len(runs)

        print(f"\n  {name}")
        print(f"    average comparisons over {len(runs)} permutations: {average:.2f}")
        print(f"    best {Top_N} (fewest comparisons):")
        for r in best:
            print(f"      {r.comparisons:>4}  {r.unsorted_array}")
        print(f"    worst {Top_N} (most comparisons):")
        for r in worst:
            print(f"      {r.comparisons:>4}  {r.unsorted_array}")


def write_csv(results: List[Result], path: Path) -> None:
    """Write every recorded run to a CSV file: one row per (algorithm, array) run."""
    with path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["algorithm", "unsorted_array", "comparisons"])
        for r in results:
            writer.writerow([r.algorithm, list(r.unsorted_array), r.comparisons])


def main() -> None:
    # No arguments -> run the required sizes (4, 6, 8). Passing one or
    # more sizes on the command line overrides that, for quick ad-hoc
    # testing without touching the required default.
    n_values = [int(arg) for arg in sys.argv[1:]] if len(sys.argv) > 1 else N_Values

    for n in n_values:
        results = run_test(n)
        print_report(results, n)

        csv_path = Path(__file__).with_name(f"driver_results_n{n}.csv")
        write_csv(results, csv_path)
        print(f"\n  full results for n={n} written to {csv_path.name}")


if __name__ == "__main__":
    main()