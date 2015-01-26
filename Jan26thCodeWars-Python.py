#Problem 9, Python codewars
'''Write a method that returns true if a given parameter is a power of 4, and false if it's not. 
If parameter is not an Integer (eg String, Array) method should return false as well.

Examples

isPowerOf4 1024 #should return True
isPowerOf4  102 #should return False
isPowerOf4   64 #should return True'''

#Solution to problem 9
#Done quickly, yes you can save line effienciency, ill refactor at a later time.

def powerof4(n):
    if (type(n) == str):
        return False
    else if (type(n) == bool):
        return False

    #print(n) used for testing

    if n == 4: #base cases below
        return True
    if n == 1:
        return True
    if (4 > n):
        return False
    
    while (True): #dealing with real value
        print(n)
        if 4 == n:
            return True
        if 4 > n:
            break #how we break
        n /= 4

    return False #last case
