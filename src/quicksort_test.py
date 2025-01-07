import unittest
from quicksort import quicksort

class TestSort(unittest.TestCase):
    testInput:  list
    testOutput: list

    # Test
    def testUnsorted(self):
        test_input = [8, 3, 1, 7, 0, 10, 2]  # Arrange
        test_output = quicksort(test_input)  # Act
        self.assertEqual(test_output, test_input)  # Assert