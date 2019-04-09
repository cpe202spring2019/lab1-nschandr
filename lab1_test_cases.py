import unittest
from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

        t2 = []
        self.assertEqual(max_list_iter(t2), None)

        t3 = [1, 2, 3]
        self.assertEqual(max_list_iter(t3), 3)

        t4 = [0, -2]
        self.assertEqual(max_list_iter(t4), 0)

        self.assertEqual(max_list_iter([1]),1)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])

        t1 = None
        with self.assertRaises(ValueError):
            reverse_rec(t1)

        self.assertEqual(reverse_rec([3]), [3])
        self.assertEqual(reverse_rec([]), None)

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

        l1 = None
        with self.assertRaises(ValueError):
            bin_search(1,0,3,l1)

        self.assertEqual(bin_search(0,0,3,[3,4,5,5]),None)
        self.assertEqual(bin_search(1,0,4,[0,1,2,3,4]),1)
        self.assertEqual(bin_search(4,0,5,[0,1,2,3,4,5]),4)
        self.assertEqual(bin_search(0,0,3,[0,1,2,3]),0)
        self.assertEqual(bin_search(1,0,0,[1]),0)
        self.assertEqual(bin_search(1,0,0,[0]),None)
        self.assertEqual(bin_search(1,2,3,[]),None)

if __name__ == "__main__":
    unittest.main()
