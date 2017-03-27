"""
This is the insertion sort algorithm.
Only efficient on small array sizes.

Advantages:
	- Simple implementation
	- Efficient for small data sets
	- More efficient than most O(n^2) sorting algorithms like bubble sort
	- Efficient for pre-sorted data. Takes O(n)

Time Complexity
	Worst Case: O(n^2)
	Best Case: O(n)
	Average Case: O(n^2)

Worst Case Space Complexity
	O(n)
"""

"""
Traditional insertion sort algorithm. 
This algorithm accepts a list and sorts the list.
"""
def insertion_sort(list):
	for index in range(0, len(list)):
		for x in range(0, index):
			if list[index]<list[index-1]:
				# Swap elements at index and index-1
				temp = list[index-1]
				list[index-1] = list[index]
				list[index] = temp

				if index>0:
					index-=1


"""
Improved insertion sort. 
Skips the first index because the first index doesn't need to be checked.
"""
def improved_insertion_sort(list):
	for index in range(1, len(list)):
		for x in range(0, index):
			if list[index]<list[index-1]:
				# Swap elements at index and index-1
				temp = list[index-1]
				list[index-1] = list[index]
				list[index] = temp

				if index>0:
					index-=1

"""
The main method for to test the algorithm.
"""
if __name__ == "__main__":
	list1 = [1, 2, 3, 4, 5]
	list2 = [5, 4, 3, 2, 1]
	list3 = [5, 3, 4, 1, 2]

	insertion_sort(list2)
	insertion_sort(list3)

	print(list1 == list2)
	print(list1 == list3)

	list2 = [5, 4, 3, 2, 1]
	list3 = [5, 3, 4, 2, 1]

	improved_insertion_sort(list2)
	improved_insertion_sort(list3)

	print(list1 == list2)
	print(list1 == list3)



