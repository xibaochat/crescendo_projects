#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    total_cost = meal_cost  + meal_cost * (tip_percent +tax_percent)/100
        return int(round(total_cost))


    if __name__ == '__main__':
    try:
        meal_cost = float(input())
    except:
        exit('not a float')
    try:
        tip_percent = int(input())
    except:
        exit('not an int')
    try:
        tax_percent = int(input())
    except:
        exit('not an int')
        
    total_price =  solve(meal_cost, tip_percent, tax_percent)
    print(total_price)

    
