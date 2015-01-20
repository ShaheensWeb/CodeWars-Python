#PROBLEM #2 BELOW
'''
    Description:
    
    Today you will build a function which rolls a dice, with a given number of sides and what numbers are somehow scratched out.
    
    To be more clear, that means you'll get a max and min.
    
    dice(2, 7) # returns a value that can be 2, 3, 4, 5, 6, 7
    Good luck!
    
    P.S: You can assume that min will be less than max
'''

#SOLUTION TO PROBLEM#2

from random import randint #from random import randint, a function that given (a,b) r
                           #returns val >= a and b <= val

def dice(minimum, maximum): #function name: dice, parameters: minimum, maximum
    return randint(minimum, maximum) #return randint between those values