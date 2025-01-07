import unittest
from quicksort import quicksort

class TestSort(unittest.TestCase):

    # Test
    def testUnsorted(self):
        test_input: list = [8, 3, 1, 7, 0, 10, 2]  # Arrange
        test_output: list = quicksort(test_input)  # Act
        self.assertEqual(test_output, [0, 1, 2, 3, 7, 8, 10])  # Assert