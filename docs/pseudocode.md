python
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
=======
function next_permutation(a,n):
	k = n - 2
	while k >= 0 and a[k] >= a[k + 1]:
		k = k - 1
	if k < 0:
		return False
	l = n - 1
	while a[k] >= a[l]:
		l = l - 1
	swap(a[k], a[l])
	reverse(a, k + 1, n - 1)
	return True

function generate_permutations(a, n):
	current = sorted(a)
	yield current
	while next_permutation(current, n):
		yield current

## sorting_algorithms here:

function bubble_sort(arr):
	n = length(arr)
	for i from 0 to n - 1:
		for j from 0 to n - i - 2:
			if arr[j] > arr[j + 1]:
				swap(arr[j], arr[j + 1])
	return arr

function insertion_sort(arr):
	n = length(arr)
	for i from 1 to n - 1:
		key = arr[i]
		j = i - 1
		while j >= 0 and arr[j] > key:
			arr[j + 1] = arr[j]
			j = j - 1
		arr[j + 1] = key
	return arr

function merge_sort(arr):
	if length(arr) <= 1:
		return arr
	mid = length(arr) // 2
	left = merge_sort(arr[0:mid])
	right = merge_sort(arr[mid:end])
	return merge(left, right)

function merge(left, right):
	result = []
	i = 0, j = 0
	while i < length(left) and j < length(right):
		if left[i] <= right[j]:
			append left[i] to result
			i = i + 1
		else:
			append right[j] to result
			j = j + 1
	extend result with left[i:end]
	extend result with right[j:end]
	return result

function quick_sort(arr, low, high):
	if low < high:
		pivot_idx = partition(arr, low, high)
		quick_sort(arr, low, pivot_idx - 1)
		quick_sort(arr, pivot_idx + 1, high)
	return arr

function partition(arr, low, high):
	pivot = arr[high]
	i = low - 1
	for j from low to high - 1:
		if arr[j] < pivot:
			i = i + 1
			swap(arr[i], arr[j])
	swap(arr[i + 1], arr[high])
	return i + 1

driver:
n_values_to_sort = [4, 6, 8]
Top_N_cases: 10

function main():
	for n in n_values_to_sort:
		results = run_test(n)
		print_report(results, n)
		write_csv(results, f"driver_results_n{n}.csv")

function write_csv(results, path):
	# file write logic

