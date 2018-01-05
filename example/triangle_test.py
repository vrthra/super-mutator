import unittest
from io import StringIO


class TestTriangle(unittest.TestCase):

    def test_equilateral():
        assert triangle(1,1,1) == 'Equilateral'

    def test_isosceles():
        assert triangle(1,2,1) == 'Isosceles'
        assert triangle(2,2,1) == 'Isosceles'
        assert triangle(2,1,2) == 'Isosceles'

    def test_scalene():
        assert triangle(1,2,3) == 'Scalene'

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestTriangle('test_equilateral'))
    suite.addTest(TestTriangle('test_isosceles'))
    suite.addTest(TestTriangle('test_scalene'))
    return suite

def runTest():
    runner = unittest.TextTestRunner(verbosity=0, stream=StringIO(), failfast=True)
    return runner.run(suite())

