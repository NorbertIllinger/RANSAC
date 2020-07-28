import unittest
from RANSAC.Common import Point
from RANSAC.Common import CircleModel
from RANSAC.Algorithm import BullockCircleFitting
from RANSAC.Common import Util
import os
import skimage

class Test_test_BullockCircleFitting(unittest.TestCase):
    #def test_A(self):
    #    self.fail("Not implemented")

    def test_constructor(self):
        p1=Point(1,1)
        p2=Point(2,2)
        p3=Point(3,3)
        expected_list=list()
        expected_list.append(p1)
        expected_list.append(p2)
        expected_list.append(p3)

        algo=BullockCircleFitting(expected_list)
        self.assertIsNotNone(algo)
        self.assertTrue (p1 in algo._points)
        self.assertTrue (p2 in algo._points)
        self.assertTrue (p3 in algo._points)
        self.assertEqual(len(algo._points),3)
        pass

if __name__ == '__main__':
    unittest.main()
