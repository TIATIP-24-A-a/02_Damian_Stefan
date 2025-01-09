import unittest
from quicksort import quicksort

class TestSort(unittest.TestCase):

    def testEmpty(self):
        test_input: list = []
        test_output: list = quicksort(test_input)
        self.assertEqual(test_output, [])

    def testOneElement(self):
        test_input: list = [42]
        test_output: list = quicksort(test_input)
        self.assertEqual(test_output, [42])

    def testUnsorted(self):
        test_input: list = [8, 3, 1, 7, 0, 10, 2]
        test_output: list = quicksort(test_input)
        self.assertEqual(test_output, [0, 1, 2, 3, 7, 8, 10])

    def testSorted(self):
        test_input: list = [1, 2, 3, 4, 5]
        test_output: list = quicksort(test_input)
        self.assertEqual(test_output, [1, 2, 3, 4, 5])

    def testReverseSorted(self):
        test_input: list = [5, 4, 3, 2, 1]
        test_output: list = quicksort(test_input)
        self.assertEqual(test_output, [1, 2, 3, 4, 5])

    def testDubbledElements(self):
        test_input: list = [3, 1, 2, 3, 4, 3]
        test_output: list = quicksort(test_input)
        self.assertEqual(test_output, [1, 2, 3, 3, 3, 4])
