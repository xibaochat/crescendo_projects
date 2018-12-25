#!/bin/python3

import math
import os
import random
import re
import sys
if __name__ == '__main__':
    try:
        n = int(input())
    except:
        exit('not an int')
    for i in range(1, 11):
        a = n * i
        print("{} x {} = {}".format(n, i, a))
                                            
