import unittest
from quicksort import quicksort

class TestSort(unittest.TestCase):

    def testEmpty(self):
        test_input = []
        test_output, error = quicksort(test_input)
        self.assertEqual(test_output, [])
        self.assertEqual(error, None)

    def testOneElement(self):
        test_input = [42]
        test_output, error = quicksort(test_input)
        self.assertEqual(test_output, [42])
        self.assertEqual(error, None)

    def testRandom(self):
        test_input = [8, 3, 1, 7, 0, 10, 2]
        test_output, error = quicksort(test_input)
        self.assertEqual(test_output, [0, 1, 2, 3, 7, 8, 10])
        self.assertEqual(error, None)

    def testSorted(self):
        test_input = [1, 2, 3, 4, 5]
        test_output, error = quicksort(test_input)
        self.assertEqual(test_output, [1, 2, 3, 4, 5])
        self.assertEqual(error, None)

    def testReverseSorted(self):
        test_input = [5, 4, 3, 2, 1]
        test_output, error = quicksort(test_input)
        self.assertEqual(test_output, [1, 2, 3, 4, 5])
        self.assertEqual(error, None)

    def testDubbledElements(self):
        test_input = [3, 1, 2, 3, 4, 3]
        test_output, error = quicksort(test_input)
        self.assertEqual(test_output, [1, 2, 3, 3, 3, 4])
        self.assertEqual(error, None)

    def testNegativeElements(self):
        test_input = [0, -1, 3, -5, 2]
        test_output, error = quicksort(test_input)
        self.assertEqual(test_output, [-5, -1, 0, 2, 3])
        self.assertEqual(error, None)

    def testAllTheSame(self):
        test_input = [7, 7, 7, 7]
        test_output, error = quicksort(test_input)
        self.assertEqual(test_output, [7, 7, 7, 7])
        self.assertEqual(error, None)

    def testManyDoubled(self):
        test_input = [4, 5, 4, 4, 6, 4, 5, 5]
        test_output, error = quicksort(test_input)
        self.assertEqual(test_output, [4, 4, 4, 4, 5, 5, 5, 6])
        self.assertEqual(error, None)

    def testFloats(self):
        test_input = [2.1, 3.5, 1.2, 5.7, 0.5]
        test_output, error = quicksort(test_input)
        self.assertEqual(test_output, [0.5, 1.2, 2.1, 3.5, 5.7])
        self.assertEqual(error, None)
    def testMixedTypes(self):
        test_input = ['D', '$', '&', 1, 7]
        test_output, error = quicksort(test_input)
        test_output, error = quicksort(test_input)
        self.assertEqual(test_output, None)
        self.assertEqual(error, Exception("Als Eingabe dürfen nur Zahlen verwendet werden!"))

    def testListOfStrings(self):
        test_input = ['D', '$', '&', 'f', '5']
        test_output, error = quicksort(test_input)
        self.assertEqual(test_output, None)
        self.assertEqual(error, Exception("Als Eingabe dürfen nur Zahlen verwendet werden!"))
