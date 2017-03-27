import sys
sys.path.insert(0, '../')

from bubble_sort import bubble_sort, improved_bubble_sort
import unittest

"""
This file contains the unit tests for the bubble sort algorithms.
"""
class TestFunction(unittest.TestCase):
	"""
	This tests the traditional bubble sort algorithm with an empty list.
	The list should remain the same.
	"""
	def test_empty_traditional(self):
		list = []
		bubble_sort(list)
		self.assertEqual([], list)

	"""
	This tests the improved bubble sort algorithm with an empty list.
	The list should remain the same.
	"""
	def test_empty_improved(self):
		list = []
		improved_bubble_sort(list)
		self.assertEqual([], list)

	"""
	This tests the traditional bubble sort algorithm with a sorted list.
	The list should remain the same.
	"""
	def test_sorted_traditional(self):
		list = [1, 2, 5, 7, 9]
		bubble_sort(list)
		self.assertEqual([1, 2, 5, 7, 9], list)

	"""
	This tests the improved bubble sort algorithm with a sorted list.
	The list should remain the same.
	"""
	def test_sorted_improved(self):
		list = [1, 2, 5, 7, 9]
		improved_bubble_sort(list)
		self.assertEqual([1, 2, 5, 7, 9], list)

	"""
	This tests the traditional bubble sort with a reversed list.
	The list should be reversed after the method call.
	"""
	def test_reversed_traditional(self):
		list = [9, 7, 5, 2, 1]
		bubble_sort(list)
		self.assertEqual([1, 2, 5, 7, 9], list)

	"""
	This tests the improved bubble sort with a reversed list.
	The list should be reversed after the method call.
	"""
	def test_reversed_improved(self):
		list = [9, 7, 5, 2, 1]
		improved_bubble_sort(list)
		self.assertEqual([1, 2, 5, 7, 9], list)

if __name__ == "__main__":
	unittest.main(exit = False)
