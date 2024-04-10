
import unittest
import numpy as np
from histo_testcases import reduced_histogram

class TestReducedHistogram(unittest.TestCase):

    def test_valid_range(self):
        print("Testing valid range with elements [2, 3, 4]:")
        h = np.array([1, 2, 3, 4, 5])
        reduced_h = reduced_histogram(h, 1, 4)         self.assertEqual(reduced_h.tolist(), [2, 3, 4])  
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
if __name__ == "__main__":
    unittest.main()




