# namespace - not affect each other
import math

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

pi = 3.14

print(sin(pi/2))    # user defined funciton - def
print(math.sin(math.pi/2))  # math inside function

from math import sin, pi
print(sin(pi/2))  # output 1.0

# use * - Such an instruction imports all entities from the indicated module.
from module import *  # aggresive form not using in regular code

# import use alias to shorten the qualified names
import pandas as pd
import math as m
import numpy as np
print(m.sin(m.pi/2))
from math import sin as sine, pi as PI
print(sine(PI/2))

#If a module is imported in the above manner and you want to access any of its entities
result = pd.csv("financial.csv")   # prefix the entity's name using dot notation
