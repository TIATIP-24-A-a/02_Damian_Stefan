import unittest
from quicksort import quicksort

class TestSort(unittest.TestCase):
    input: list
    output: list

    # Test
    def testUnsorted(self):
        testInput = [8, 3, 1, 7, 0, 10, 2]  # Arrange
        testOutput= quicksort(testInput)  # Act
        self.assertEqual(testOutput, testInput)  # Assert