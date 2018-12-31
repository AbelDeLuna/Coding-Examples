#!/bin/python3


import math
import os
import random
import re
import sys


def minimumBribesUpdated(q):
    cPosition = len(q)
    bribes = 0
    while cPosition > 1:
        #check if the current person is in their proper location
        if cPosition != q[cPosition - 1]:
            if cPosition not in q[max(cPosition -3, 0): cPosition-1]:
                return "Too chaotic"
            else:
                indx = q[max(cPosition -3,0): cPosition - 1].index(cPosition) + max(cPosition - 3, 0)
                q[indx] = q[indx +1]
                q[indx + 1] = cPosition
                bribes = bribes + 1
        else:
            cPosition = cPosition - 1
    return bribes

if __name__ == '__main__':
    #t = int(input())
    t = 1

    for t_itr in range(t):
        #n = int(input())
        #n = 8
        #q = list(map(int, input().rstrip().split()))
        #q= [1, 2, 5, 3, 7, 8, 6, 4]
        
        #q = [2,1,4,3,5]
        q = [2, 1, 5, 3, 4]
        print(minimumBribesUpdated(q))
