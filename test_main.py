import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_probb_vector(self) : 
       self.assertTrue( len(probs)==5, "the probs array has the wrong length" )
       self.assertTrue( probs[0]==0.5, "the first element of the probs array is incorrect" )
       self.assertTrue( probs[1]==0.1, "the second element of the probs array is incorrect" )
       self.assertTrue( probs[2]==0.2, "the third element of the probs array is incorrect" )
       self.assertTrue( probs[3]==0.05, "the fourth element of the probs array is incorrect" )
       self.assertTrue( probs[4]==0.15, "the fifth element of the probs array is incorrect" )

    def test_variable(self) : 
       mean = 0
       for i in range(100) : mean = mean + myvariable( probs )
       mean = mean  / 100 

       bar = np.sqrt(variance/100)*st.norm.ppf( (0.99 + 1) / 2 )
       self.assertTrue( np.fabs( mean - expectation )<bar, "your function appears to be sampling from the wrong statistical distribution" )

    def test_expectation(self) : 
        myexp, myvar = 0, 0 
        for i in range(5) : 
            myexp = myexp + probs[i]*i
            myvar = myvar + probs[i]*i*i
        self.assertTrue( np.abs( myexp - expectation ) < 1e-7, "you have computed the expectation wrongly )
        self.assertTrue( np.abs( myvar - myexp*myexp - variance ) < 1e-7, "you have computed the variance wrongly )
    
