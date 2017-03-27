"""
This is the quick sort algorithm.
It is a divide and conquer algorithm.

Advantages:
	- Low overhead
	- Efficient sorting algorithm. More efficient than merge sort although they have the same asymptotic time complexity.

Time complexity:
	Worst Case: O(n^2) 
	Best Case: O(nlogn)
	Average Case: O(nlogn)

Worst space complexity:
	O(n)
"""

"""
This is the quick sort algorithm.
"""
def quick_sort(list):
	if len(list) == 0 or len(list)==1:
		return list
	else:
		pivot = list[0]
		bigger, smaller = partition(list[1:], pivot)

		bigger = quick_sort(bigger)
		smaller = quick_sort(smaller)

		return smaller + [pivot] + bigger

"""
A helper function that returns 2 lists. The first is a list that consists of elements smaller than or equal to the pivot.
The second list is a list that consists of elements larger than the pivot.
"""
def partition(list, pivot):
	bigger = []
	smaller = []
	for element in list:
		if element <= pivot:
			smaller.append(element)
		else:
			bigger.append(element)

	return bigger, smaller

"""
The main line logic of the program.
"""
if __name__ == "__main__":
	list1 = [1, 2, 3, 4, 5]
	list2 = [5, 4, 3, 2, 1]

	list2 = quick_sort(list2)

	print(list1 == list2)