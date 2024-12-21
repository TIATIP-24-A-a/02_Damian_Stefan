import unittest
from quicksort.py import quicksort

class TestSort(unittest.TestCase):
    input: list
    output: list

    # Test
    def test_sort(self):
        testInput = [3, 0, 12, 8]  # Arrange
        testOutput= quicksort(a)  # Act
        self.assertEqual(testOutput, testInput)  # Assert