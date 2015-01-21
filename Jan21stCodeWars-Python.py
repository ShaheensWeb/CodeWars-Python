#Problem #4 Below

'''
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
'''

#Solution 1 to Problem 4
def solution(string, ending):
    return ((string[-(ending.__len__()):]) == ending)

#Solution 2 to Problem 4, which I took from a stackoverflow post

def solution(string, ending):
    return string.endswith(ending)


 # Note to self: when trying complex one line problems like the first solution
 # Ensure that there does not indeed exist a dot function (in python atleast) that 
 # Does exactly what youre function is intended to do. In this case .endswith(ending). 
