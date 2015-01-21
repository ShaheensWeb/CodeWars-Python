#Problem #4
'''Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
'''

#Solution #1 to Problem #4, This is the one I made 
def solution(string, ending):
    return ((string[-(ending.__len__()):]) == ending) 

#Alternate More Simplistic Solution
#(Solution #2 to Problem #4)
def solution(string, ending):
    return string.endswith(ending)