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
    if n < 1 or n > 100:
        exit('not in the range')
    if n % 2 == 0 and (n in range(2,5) or n > 20):
        print('Not Weird')
    else:
        print('Weird')

    
