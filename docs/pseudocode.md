```python
permutations:
function next_permutation(a,n):
	k = n - 2
	while k >= 0 and a[k] > = a[k+1]:
		k = k - 1
	if k < 0:
		return false // a being the last index of the permutation

l = n - 1 
	while a[1] <= a[k]:
		l = l - 1
		swap a[k], a[1]
		reverse a[k+1.. n-1]
		return true

function permutations(n):
	if n < 0: throw error
	if n == 0: yield an empty tuple; reutn

current = [0,1,..., n-1]
yield current
while next_permutation(current,n):
	yield current

##sorting_algorithms here:

driver:
n_values_to_sort = [4,6,8]
Top_N_cases: 10
ALGORITHMS = {"mergesort": MERGESORT,
"quicksort": QUICKSORT, "shaker sort" SHAKER_SORT,
"heapsort": HEAPSORT
}

structure Result: algorithm, unsorted_array, comparisons

function run_test: (n):
	results = []
		for perm in permutations(n):
			expected = sorted(perm)
			for name, sort_func in ALGORTHMS:
				sorted_array, comparisons = sort_func(perm)
				if sorted_array != expected: error "inccorrect sort"
					results.append(Result(name,perm,comparisons))
				return results

function print_report(results, n):
	for name in ALGORITHMS:
		runs = results where algorithm == name
		sort runs by comparisons in ascending
		best = first Top_N_cases runs
		worst = last Top_N_cases runs, reversed
		average = mean(comparisons over runs)
		print name, average, best (count + array), worst (count + array)

function write_csv(results, path):
  write head: algorithm, unsorted_array, comparisons
    for each result: write a row

  function MAIN():
  n_values = command-line args if given, else n_values_to_sort
    for n in n_values:
      results = run_test(n)
      print_report(results,n)
      write_csv(results,"driver_results_n{n}.csv"
```
