#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

# n towers
# each tower is height m
def towerBreakers(n, m):
    #
    # i originally wrote a bunch of game logic / array/stack manipulation code for this question
    # it turns out the solution is more of a "game rules" solution
    #

    # solution from the internet
    # if m ==1 or n%2 == 0:
    #     return 2
    # else:
    #     return 1

    # i don't like multiple returns from functions so refactored into...
    winning_player = 1
    if m ==1 or n%2 == 0:
        winning_player = 2

    # i would also be more descriptive than to name parameters n and m, but that is the function definiton provided

    return winning_player


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
