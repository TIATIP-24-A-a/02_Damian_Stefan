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

    def testRandom(self):
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

    def testNegativeElements(self):
        test_input: list = [0, -1, 3, -5, 2]
        test_output: list = quicksort(test_input)
        self.assertEqual(test_output, [-5, -1, 0, 2, 3])

    def testAllTheSame(self):
        test_input: list = [7, 7, 7, 7]
        test_output: list = quicksort(test_input)
        self.assertEqual(test_output, [7, 7, 7, 7])

    def testManyDoubled(self):
        test_input: list = [4, 5, 4, 4, 6, 4, 5, 5]
        test_output: list = quicksort(test_input)
        self.assertEqual(test_output, [4, 4, 4, 4, 5, 5, 5, 6])

    def testFloats(self):
        test_input: list = [2.1, 3.5, 1.2, 5.7, 0.5]
        test_output: list = quicksort(test_input)
        self.assertEqual(test_output, [0.5, 1.2, 2.1, 3.5, 5.7])

    def test_numbers_smaller_than_1_or_bigger_than_100(self):
        with self.assertRaises(Exception) as context:
            test_input: list = ['D', '$', '&', 1, 7]
            quicksort(test_input)
        self.assertEqual(str(context.exception), "Als Eingabe dürfen nur Zahlen verwendet werden!")
