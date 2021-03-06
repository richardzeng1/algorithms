import sys
sys.path.insert(0, '../')

from selection_sort import selection_sort
import unittest
"""
This class contains the unit tests for the selection sort algorithm.
"""
class TestFunction(unittest.TestCase):
	"""
	This tests the selection sort algorithm with an empty list.
	The list should remain the same.
	"""
	def test_empty_list(self):
		list = []
		selection_sort(list)
		self.assertEqual([], list)

	"""
	This tests the selection sort algorithm with a sorted list.
	The list should remain the same.
	"""
	def test_sorted_list(self):
		list = [1, 2, 3, 4, 5]
		selection_sort(list)
		self.assertEqual([1, 2, 3, 4, 5], list)

	"""
	This tests the selection sort algorithm with a reversed list.
	The original list should be reversed.
	"""
	def test_reverse_list(self):
		list = [9, 7, 5, 3, 1]
		selection_sort(list)
		self.assertEqual([1, 3, 5, 7, 9], list)

if __name__ == "__main__":
	unittest.main(exit = False)
