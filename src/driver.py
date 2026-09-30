"""
Driver program: ties the permutation generator and all four sorting
algorithms together. As per the assignment requirements, this driver records the

- Algorithm name
- Unsorted array 
- Number of comparisons

"""

import csv
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

from permutations import permutations
from sorting_algos import mergesort, quicksort, shaker_sort, heap_sort

# Default size of array to test (permutations(N) produces N! arrays,
# and each is run through all 4 algorithms, so keep N modest --
# 5! = 120 arrays x 4 algorithms = 480 runs is quick; 8! = 40320 would
# make the printed table and CSV unwieldy).
N = 5

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
    """Print every recorded run, then a per-algorithm summary."""
    array_width = max(len(str(r.unsorted_array)) for r in results)

    print(f"Ran {len(ALGORITHMS)} algorithms against all {len(list(permutations(n)))} "
          f"permutations of 0..{n - 1} ({len(results)} total runs)\n")

    print(f"{'algorithm':<12}  {'unsorted array':<{array_width}}  comparisons")
    print("-" * (12 + array_width + 15))
    for r in results:
        print(f"{r.algorithm:<12}  {str(r.unsorted_array):<{array_width}}  {r.comparisons}")

    # Per-algorithm summary: total / average / min / max comparisons
    # across every permutation tested. This is what actually shows the
    # difference in how consistent each algorithm is (e.g. mergesort's
    # comparison count barely moves between arrays; quicksort's swings a lot).
    print(f"\n{'algorithm':<12}  {'total':>8}  {'average':>9}  {'min':>6}  {'max':>6}")
    print("-" * 50)
    for name in ALGORITHMS:
        counts = [r.comparisons for r in results if r.algorithm == name]
        total = sum(counts)
        average = total / len(counts)
        print(f"{name:<12}  {total:>8}  {average:>9.2f}  {min(counts):>6}  {max(counts):>6}")


def write_csv(results: List[Result], path: Path) -> None:
    """Write every recorded run to a CSV file: one row per (algorithm, array) run."""
    with path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["algorithm", "unsorted_array", "comparisons"])
        for r in results:
            writer.writerow([r.algorithm, list(r.unsorted_array), r.comparisons])


def main() -> None:
    n = int(sys.argv[1]) if len(sys.argv) > 1 else N

    results = run_test(n)
    print_report(results, n)

    csv_path = Path(__file__).with_name("driver_results.csv")
    write_csv(results, csv_path)
    print(f"\nWrote {len(results)} rows to {csv_path}")


if __name__ == "__main__":
    main()