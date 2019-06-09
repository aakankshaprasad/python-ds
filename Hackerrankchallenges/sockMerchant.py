#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    stack = list()
    for c in ar:
        if c not in stack:
            stack.append(c)
            #ar.remove(c)
        elif c in stack:
            count += 1
            stack.remove(c)
            #ar.remove(c)

    return count

if __name__ == '__main__':

    n = 9
    ar = [10,20,20,10,10,30,50,10,20]



    result = sockMerchant(n, ar)

    print(result)
