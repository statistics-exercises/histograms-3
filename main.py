import numpy as np

def myvariable( probs ) : 
  myvar = np.random.uniform(0,1) 
  if myvar < probs[0] : return 0
  if myvar < probs[0] + probs[1] : return 1
  # You will need to write the rest of this function here
  
probs = [0.5, 0.1, ]  # You need to fill in the rest of this vector
expectation, variance = 0, 0
# You need to add code to calculate the expectation and the variance from
# the vector of probabilities given above here.

print( expectation, variance, myvariable( probs ), myvariable( probs ), myvariable( probs ) )
