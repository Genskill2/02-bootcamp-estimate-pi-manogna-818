import math
import unittest

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
def wallis(n):
   k=2
   for i in range(1,n+1):
     a=4*i*i
     b=a/(a-1)
     k=k*b
   return k
def monte_carlo(n):
  import random
  c_p=0
  s_p=0
  for i in range(0,n):
     x=random.random()
     y=random.random()
     d=(x*x)+(y*y)
     if d<=1:
         c_p=c_p+1
     s_p=s_p+1
     pi=4*c_p/s_p
  return pi       
    
if __name__ == "__main__":
    unittest.main()
