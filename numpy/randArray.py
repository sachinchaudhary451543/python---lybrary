# create numpy arrays with Random Number
# *rand()* >the function is used to generate a rando value between 0 to 1.
import numpy as np
var = np.random.rand(4)
var1 = np.random.rand(2,4)
print("rand: \n", var1)
print(var)




# *randn()* > the function is used to generate a random value close to zero.

var2 = np.random.randn(5)
print(var2)


# *ranf()** > the function for doing samplng i the nympy. it returns an aray of specified shape and fills it with random 
# float in the half-open interval [0.0, 1.0].
var3 = np.random.ranf(9)
print(var3)


# *randint()** >the function is used to generate a random number bebetween a given range.
# var4 = np.random.randint(min,max,total_number)
var4 = np.random.randint(3,6,8)
print(var4)