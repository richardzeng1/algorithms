import time
"""
This is the bubble sort algorithm.
Slow and inefficient sorting algorithm.

Advantages:
	- Simple to implement
	- Good performance if list is already sorted or have a few elements in close to sorted order

Time Complexity
	Worst Case: O(n^2)
	Best Case: O(n)
	Average Case: O(n)

Space Complexity
	O(1)
"""

"""
Traditional bubble sort algorithm.
This algorithm takes a list and sorts the list.
"""
def bubble_sort(list):
	for iteration in range(0, len(list)):
		for index in range(0, len(list)-1):
			if list[index]>list[index+1]:
				# swap elements at index and index+1
				temp = list[index]
				list[index] = list[index+1]
				list[index+1] = temp

"""
An improved version of bubble sort.
If no swaps are made in an iteration, it means the list is sorted.
This prevents the algorithm from iterating after the list is sorted.
"""
def improved_bubble_sort(list):
	for iteration in range(0, len(list)):
		sorted = True 
		for index in range(0, len(list)-1):
			if list[index]>list[index+1]:
				sorted = False
				# swap elements at index and index+1
				temp = list[index]
				list[index] = list[index+1]
				list[index+1] = temp

		if sorted:
			break

"""
The mainline logic to demonstrate the sorting algorithms.
"""
if __name__ == "__main__":
	list1 = [1, 2, 3, 4, 5]
	list2 = [5, 4, 3, 2, 1]
	list3 = [5, 3, 4, 1, 2]

	bubble_sort(list2)
	bubble_sort(list3)

	print (list1 == list2)
	print (list1 == list3)

	list2 = [5, 4, 3, 2, 1]
	list3 = [5, 3, 4, 1, 2]

	improved_bubble_sort(list2)
	improved_bubble_sort(list3)

	print (list1 == list2)
	print (list1 == list3)

	list4 = [1, 2, 3, 5, 4]

	start = time.time()
	bubble_sort(list4)
	end = time.time()

	print ("Traditional bubble sort time " + str(end-start))

	list4 = [1, 2, 3, 5, 4]

	start = time.time()
	improved_bubble_sort(list4)
	end = time.time()

	print ("Improved bubble sort time " + str(end-start))






