import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    #while quotient is <=1
    #store the remainder
    rem=list()
    while(n>=1):
        val=n%2
        n=n//2
        rem.append(val)
    #calculate the continuous 1's in the list
    size=len(rem)
    count=1
    prev=1
    for c in range(0,size-1):
        # print(c)
        if rem[c]==rem[c+1]==1:
            count+=1
        elif rem[c+1]==0:
            if(prev<count):
                prev=count
                count=1
            else:
                count=1
        #print('index: ',c,'count: ',count,'previous count: ',prev)
    if (prev>count):
        count=prev
        # print(rem[c])
    print(count)