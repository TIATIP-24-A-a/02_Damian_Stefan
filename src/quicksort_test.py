import unittest
from quicksort import quicksort

class TestSort(unittest.TestCase):
    input: list
    output: list

    # Test
    def test(self):
        testInput = [3, 0, 12, 8]  # Arrange
        testOutput= quicksort(testInput)  # Act
        self.assertEqual(testOutput, testInput)  # Assert