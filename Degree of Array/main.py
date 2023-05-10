#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'degreeOfArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

#
# Complete the 'degreeOfArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def findLargestDegree(degree_dict): 
    largest_degree = 0

    for values in degree_dict.items():
        # [0] holds number from input array (key), [1] holds everything else (values)
        degree, first_index, last_index = values[1]
        if degree > largest_degree:
            largest_degree = degree
    
    return largest_degree

def degreeOfArray(arr):
    # get degree
    # length of the shorest sub-array with that degree
    
    # examples during interview
    # 1, 1, 2, 3, 2, 1, 2
    # 1, 1, 1, 2, 2, 3, 2
    
    # test case 1 from HackerRank
    # arr = [5,1,2,2]

    degree_dict = {}
    for i in range(len(arr)):        
        if degree_dict.get(arr[i]) is None:
            degree = 1
            first_index = i
            last_index = i
            # store index of first occurrance first time only 
            degree_dict[arr[i]] = (degree, first_index, last_index)
        else:
            degree, first_index, last_index = degree_dict.get(arr[i])
            # digit seen, increase degree by 1
            degree += 1
            # first index already set on first pass
            # store index of last occurrance always (last index where digit was seen) 
            last_index = i
            degree_dict[arr[i]] = (degree, first_index, last_index)
    
    largest_degree = findLargestDegree(degree_dict)
    
    # could filter the dictionary here and only parse the minimized dictionary
    # there are tradeoffs with all engineering. contining with a traditional approach that iterates for simplicity

    #initialize to an unreasonably large value
    minimum_subarray_length = 0xFFFFFFFF
    
    # go through dictiontary 
    for values in degree_dict.items():
        # [0] holds number from input array (key), [1] holds everything else (values)
        degree, first_index, last_index = values[1]
        if(degree == largest_degree):
            subarray_length = last_index - first_index + 1 # +1 to include both ends of the subarray in the length 
            if(subarray_length < minimum_subarray_length):
                minimum_subarray_length = subarray_length

    return minimum_subarray_length

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = degreeOfArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()