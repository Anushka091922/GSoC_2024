import unittest
import numpy as np
from histo_testcases import reduced_histogram


class TestReducedHistogram(unittest.TestCase):


    def test_valid_range(self):
        print("Testing valid range with elements [2, 3, 4]:")
        h = np.array([1, 2, 3, 4, 5])
        reduced_h = reduced_histogram(h, 1, 4)
        self.assertEqual(reduced_h.tolist(), [2, 3, 4])  


    def test_out_of_bounds_start(self):
        print("Testing out of bounds start index:")
        h = np.array([1, 2, 3, 4, 5])
        with self.assertRaises(ValueError):
            reduced_histogram(h, -1, 2)  


    def test_out_of_bounds_end(self):
        print("Testing out of bounds end index:")
        h = np.array([1, 2, 3, 4, 5])
        with self.assertRaises(ValueError):
            reduced_histogram(h, 2, 6)  


    def test_maximum_values(self):
        print("Testing with maximum values:")
        h = np.array([1000, 2000, 3000, 4000, 5000])
        reduced_h = reduced_histogram(h, 1, 4)
        self.assertEqual(reduced_h.tolist(), [2000, 3000, 4000])


    def test_negative_values(self):
        print("Testing with negative values:")
        h = np.array([-1, -2, -3, -4, -5])
        reduced_h = reduced_histogram(h, 1, 4)
        self.assertEqual(reduced_h.tolist(), [-2, -3, -4])


    def test_float_values(self):
        print("Testing with float values:")
        h = np.array([1.5, 2.3, 3.7, 4.1, 5.9])
        reduced_h = reduced_histogram(h, 1, 4)
        self.assertEqual(reduced_h.tolist(), [2.3, 3.7, 4.1])


# Read data from the file and execute test cases
if __name__ == "__main__":
    unittest.main()

