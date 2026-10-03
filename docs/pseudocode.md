```python
permutations:
function next_permutation(a,n):
	k = n - 2
	while k >= 0 and a[k] >= a[k+1]:
		k = k - 1
	if k < 0:
		return false // a being the last index of the permutation

	l = n - 1 
	while a[l] <= a[k]:
		l = l - 1
	swap a[k], a[l]
	reverse a[k+1.. n-1]
	return true

function permutations(n):
	if n < 0: throw error
	if n == 0: yield an empty tuple; return

	current = [0,1,..., n-1]
	yield current
	while next_permutation(current,n):
		yield current

## sorting_algorithms here:

function MERGESORT(arr):
	comparisons = 0
	if length(arr) <= 1:
		return arr, comparisons

	mid = length(arr) // 2
	left, comp_left = MERGESORT(arr[0..mid-1])
	right, comp_right = MERGESORT(arr[mid..end])
	
	merged, comp_merge = MERGE(left, right)
	total_comparisons = comp_left + comp_right + comp_merge
	return merged, total_comparisons

function MERGE(left, right):
	result = []
	i = 0, j = 0
	comparisons = 0
	while i < length(left) and j < length(right):
		comparisons = comparisons + 1
		if left[i] <= right[j]:
			append left[i] to result
			i = i + 1
		else:
			append right[j] to result
			j = j + 1
	extend result with left[i..end]
	extend result with right[j..end]
	return result, comparisons

function QUICKSORT(arr):
	comparisons = 0
	A = copy of arr
	comparisons = QUICKSORT_HELPER(A, 0, length(A) - 1)
	return A, comparisons

function QUICKSORT_HELPER(arr, low, high):
	comparisons = 0
	if low < high:
		pivot_idx, comp_partition = PARTITION(arr, low, high)
		comp_left = QUICKSORT_HELPER(arr, low, pivot_idx - 1)
		comp_right = QUICKSORT_HELPER(arr, pivot_idx + 1, high)
		comparisons = comp_partition + comp_left + comp_right
	return comparisons

function PARTITION(arr, low, high):
	pivot = arr[high]
	i = low - 1
	comparisons = 0
	for j from low to high - 1:
		comparisons = comparisons + 1
		if arr[j] < pivot:
			i = i + 1
			swap(arr[i], arr[j])
	swap(arr[i + 1], arr[high])
	return i + 1, comparisons

function SHAKER_SORT(arr):
	A = copy of arr
	n = length(A)
	swapped = true
	start = 0
	end = n - 1
	comparisons = 0

	while swapped:
		swapped = false
		for i from start to end - 1:
			comparisons = comparisons + 1
			if A[i] > A[i + 1]:
				swap(A[i], A[i + 1])
				swapped = true

		if not swapped:
			break

		swapped = false
		end = end - 1

		for i from end - 1 down to start:
			comparisons = comparisons + 1
			if A[i] > A[i + 1]:
				swap(A[i], A[i + 1])
				swapped = true

		start = start + 1

	return A, comparisons

function HEAPSORT(arr):
	A = copy of arr
	n = length(A)
	comparisons = 0

	for i from (n // 2) - 1 down to 0:
		comp = HEAPIFY(A, n, i)
		comparisons = comparisons + comp

	for i from n - 1 down to 1:
		swap(A[0], A[i])
		comp = HEAPIFY(A, i, 0)
		comparisons = comparisons + comp

	return A, comparisons

function HEAPIFY(arr, n, i):
	largest = i
	left = 2 * i + 1
	right = 2 * i + 2
	comparisons = 0

	if left < n:
		comparisons = comparisons + 1
		if arr[left] > arr[largest]:
			largest = left

	if right < n:
		comparisons = comparisons + 1
		if arr[right] > arr[largest]:
			largest = right

	if largest != i:
		swap(arr[i], arr[largest])
		comp_recursive = HEAPIFY(arr, n, largest)
		comparisons = comparisons + comp_recursive

	return comparisons

driver:
n_values_to_sort = [4,6,8]
Top_N_cases: 10
ALGORITHMS = {
	"mergesort": MERGESORT,
	"quicksort": QUICKSORT,
	"shaker sort": SHAKER_SORT,
	"heapsort": HEAPSORT
}

structure Result: algorithm, unsorted_array, comparisons

function run_test(n):
	results = []
	for perm in permutations(n):
		expected = sorted(perm)
		for name, sort_func in ALGORITHMS:
			sorted_array, comparisons = sort_func(perm)
			if sorted_array != expected: error "incorrect sort"
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
		write_csv(results,f"driver_results_n{n}.csv")
```
