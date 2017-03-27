"""
This is the selection sort algorithm.
Inefficient on large data sizes, generally worst than insertion sort.

Advantages:
	- Simple to implement

Time Complexity
	Worst Case: O(n^2)
	Best Case: O(n^2)
	Average Case: O(n^2)

Total Space Complexity
	O(n)
"""

"""
Selection sort algorithm.
The function accepts a list and sorts the list.
"""
def selection_sort(list):
	for index in range(0, len(list)):
		min_index = index
		for smallest_index in range(index, len(list)):
			if list[smallest_index]<list[min_index]:
				min_index = smallest_index

		# swapping the smallest unsorted element with the index value
		if min_index>-1:
			temp = list[min_index]
			list[min_index] = list[index]
			list[index] = temp

"""
This is the mainline logic to test the code.
"""
if __name__ == "__main__":
	list1 = [1, 2, 3, 4, 5]
	list2 = [5, 4, 3, 2, 1]
	list3 = [5, 3, 4, 1, 2] 

	selection_sort(list2)
	selection_sort(list3)

	print(list1 == list2)
	print(list1 == list3)





