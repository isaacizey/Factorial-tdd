import unittest
from factorial import factorial


class Test_factorial(unittest.TestCase):
    """ This method tests the factorial of numbers """

    def test_factorial(self):
        fact = factorial(8)
        self.assertEquals(fact, 40320)

    def test_2_confirm(self):
        fact = factorial(6)
        self.assertEquals(fact, 720)

    def test_negative_int(self):
        fact = factorial(-6)
        self.assertEquals(fact, 0)
    
    def test_zero_exponential(self):
        fact = factorial(0)
        self.assertEquals(fact, 1)

    def test_fraction(self):
        fact = factorial(0.5)
        self.assertEquals(fact, 0)

    def test_factorial_two_confirm(self):
        fact = factorial(2)
        self.assertEquals(fact, 2)

    def test_factorial_one_confirm(self):
        fact = factorial(2)
        self.assertEquals(fact, 2)

    def test_non_int(self):
        fact = factorial("p")
        self.assertEquals(fact, 0)

    def test_floats(self):
        fact = factorial(6.9)
        self.assertEquals(fact, 0
        )
    def test_equations(self):
        fact = factorial(1*2)
        self.assertEquals(fact, 2)



if __name__=="__main__":
  unittest.main()


