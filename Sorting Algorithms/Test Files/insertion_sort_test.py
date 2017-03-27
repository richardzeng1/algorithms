import sys
sys.path.insert(0, '../')

from insertion_sort import insertion_sort, improved_insertion_sort
import unittest

"""
This file contains the unit tests for the insertion sort algorithms.
"""
class TestFunction(unittest.TestCase):
	"""
	This tests the traditional insertion sort algorithm with an empty list.
	The list should remain the same.
	"""
	def test_empty_traditional(self):
		list = []
		insertion_sort(list)
		self.assertEqual([], list)

	"""
	This tests the improved insertion sort algorithm with an empty list.
	The list should remain the same.
	"""
	def test_empty_improved(self):
		list = []
		improved_insertion_sort(list)
		self.assertEqual([], list)

	"""
	This tests the traditional insertion sort algorithm with a sorted list.
	The list should remain the same.
	"""
	def test_sorted_traditional(self):
		list = [1, 2, 5, 7, 9]
		insertion_sort(list)
		self.assertEqual([1, 2, 5, 7, 9], list)

	"""
	This tests the improved insertion sort algorithm with a sorted list.
	The list should remain the same.
	"""
	def test_sorted_improved(self):
		list = [1, 2, 5, 7, 9]
		improved_insertion_sort(list)
		self.assertEqual([1, 2, 5, 7, 9], list)

	"""
	This tests the traditional insertion sort with a reversed list.
	The list should be reversed after the method call.
	"""
	def test_reversed_traditional(self):
		list = [9, 7, 5, 2, 1]
		insertion_sort(list)
		self.assertEqual([1, 2, 5, 7, 9], list)

	"""
	This tests the improved insertion sort with a reversed list.
	The list should be reversed after the method call.
	"""
	def test_reversed_improved(self):
		list = [9, 7, 5, 2, 1]
		improved_insertion_sort(list)
		self.assertEqual([1, 2, 5, 7, 9], list)

if __name__ == "__main__":
	unittest.main(exit = False)
