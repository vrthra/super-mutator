import unittest
from io import StringIO


class TestTriangle(unittest.TestCase):

    def test_equilateral(self):
        assert triangle.triangle(1,1,1) == 'Equilateral'

    def test_isosceles(self):
        assert triangle.triangle(1,2,1) != 'Equilateral'
        assert triangle.triangle(2,2,1) != 'Equilateral'
        assert triangle.triangle(1,2,2) != 'Equilateral'

    def test_scalene(self):
        assert triangle.triangle(1,2,3) != 'Equilateral'

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestTriangle('test_equilateral'))
    suite.addTest(TestTriangle('test_isosceles'))
    suite.addTest(TestTriangle('test_scalene'))
    return suite

def runTest():
    runner = unittest.TextTestRunner(verbosity=0, failfast=True)
    return runner.run(suite())

