#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    rem=list()
    count=1
    while n>0:
        a=n%2
        rem.append(a)
        n=n//2
        #print('n=',n)
    #print(rem)
    i=0
    while i<(len(rem)-1):
        if rem[i] & rem[i+1] == 1:
            count+=1
            i+=1
        else:
            i+=1
    print(count)
