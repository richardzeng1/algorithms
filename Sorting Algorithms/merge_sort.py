"""
This is the merge sort algorithm.
It is a divide and conquor algorithm and very affective.

Advantages:
	- Simple implementation.
	- On random data, behaves asymptotically O(nlogn). However, real world applications can have variations for improved efficiency.

Time complexity:
	Worst Case: O(nlogn)
	Best Case: O(nlogn)
	Average: O(nlogn)

Space complexity:
	O(n)
"""

"""
Traditional merge sort algorithm.
This function takes in a list and returns sorts the list.
"""
def merge_sort(list):
	if len(list) == 1:
		return list
	else:
		middle = len(list)/2

		left = merge_sort(list[:middle])
		right = merge_sort(list[middle:])

		return merge(left, right)

"""
This is a helper function that merges 2 sorted lists.
This function accepts 2 sorted lists and returns a merged sorted list comprised of the 2 lists.
"""
def merge(list1, list2):
	merged_list = []
	while (len(list1)>0 and len(list2)>0):
		if list1[0]<=list2[0]:
			merged_list.append(list1.pop(0))
		else:
			merged_list.append(list2.pop(0))
	if len(list1)>0:
		merged_list.extend(list1)
	if len(list2)>0:
		merged_list.extend(list2)

	return merged_list

"""
This is the mainline logic of the program.
"""
if __name__ == "__main__":
	list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	list2 = [5, 4, 3, 2, 1, 6, 8, 7, 10, 9]

	list2 = merge_sort(list2)

	print(list1 == list2)


