#Problem 6 Python Set
''' Your task is to finish two functions, minimumSum and maximumSum, that take 2 parameters:

values: an array of integers with an arbitrary length; may be positive and negative
n: how many integers should be summed; always 0 or bigger
Example:

values = [5, 4, 3, 2, 1];
minimum_sum(values, 2) #should return 1 + 2 = 3
maximum_sum(values, 3) #should return 3 + 4 + 5 = 12
All values given to the functions will be integers. Also take care of the following special cases:

if values is empty, both functions should return 0
if n is 0, both functions should also return 0
if n is larger than values's length, use the length instead.
'''


#solution to PROBLEM 6: BELOW

def minimum_sum(values, n):
    if n == 0 or len(values) == 0: #base case check as described
        return 0 #return 0 as told 
    v = sorted(values) #sort the values
    returnVal = 0 #make a return variable 
    for x in range(n): #for x in the range of n
        if x < len(values): # if len values < x 
            returnVal += v[x] #add the value that meets bounds to return val
    return returnVal #return the val 

def maximum_sum(values, n):
    if n == 0 or len(values) == 0:
        return 0
    v = sorted(values, reverse=True)
    returnVal = 0
    for x in range(n):
        if x < len(values):
            returnVal += v[x]
    return returnVal

