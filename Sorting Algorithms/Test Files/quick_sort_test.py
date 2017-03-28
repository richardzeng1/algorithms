import sys
sys.path.insert(0, '../')

from quick_sort import quick_sort, partition
import unittest
"""
This class contains the unit tests for the merge sort algorithm.
"""
class TestFunction(unittest.TestCase):
	"""
	This tests the quick sort algorithm with an empty list.
	The list should remain the same.
	"""
	def test_empty_list(self):
		list = []
		list = quick_sort(list)
		self.assertEqual([], list)

	"""
	This tests the quick sort algorithm with a sorted list.
	The list should remain the same.
	"""
	def test_sorted_list(self):
		list = [1, 2, 3, 4, 5]
		list = quick_sort(list)
		self.assertEqual([1, 2, 3, 4, 5], list)

	"""
	This tests the quick sort algorithm with a reversed list.
	The original list should be reversed.
	"""
	def test_reverse_list(self):
		list = [9, 7, 5, 3, 1]
		list = quick_sort(list)
		self.assertEqual([1, 3, 5, 7, 9], list)

	"""
	This tests the partition by partitioning an empty list.
	It should return two empty list.
	"""
	def test_empty_partition(self):
		list1, list2 = partition([], 1)
		self.assertEqual(list1, [])
		self.assertEqual(list2, [])

	"""
	This tests the partition helper function by partitioning an unsorted list.
	It should return a partition of the unsorted list based on the pivot.
	"""
	def test_unsorted_partition(self):
		list1, list2 = partition([-10, 8, -6, 4, -2], 0)
		self.assertEqual(list2, [-10, -6, -2])
		self.assertEqual(list1, [8, 4])
		
if __name__ == "__main__":
	unittest.main(exit = False)
